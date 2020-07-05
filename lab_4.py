import os, sys
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QLabel


def main(argv):
    app = QApplication(argv)

    label = QLabel("Hello")
    # label.setPixmap(QPixmap('img/qt.png'))
    label.setPixmap(QPixmap(':/img/img/qt.png'))
    label.show()

    return app.exec_()


if __name__ == "__main__":
    if not "QT_QPA_PLATFORM_PLUGIN_PATH" in os.environ:
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'

    exit_status = main(sys.argv)
    sys.exit(exit_status)
