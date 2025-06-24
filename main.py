from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import resources
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.setWindowTitle("PRO STOCK")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.showMaximized()
    sys.exit(app.exec())