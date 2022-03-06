from PyQt5.QtWidgets import QApplication, qApp
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_dark_notepad import DarkNotepad

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        qApp.installEventFilter(self)
        self.__windowDict = dict()
        self.__new()

    def __new(self):
        mainWindow = DarkNotepad()
        mainWindow.newClicked.connect(self.__new)
        StyleSetter.setWindowStyle(mainWindow)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/dark-notepad.svg')
        self.__titleBarWindow.show()

    def eventFilter(self, obj, e):
        if isinstance(obj, CustomTitlebarWindow):
            if e.type() == 17:
                self.__windowDict[obj] = obj.winId()
            elif e.type() == 19:
                w = self.__windowDict.get(obj, 0)
                if w:
                    self.__windowDict.pop(obj)
        return super().eventFilter(obj, e)