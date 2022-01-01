# pyqt-dark-notepad
PyQt Dark Notepad

## Requirements
* PyQt5 >= 5.8

## Included pacakges
* <a href="https://github.com/yjg30737/pyqt-find-replace-text-widget.git">pyqt-find-replace-text-widget</a>
* <a href="https://github.com/yjg30737/pyqt-font-dialog.git">pyqt-font-dialog</a>
* <a href="https://github.com/yjg30737/pyqt-color-dialog.git">pyqt-color-dialog</a>
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-dark-notepad.git --upgrade```

## Feature
* New, Open, Save, Save As
* Font, color settings
* Drag and drop from local file and text(local and web)
* Show "Would you save" message box before closing (If untitled or opened file was modified)
* Find, replace texts (option to choose case sensitivity level)
* Zoom in/out, reset (Ctrl+Mouse wheel moving)

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
![image](https://user-images.githubusercontent.com/55078043/146741214-c6bb76af-3825-4f76-97da-7fe51ebf8df5.png)

