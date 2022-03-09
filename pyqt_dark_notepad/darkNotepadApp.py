from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
from pyqt_dark_notepad import DarkNotepad

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_custom_titlebar_window import CustomTitlebarWindow
from pyqt_new_window_handler import NewWindowHandler
from python_get_absolute_resource_path import get_absolute_resource_path


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler = NewWindowHandler(DarkNotepad, get_absolute_resource_path('ico/dark-notepad.svg'))
