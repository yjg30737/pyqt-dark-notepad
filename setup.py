from setuptools import setup, find_packages

setup(
    name='pyqt-dark-notepad',
    version='2.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_notepad.ico': ['close.svg', 'dark-notepad.svg']},
    description='PyQt Dark Notepad',
    url='https://github.com/yjg30737/pyqt-dark-notepad.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main',
        'pyqt-find-replace-text-widget @ git+https://git@github.com/yjg30737/pyqt-find-replace-text-widget.git@main',
        'pyqt-font-dialog @ git+https://git@github.com/yjg30737/pyqt-font-dialog.git@main',
        'pyqt-color-picker>=0.0.1',
        'pyqt-line-number-widget @ git+https://git@github.com/yjg30737/pyqt-line-number-widget.git@main',
        'pyqt-svg-icon-pushbutton>=0.0.1',
        'python-get-absolute-resource-path>=0.0.1',
        'pyqt-new-window-handler @ git+https://git@github.com/yjg30737/pyqt-new-window-handler.git@main'
    ]
)