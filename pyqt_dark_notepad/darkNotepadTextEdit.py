from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QTextEdit, QApplication


class DarkNotepadTextEdit(QTextEdit):
    fileDropped = pyqtSignal(str)
    zoomSignal = pyqtSignal(int)
    cursorOnTop = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__scale = 100
        self.__min = 10
        self.__max = 400
        self.__step = 10
        self.__init = 100
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.__cursorOnTopEvent = False

    def dragEnterEvent(self, e):
        super().dragEnterEvent(e)
        if e.mimeData().text():
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        super().dragMoveEvent(e)

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            url = e.mimeData().urls()[-1]
            # Drop the local file (*.txt, *.css ...)
            if url.isLocalFile():
                super().dropEvent(e)
                filename = url.path()[1:]
                self.fileDropped.emit(filename)
            # Drop the local text (as plain text)
            else:
                text = e.mimeData().text()
                self.append(text)
        # Drop the web text (as plain text)
        else:
            text = e.mimeData().text()
            self.append(text)

    def wheelEvent(self, e):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            if e.angleDelta().y() > 0:
                self.zoomIn(10)
            else:
                self.zoomOut(10)
        return super().wheelEvent(e)

    def zoomInit(self):
        default_scale = 100
        if self.__scale > default_scale:
            while True:
                if self.__scale-10 < default_scale:
                    self.__scale = 100
                    self.zoomSignal.emit(self.__scale)
                    break
                self.zoomOut(10)
        else:
            while True:
                if self.__scale+10 > default_scale:
                    self.__scale = 100
                    self.zoomSignal.emit(self.__scale)
                    break
                self.zoomIn(10)

    def zoomIn(self, range: int = ...) -> None:
        if self.__scale < self.__max:
            super().zoomIn()
            self.__scale += 10
            self.zoomSignal.emit(self.__scale)

    def zoomOut(self, range: int = ...) -> None:
        if self.__scale > self.__min:
            super().zoomOut()
            self.__scale -= 10
            self.zoomSignal.emit(self.__scale)

    def setScale(self, scale):
        scale_diff = self.__scale - scale
        if scale_diff < 0:
            self.zoomIn()
        elif scale_diff > 0:
            self.zoomOut()
        else:
            pass

    def getScale(self):
        return self.__scale

    def setCursorOnTopEvent(self, f: bool):
        self.__cursorOnTopEvent = f

    def mouseMoveEvent(self, e):
        p = e.pos()
        y = p.y()
        if self.__cursorOnTopEvent:
            if y < 2:
                self.cursorOnTop.emit()
        return super().mouseMoveEvent(e)