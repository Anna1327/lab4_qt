from PySide2.QtCore import Signal, Slot, Qt
from PySide2.QtWidgets import QMainWindow, QApplication,QToolBar
from ui_stylesheet import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

