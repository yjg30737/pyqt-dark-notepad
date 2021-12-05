import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTextEdit


class DarkNotepadTextEdit(QTextEdit):
    fileDropped = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

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
            # Drop the local text
            else:
                text = e.mimeData().text()
                self.append(text)
        # Drop the web text
        else:
            text = e.mimeData().text()
            self.append(text)
