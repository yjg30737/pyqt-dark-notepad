import os

from PyQt5.QtWidgets import QMessageBox
from pyqt_resource_helper import PyQtResourceHelper


class WouldYouSaveMessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        PyQtResourceHelper.setStyleSheet([self], ['style/dark_gray_theme.css'])
        PyQtResourceHelper.setStyleSheet([self], ['style/no_icon_button.css'])
