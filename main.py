import os, sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
from main_test import *


def main(argv):
    app = QApplication(argv)

    w = MainWindow()
    w.show()

    return app.exec_()


if __name__ == "__main__":
    if not "QT_QPA_PLATFORM_PLUGIN_PATH" in os.environ:
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'

    exit_status = main(sys.argv)
    sys.exit(exit_status)
