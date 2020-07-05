import os, sys
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication
from mainwindow_stylesheet import MainWindow


def main(argv):
    app = QApplication(argv)

    file = QFile('style.txt')
    if not file.open(QIODevice.ReadOnly):
        print('Style sheet is not load')
        return -1

    w = MainWindow()
    w.show()

    stylesheet = file.readAll().data().decode()
    app.setStyleSheet(stylesheet)

    return app.exec_()


if __name__ == "__main__":
    if not "QT_QPA_PLATFORM_PLUGIN_PATH" in os.environ:
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'

    exit_status = main(sys.argv)
    sys.exit(exit_status)