import os

from PyQt5.QtWidgets import QApplication
from pyqt_dark_notepad import DarkNotepad

from pyqt_new_window_handler import NewWindowHandler


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icon_filename = os.path.join(os.path.dirname(__file__), 'ico/dark-notepad.svg')
        self.__handler = NewWindowHandler(DarkNotepad, icon_filename=icon_filename)
