from PyQt5.QtWidgets import QMessageBox


class WouldYouSaveMessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
