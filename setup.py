from setuptools import setup, find_packages

setup(
    name='pyqt-dark-notepad',
    version='2.0.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_notepad.ico': ['close.svg', 'dark-notepad.svg']},
    description='PyQt5 Dark Notepad',
    url='https://github.com/yjg30737/pyqt-dark-notepad.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-find-replace-text-widget @ git+https://git@github.com/yjg30737/pyqt-find-replace-text-widget.git@main',
        'pyqt-font-dialog @ git+https://git@github.com/yjg30737/pyqt-font-dialog.git@main',
        'pyqt-color-dialog @ git+https://git@github.com/yjg30737/pyqt-color-dialog.git@main',
        'pyqt-line-number-widget @ git+https://git@github.com/yjg30737/pyqt-line-number-widget.git@main',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main',
        'python-get-absolute-resource-path @ git+https://git@github.com/yjg30737/python-get-absolute-resource-path.git@main',
        'pyqt-new-window-handler @ git+https://git@github.com/yjg30737/pyqt-new-window-handler.git@main'
    ]
)