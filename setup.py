from setuptools import setup, find_packages

setup(
    name='pyqt-dark-notepad',
    version='2.1.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_notepad.ico': ['close.svg', 'dark-notepad.svg']},
    description='PyQt dark notepad',
    url='https://github.com/yjg30737/pyqt-dark-notepad.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter>=0.0.1',
        'pyqt-find-replace-text-widget>=0.0.1',
        'pyqt-font-dialog>=0.0.1',
        'pyqt-color-picker>=0.0.1',
        'pyqt-line-number-widget>=0.0.1',
        'pyqt-svg-button>=0.0.1',
        'pyqt-new-window-handler>=0.0.1'
    ]
)