# pyqt-dark-notepad
PyQt Dark Notepad

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-dark-notepad.git --upgrade```

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
