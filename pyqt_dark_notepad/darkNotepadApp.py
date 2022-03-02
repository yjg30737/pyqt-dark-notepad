import os, sys, inspect

from PyQt5.QtWidgets import QPushButton, QApplication
from pyqt_custom_titlebar_window import CustomTitlebarWindow
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_dark_notepad import DarkNotepad

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = DarkNotepad()
        StyleSetter.setWindowStyle(mainWindow)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename='ico/dark-notepad.svg')
        self.__titleBarWindow.show()