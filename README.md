# pyqt-dark-notepad
PyQt dark notepad

## Note
Line edit widget doesn't properly work if text widget's font family is not Gulim.

## Requirements
* PyQt5 >= 5.15

## Included pacakges
* <a href="https://github.com/yjg30737/pyqt-style-setter.git">pyqt-style-setter</a> - For theme
* <a href="https://github.com/yjg30737/pyqt-find-replace-text-widget.git">pyqt-find-replace-text-widget</a>
* <a href="https://github.com/yjg30737/pyqt-font-dialog.git">pyqt-font-dialog</a>
* <a href="https://github.com/yjg30737/pyqt-color-picker.git">pyqt-color-picker</a>
* <a href="https://github.com/yjg30737/pyqt-line-number-widget.git">pyqt-line-number-widget</a>
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a> - for using button which supports svg icon
* <a href="https://github.com/yjg30737/absresgetter.git">absresgetter</a>
* <a href="https://github.com/yjg30737/pyqt-new-window-handler.git">pyqt-new-window-handler</a>

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-dark-notepad.git --upgrade`

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
![image](https://user-images.githubusercontent.com/55078043/161405218-ebaaa931-b494-4a05-850a-d62563251c1a.png)
