from PyQt5.QtWidgets import QApplication
from pyqt_dark_notepad import DarkNotepad

from pyqt_new_window_handler import NewWindowHandler
import absresgetter


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__handler = NewWindowHandler(DarkNotepad, absresgetter.getabsres('ico/dark-notepad.svg'))
