from external_overlay import ExternalOverlay
from ui import ui
from external_overlay import ExternalOverlay
import dearpygui.dearpygui as dpg


def ui(tar_hwnd=None):
    with dpg.window():
         dpg.add_text("Hello World")


overlay = ExternalOverlay("Диплом переводчик @ Юрьев Григорий Александрович (9362)", ui)
overlay.start()