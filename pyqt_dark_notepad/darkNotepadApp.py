from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
from pyqt_dark_notepad import DarkNotepad

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.installEventFilter(self)
        self.__windowDict = dict()
        self.__new()

    def __new(self):
        mainWindow = DarkNotepad()
        mainWindow.newClicked.connect(self.__new)
        StyleSetter.setWindowStyle(mainWindow)
        titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/dark-notepad.svg')
        titleBarWindow.setAttribute(Qt.WA_DeleteOnClose)
        titleBarWindow.destroyed.connect(self.__destroyed)
        titleBarWindow.show()

    def eventFilter(self, obj, e):
        if isinstance(obj, CustomTitlebarWindow):
            if e.type() == 17:
                w = [c for c in obj.children() if isinstance(c, DarkNotepad)][0]
                self.__windowDict[w] = obj
        return super().eventFilter(obj, e)

    def __destroyed(self, w):
        w = [c for c in w.children() if isinstance(c, DarkNotepad)][0]
        del(self.__windowDict[w])