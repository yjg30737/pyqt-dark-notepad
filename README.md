# pyqt-dark-notepad
PyQt Dark Notepad

## Note
Line edit widget doesn't properly work after user zoom in/out the widget or resize the font.

I'm working on "new" feature(It doesn't work properly).

## Requirements
* PyQt5 >= 5.15

## Included pacakges
* <a href="https://github.com/yjg30737/pyqt-style-setter.git">pyqt-style-setter</a> - For theme
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-setter.git">pyqt-custom-titlebar-setter</a> - For frameless window
* <a href="https://github.com/yjg30737/pyqt-find-replace-text-widget.git">pyqt-find-replace-text-widget</a>
* <a href="https://github.com/yjg30737/pyqt-font-dialog.git">pyqt-font-dialog</a>
* <a href="https://github.com/yjg30737/pyqt-color-dialog.git">pyqt-color-dialog</a>
* <a href="https://github.com/yjg30737/pyqt-line-number-widget.git">pyqt-line-number-widget</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a> - For making button support svg icon

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
from pyqt_dark_notepad.darkNotepadApp import DarkNotepadApp


if __name__ == "__main__":
    import sys

    app = DarkNotepadApp(sys.argv)
    app.exec_()
```

## Preview
![image](https://user-images.githubusercontent.com/55078043/156080318-f880a636-2190-4238-aa3c-02e662730451.png)
