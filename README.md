# pyqt-dark-notepad
PyQt Dark Notepad

## Requirements
* PyQt5 >= 5.8

## Included pacakges
* <a href="https://github.com/yjg30737/pyqt-find-replace-text-widget.git">pyqt-find-replace-text-widget</a>
* <a href="https://github.com/yjg30737/pyqt-font-dialog.git">pyqt-font-dialog</a>
* <a href="https://github.com/yjg30737/pyqt-color-dialog.git">pyqt-color-dialog</a>
* <a href="https://github.com/yjg30737/pyqt-line-number-widget.git">pyqt-line-number-widget</a>

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-dark-notepad.git --upgrade```

## Feature
* New, Open, Save, Save As
* Font, color settings
* Drag and drop from local file and text(local and web)
* Show "Would you save" message box before closing (If untitled or opened file was modified)
* Find, replace texts (option to choose case sensitivity level)
* Zoom in/out, reset (Ctrl+Mouse wheel moving)
* Show various info on status bar
* Show as full screen
* Being able to show/hide menu bar. You can hide menu bar with close button on the right corner of menu bar, show menu bar with place the mouse cursor on the top of the text widget.
* Show line number widget (it doesn't work properly so far)

## Code Example
```python
import sys
from PyQt5.QtWidgets import QApplication
from pyqt_dark_notepad import DarkNotepad

if __name__ == "__main__":
    app = QApplication(sys.argv)
    darkNotepad = DarkNotepad()
    darkNotepad.show()
    sys.exit(app.exec_())
```

## Preview
![image](https://user-images.githubusercontent.com/55078043/148221856-1bfec82a-d17b-4a52-9843-6ccaf1b6d187.png)

## Note
Line edit widget doesn't properly work after user zoom in/out the widget or resize the font.

