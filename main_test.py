import unittest
import os, sys

from PySide2.QtCore import Qt, QObject
from PySide2.QtWidgets import QApplication, QPushButton, QLabel
from PySide2.QtTest import QTest
from mainwindow import MainWindow


class MouseClickTest(unittest.TestCase):

    def testQPushButton(self):
        button = QPushButton()
        button.setCheckable(True)
        button.setChecked(False)

        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(button.isChecked())

        QTest.mouseClick(button, Qt.LeftButton)
        self.assertFalse(button.isChecked())

        QApplication.closeAllWindows()

    def testQPushButtonQLabel(self):
        button = QPushButton()
        label = QLabel()
        button.pressed.connect(lambda: label.setText("Hello!"))

        self.assertTrue(label.text() == '')
        QTest.mouseClick(button, Qt.LeftButton)
        self.assertTrue(label.text() == "Hello!")

        QApplication.closeAllWindows()


if __name__ == "__main__":
    if not "QT_QPA_PLATFORM_PLUGIN_PATH" in os.environ:
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'
    app = QApplication()

    unittest.main()
