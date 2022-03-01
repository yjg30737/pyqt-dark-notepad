from setuptools import setup, find_packages

setup(
    name='pyqt-dark-notepad',
    version='1.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_notepad.ico': ['close.png', 'dark-notepad.svg']},
    description='Dark notepad made of PyQt5',
    url='https://github.com/yjg30737/pyqt-dark-notepad.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-dark-gray-theme @ git+https://git@github.com/yjg30737/pyqt-dark-gray-theme.git@main',
        'pyqt-custom-titlebar-window @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-window.git@main',
        'pyqt-find-replace-text-widget @ git+https://git@github.com/yjg30737/pyqt-find-replace-text-widget.git@main',
        'pyqt-font-dialog @ git+https://git@github.com/yjg30737/pyqt-font-dialog.git@main',
        'pyqt-color-dialog @ git+https://git@github.com/yjg30737/pyqt-color-dialog.git@main',
        'pyqt-line-number-widget @ git+https://git@github.com/yjg30737/pyqt-line-number-widget.git'
    ]
)