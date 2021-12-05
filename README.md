# pyqt-dark-notepad
PyQt Dark Notepad

## Requirements
* PyQt5 >= 5.8

## Included module (Which are automatically installed)
* <a href="https://github.com/yjg30737/pyqt-find-replace-text-widget.git">pyqt-find-replace-text-widget</a>
* <a href="https://github.com/yjg30737/pyqt-font-dialog.git">pyqt-font-dialog</a>
* <a href="https://github.com/yjg30737/pyqt5-color-dialog.git">pyqt5-color-dialog</a>

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-dark-notepad.git --upgrade```

## Feature
* New, Open, Save, Save As
* Font, Color Settings
* Drag and drop from local file and text(local and web)
* Show "Would you save" message box before closing (If untitled or opened file was modified)

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
![image](https://user-images.githubusercontent.com/55078043/144734371-03942647-59e3-454e-9c1c-74c979e28c88.png)
