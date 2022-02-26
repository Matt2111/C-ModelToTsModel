import dearpygui.dearpygui as dpg

class Fonts:
    def __init__(self):
        with dpg.font_registry():
            self.default = dpg.add_font("seguisym.ttf", 19)
            self.title = dpg.add_font("seguisym.ttf", 25)

    def SetFont(self):
        dpg.bind_font(self.default)
