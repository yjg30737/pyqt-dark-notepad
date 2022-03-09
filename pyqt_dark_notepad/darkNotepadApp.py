from PyQt5.QtWidgets import QApplication
from pyqt_dark_notepad import DarkNotepad

from pyqt_new_window_handler import NewWindowHandler
from python_get_absolute_resource_path import get_absolute_resource_path


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler = NewWindowHandler(DarkNotepad, get_absolute_resource_path('ico/dark-notepad.svg'))
