import os, sys, inspect

from PyQt5.QtWidgets import QPushButton, QApplication
from pyqt_custom_titlebar_window import CustomTitlebarWindow
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_dark_notepad import DarkNotepad


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mainWindow = DarkNotepad()
        self.__setWindowStyle(mainWindow)
        self.__setCustomTitleBar(mainWindow)

    def __setWindowStyle(self, main_window):
        main_window.setStyleSheet(getThemeStyle())  # theme
        btns = main_window.findChildren(QPushButton)  # buttons
        for btn in btns:
            # check if text exists
            if btn.text().strip() == '':
                btn.setStyleSheet(getIconButtonStyle())  # no text - icon button style
            else:
                btn.setStyleSheet(getIconTextButtonStyle())  # text - icon-text button style
        menu_bar = main_window.menuBar()  # menu bar
        menu_bar_style = getMenuBarStyle(menu_bar)
        menu_bar.setStyleSheet(menu_bar_style)

    def __setCustomTitleBar(self, main_window):
        self.__titleBarWindow = CustomTitlebarWindow(main_window)
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
        self.__titleBarWindow.setTopTitleBar(icon_filename=os.path.join(caller_path, 'ico\\dark-notepad.svg'))
        self.__titleBarWindow.setButtons()