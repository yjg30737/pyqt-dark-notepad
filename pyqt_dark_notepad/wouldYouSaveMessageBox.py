import os
from PyQt5.QtWidgets import QMessageBox


class WouldYouSaveMessageBox(QMessageBox):
    def __init__(self):
        super().__init__()

        css_file_path = os.path.join(os.path.dirname(os.path.relpath(__file__, os.getcwd())),
                                     r'style/dark_gray_theme.css')
        css_file = open(css_file_path)
        css_code = css_file.read()
        css_file.close()

        self.setStyleSheet(css_code)
