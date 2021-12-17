from setuptools import setup, find_packages

setup(
    name='pyqt-dark-notepad',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_notepad.style': ['dark_gray_theme.css']},
    description='Dark notepad made of PyQt5',
    url='https://github.com/yjg30737/pyqt-dark-notepad.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-find-replace-text-widget @ git+https://git@github.com/yjg30737/pyqt-find-replace-text-widget.git@main',
        'pyqt-font-dialog @ git+https://git@github.com/yjg30737/pyqt-font-dialog.git@main',
        'pyqt5-color-dialog @ git+https://git@github.com/yjg30737/pyqt5-color-dialog.git@main',
        'pyqt-resource-helpee @ git+https://git@github.com/yjg30737/pyqt-resource-helpee.git@main'
    ]
)