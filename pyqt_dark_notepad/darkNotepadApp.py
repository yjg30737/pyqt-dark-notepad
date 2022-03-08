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
        titleBarWindow.show()

    def eventFilter(self, obj, e):
        if isinstance(obj, CustomTitlebarWindow):
            if e.type() == 17:
                self.__windowDict[obj] = obj.winId()
            elif e.type() == 19:
                currentWidget = obj.getInnerWidget()
                if currentWidget.isChanged():
                    reply = currentWidget.execWouldYouSaveMessageBox()
                    if reply == QMessageBox.Yes:
                        currentWidget.save()
                        w = self.__windowDict.get(obj, 0)
                        if w:
                            self.__windowDict.pop(obj)
                    elif reply == QMessageBox.No:
                        e.accept()
                        w = self.__windowDict.get(obj, 0)
                        if w:
                            self.__windowDict.pop(obj)
                    elif reply == QMessageBox.Cancel:
                        e.ignore()
                        return True

        return super().eventFilter(obj, e)