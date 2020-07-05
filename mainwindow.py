from PySide2.QtCore import Signal, Slot, Qt
from PySide2.QtWidgets import QMainWindow, QApplication,QToolBar
from ui_mainwindow import Ui_MainWindow
# from ui_stylesheet import Ui_MainWindow


class MainWindow(QMainWindow):

    valueChanged = Signal(int)

    @Slot(float)
    def setValue(self, value):
        self.valueChanged.emit(int(value))

    def __init__(self):
        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.action_Exit.triggered.connect(self.exit)

        toolBar = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea, toolBar)
        toolBar.addAction(self.__ui.action_Exit)

    @Slot()
    def exit(self):
        QApplication.quit()
