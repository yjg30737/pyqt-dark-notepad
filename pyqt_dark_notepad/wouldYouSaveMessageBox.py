import os
from PyQt5.QtWidgets import QMessageBox
from pyqt_resource_helper import PyQtResourceHelper


class WouldYouSaveMessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
