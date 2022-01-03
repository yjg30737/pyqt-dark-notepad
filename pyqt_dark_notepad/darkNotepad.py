import os.path

from PyQt5.QtGui import QTextCursor, QColor, QTextDocument
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu, QAction, QFileDialog, qApp, QDialog, \
    QWidget, QVBoxLayout, QMessageBox, QActionGroup, QLabel
from pyqt_color_dialog import ColorPickerDialog
from pyqt_find_replace_text_widget import FindReplaceTextWidget
from pyqt_find_text_widget import FindTextWidget
from pyqt_font_dialog import FontDialog

from pyqt_dark_notepad.darkNotepadTextEdit import DarkNotepadTextEdit
from pyqt_dark_notepad.wouldYouSaveMessageBox import WouldYouSaveMessageBox

from pyqt_resource_helper.pyqtResourceHelper import PyQtResourceHelper


class DarkNotepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__cur_filename = 'Untitled'
        self.__old_text = ''
        self.__new_text = ''
        self.__changed_flag = False
        self.__current_text_color = QColor(255, 255, 255)
        self.__initUi()

    def __initUi(self):
        self.__title = '{0} - Dark notepad'
        self.setWindowTitle(self.__title.format(self.__cur_filename))
        self.__textEdit = DarkNotepadTextEdit()
        self.__textEdit.textChanged.connect(self.__setChangedFlag)
        self.__textEdit.cursorPositionChanged.connect(self.__renewRcInfoInStatusBar)
        self.__textEdit.textChanged.connect(self.__renewCharsLinesCountInStatusBar)
        self.__textEdit.fileDropped.connect(self.__execOpen)
        self.__textEdit.zoomSignal.connect(self.__zoomByWheel)

        # Declare find widget in advance
        self.__findReplaceWidget = FindReplaceTextWidget(self.__textEdit)
        # Hide in default (make it show to use find feature)
        self.__findReplaceWidget.setVisible(False)

        lay = QVBoxLayout()
        lay.addWidget(self.__findReplaceWidget)
        lay.addWidget(self.__textEdit)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

        self.__setStatusBar()
        self.__setActions()
        self.__setMenuBar()

        PyQtResourceHelper.setStyleSheet([self], ['style/dark_gray_theme.css'])

        # Set the text color independently
        self.__textEdit.setTextColor(self.__current_text_color)

    def __setActions(self):
        # filemenu actions
        self.__newAction = QAction('New...')
        self.__newAction.setShortcut('Ctrl+N')
        self.__newAction.triggered.connect(self.__new)

        self.__openAction = QAction('Open...')
        self.__openAction.setShortcut('Ctrl+O')
        self.__openAction.triggered.connect(self.__open)

        self.__saveAction = QAction('Save...')
        self.__saveAction.setShortcut('Ctrl+S')
        self.__saveAction.triggered.connect(self.__save)

        self.__saveAsAction = QAction('Save As...')
        self.__saveAsAction.setShortcut('Ctrl+Shift+S')
        self.__saveAsAction.triggered.connect(self.__saveAs)

        self.__quitAction = QAction('Exit', self)
        self.__quitAction.triggered.connect(qApp.quit)

        # editmenu actions
        self.__findAction = QAction('Find')
        self.__findAction.setShortcut('Ctrl+F')
        self.__findAction.triggered.connect(self.__find)

        self.__replaceAction = QAction('Replace')
        self.__replaceAction.setShortcut('Ctrl+R')
        self.__replaceAction.triggered.connect(self.__replace)

        # formatmenu actions
        self.__fontAction = QAction('Font')
        self.__fontAction.triggered.connect(self.__setFont)

        self.__colorAction = QAction('Color')
        self.__colorAction.triggered.connect(self.__setColor)

        # viewmenu actions
        self.__zoomInAction = QAction('Zoom in')
        self.__zoomInAction.triggered.connect(self.__zoomIn)

        self.__zoomOutAction = QAction('Zoom out')
        self.__zoomOutAction.triggered.connect(self.__zoomOut)

        self.__zoomResetAction = QAction('Reset')
        self.__zoomResetAction.triggered.connect(self.__zoomReset)

        self.__statusBarAction = QAction("Show status bar", self)
        self.__statusBarAction.setCheckable(True)
        self.__statusBarAction.setChecked(True)
        self.__statusBarAction.toggled.connect(self.__statusBar.setVisible)

    def __setMenuBar(self):
        menubar = QMenuBar()

        filemenu = QMenu('File', self)
        filemenu.addAction(self.__newAction)
        filemenu.addAction(self.__openAction)
        filemenu.addAction(self.__saveAction)
        filemenu.addAction(self.__saveAsAction)
        self.__openRecentMenu = filemenu.addMenu('Open Recent')
        self.__initOpenRecentFilesActionMenu()
        filemenu.addSeparator()
        filemenu.addAction(self.__quitAction)

        editmenu = QMenu('Edit', self)
        editmenu.addAction(self.__findAction)
        editmenu.addAction(self.__replaceAction)

        formatmenu = QMenu('Format', self)
        formatmenu.addAction(self.__fontAction)
        formatmenu.addAction(self.__colorAction)

        viewmenu = QMenu('View', self)

        group_menu = viewmenu.addMenu('Zoom in/out')
        group_menu.addAction(self.__zoomInAction)
        group_menu.addAction(self.__zoomOutAction)
        group_menu.addSeparator()
        group_menu.addAction(self.__zoomResetAction)

        viewmenu.addAction(self.__statusBarAction)

        menubar.addMenu(filemenu)
        menubar.addMenu(editmenu)
        menubar.addMenu(formatmenu)
        menubar.addMenu(viewmenu)

        self.setMenuBar(menubar)

    def __setStatusBar(self):
        self.__statusBar = self.statusBar()
        self.__statusBar.setVisible(True)
        self.__statusBar.setSizeGripEnabled(False)
        
        self.__zoomScaleText = '{0}%'
        self.__zoomScaleLabel = QLabel()
        self.__zoomScaleLabel.setText(self.__zoomScaleText.format(self.__textEdit.getScale()))

        self.__fontLabelText = '{0}, {1}pt'
        self.__fontLabel = QLabel()
        font = self.__textEdit.currentFont()
        self.__fontLabel.setText(self.__fontLabelText.format(font.family(), font.pointSize()))

        self.__colorLabelText = '{0}'
        self.__colorLabel = QLabel()
        # todo get initial color properly (supposed to get #FFFFFF get #000000 instead)
        self.__colorLabel.setText(self.__colorLabelText.format('#FFFFFF'))

        self.__rcLabelText = '{0}:{1}'
        self.__rcLabel = QLabel()
        self.__charsLinesCountText = '{0} chars, {1} lines'
        self.__charsLinesCountLabel = QLabel()

        self.__statusBar.addPermanentWidget(self.__zoomScaleLabel)
        self.__statusBar.addPermanentWidget(self.__colorLabel)
        self.__statusBar.addPermanentWidget(self.__fontLabel)
        self.__statusBar.addPermanentWidget(self.__rcLabel)
        self.__statusBar.addPermanentWidget(self.__charsLinesCountLabel)
        self.__renewRcInfoInStatusBar()
        self.__renewCharsLinesCountInStatusBar()

    def __renewRcInfoInStatusBar(self):
        cur = self.__textEdit.textCursor()
        r, c = cur.blockNumber()+1, cur.positionInBlock()+1
        self.__rcLabel.setText(self.__rcLabelText.format(r, c))

    def __renewCharsLinesCountInStatusBar(self):
        self.__charsLinesCountLabel.setText(self.__charsLinesCountText.format(len(self.__textEdit.toPlainText()),
                                                                                  self.__textEdit.document().lineCount()))

    def __setChangedFlag(self):
        self.__new_text = self.__textEdit.toPlainText()
        self.__changed_flag = not self.__old_text == self.__new_text

    def __new(self):
        self.__new_window = DarkNotepad()
        self.__new_window.show()

    def __execWouldYouSaveMessageBox(self):
        saveMsgBox = WouldYouSaveMessageBox()
        saveMsgBox.setText('Do you want to save your changes?')
        saveMsgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        reply = saveMsgBox.exec()
        return reply

    def __open(self):
        if self.__changed_flag:
            reply = self.__execWouldYouSaveMessageBox()
            if reply == QMessageBox.Yes:
                self.__save()
            elif reply == QMessageBox.No:
                pass
            elif reply == QMessageBox.Cancel:
                return
            else:
                return
        filename = QFileDialog.getOpenFileName(self, 'Open', '', 'Text File (*.txt)')
        if filename[0]:
            filename = filename[0]
            self.__execOpen(filename)

    def __execOpen(self, filename):
        self.__setFileContent(filename)
        self.__setTitle(filename)
        self.__changed_flag = False

    def __setFileContent(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.__setText(f)
        except Exception:
            try:
                with open(filename, 'r') as f:
                    self.__setText(f)
            except Exception:
                return

    def __setText(self, filename):
        contents = filename.read()
        self.__textEdit.setText(contents)
        self.__old_text = contents

    def __setTitle(self, filename):
        self.__cur_filename = filename
        self.setWindowTitle(self.__title.format(self.__cur_filename))

    def __save(self):
        if self.__cur_filename == 'Untitled':
            self.__execSaveDialog()
        else:
            self.__execSave(self.__cur_filename)

    def __saveAs(self):
        self.__execSaveDialog()

    def __execSaveDialog(self):
        dirname = os.path.dirname(self.__cur_filename)
        filename = QFileDialog.getSaveFileName(self, 'Save As...', dirname, "Text File (*.txt)")
        filename = filename[0]
        if filename:
            self.__execSave(filename)

    def __execSave(self, filename):
        try:
            f = open(filename, 'w')
            contents = self.__textEdit.toPlainText()
            f.write(contents)
            f.close()
            if self.__cur_filename == filename:
                pass
            else:
                self.__setTitle(filename)
            self.__old_text = contents
            self.__changed_flag = False
        except Exception as e:
            print(e)

    def __find(self):
        self.__findReplaceWidget.setVisible(True)
        self.__findReplaceWidget.setOnlyFindTextWidget(True)
        self.__findReplaceWidget.setFocus()

    def __replace(self):
        self.__findReplaceWidget.setVisible(True)
        self.__findReplaceWidget.setOnlyFindTextWidget(False)
        self.__findReplaceWidget.setFocus()

    def __setFont(self):
        font = self.__textEdit.font()
        font.setPointSize(int(self.__fontLabel.text().split(',')[1][:-2]))
        dialog = FontDialog(font)
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            font = dialog.getFont()
            self.__textEdit.setFont(font)
            self.__fontLabel.setText(self.__fontLabelText.format(font.family(), font.pointSize()))

    def __setColor(self):
        color = self.__textEdit.textColor()
        dialog = ColorPickerDialog(color)
        reply = dialog.exec()
        if reply == QDialog.Accepted:
            color = dialog.getColor()

            # Set existing text color of textedit
            self.__textEdit.selectAll()
            self.__textEdit.setTextColor(color)
            tc = self.__textEdit.textCursor()
            tc.clearSelection()
            self.__textEdit.setTextCursor(tc)

            tc = self.__textEdit.textCursor()
            tc.movePosition(QTextCursor.Start)

            # Set text color of textedit in general
            self.__textEdit.setTextColor(color)

            self.__colorLabel.setText(self.__colorLabelText.format(color.name()))

    def __zoomByWheel(self, n):
        self.__zoomScaleLabel.setText(self.__zoomScaleText.format(n))
        self.__zoomInAction.setEnabled(n < 400)
        self.__zoomOutAction.setEnabled(n > 10)

    def __zoomIn(self):
        self.__textEdit.zoomIn(10)
        self.__zoomScaleLabel.setText(self.__zoomScaleText.format(self.__textEdit.getScale()))

    def __zoomOut(self):
        self.__textEdit.zoomOut(10)
        self.__zoomScaleLabel.setText(self.__zoomScaleText.format(self.__textEdit.getScale()))

    def __zoomReset(self):
        self.__textEdit.zoomInit()
        self.__zoomScaleLabel.setText(self.__zoomScaleText.format(100))

    def closeEvent(self, e):
        if self.__changed_flag:
            reply = self.__execWouldYouSaveMessageBox()
            if reply == QMessageBox.Yes:
                self.__save()
            elif reply == QMessageBox.No:
                e.accept()
            elif reply == QMessageBox.Cancel:
                e.ignore()
            else:
                e.ignore()

    def __initOpenRecentFilesActionMenu(self):
        noRecentFilesTextAction = QAction('No recent files', self)
        noRecentFilesTextAction.setEnabled(False)
        self.__openRecentMenu.addAction(noRecentFilesTextAction)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    darkNotepad = DarkNotepad()
    darkNotepad.show()
    app.exec_()