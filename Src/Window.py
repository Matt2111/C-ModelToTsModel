import dearpygui.dearpygui as dpg
from Converter import Converter
from Types import Types
types = Types()

def ConvertModels():
    converter = Converter()
    try:
        dpg.set_value("convertedModel", converter.Convert(dpg.get_value("cModel")))
    except IndexError:
        pass

def SetType():
    fromType, toType = dpg.get_value("from"), dpg.get_value("to")
    if fromType and toType:
        types.Set(fromType, toType)
        ConvertModels()
        UpdateTypes()
        dpg.set_value("from", "")
        dpg.set_value("to", "")

def Remove():
    types.Remove(dpg.get_value("remove").split(" -> ")[0])
    UpdateTypes()
    ConvertModels()

def UpdateTypes():
    dpg.configure_item("remove", items=[f"{_} -> {types.Read(_)}" for _ in types.types])
    dpg.set_value("remove", "Remove")

def MainWindow():
    with dpg.window(label="Dear PyGui Demo", tag="main", no_scrollbar=True):
        with dpg.menu_bar():
            with dpg.menu(label="Types"):
                with dpg.menu(label="Set Type"):
                    dpg.add_input_text(hint="From", width=100, tag="from")
                    dpg.add_input_text(hint="To", width=100, tag="to")
                    dpg.add_button(label="Set", callback=SetType)
                with dpg.menu(label="Remove Type"):
                    dpg.add_combo(width=100, callback=Remove, tag="remove")
                    UpdateTypes()
        with dpg.table(header_row=False):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("C# Model")
                dpg.add_text("TypeScript Model")
            with dpg.table_row():
                dpg.add_input_text(multiline=True, tab_input=True, callback=ConvertModels, tag="cModel",
                                   width=-1, height=-1)
                dpg.add_input_text(multiline=True, readonly=True, tag="convertedModel",
                                   width=-1, height=-1)
