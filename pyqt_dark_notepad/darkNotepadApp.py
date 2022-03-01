from PyQt5.QtWidgets import QPushButton, QApplication
from pyqt_custom_titlebar_window import CustomTitlebarWindow
from pyqt_dark_gray_theme.darkGrayTheme import *
from pyqt_dark_notepad import DarkNotepad


class DarkNotepadApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ex = DarkNotepad()
        ex.setStyleSheet(getThemeStyle())  # theme
        btns = ex.findChildren(QPushButton)  # buttons
        for btn in btns:
            # check if text exists
            if btn.text().strip() == '':
                btn.setStyleSheet(getIconButtonStyle())  # no text - icon button style
            else:
                btn.setStyleSheet(getIconTextButtonStyle())  # text - icon-text button style
        menu_bar = ex.menuBar()  # menu bar
        menu_bar_style = getMenuBarStyle(menu_bar)
        menu_bar.setStyleSheet(menu_bar_style)
        self.__window = CustomTitlebarWindow(ex)
        self.__window.setTopTitleBar(icon_filename='dark-notepad.svg')
        self.__window.setButtons()
        self.__window.show()