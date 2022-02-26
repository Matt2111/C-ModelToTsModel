import dearpygui.dearpygui as dpg
from Fonts import Fonts
from Window import MainWindow


def main():
    dpg.create_context()
    dpg.create_viewport(width=840, height=685, title="Model To Model", large_icon="c2c.ico")
    dpg.setup_dearpygui()

    fonts = Fonts()
    fonts.SetFont()

    MainWindow()

    dpg.set_primary_window("main", True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    main()
