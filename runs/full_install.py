import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


def full_run():
    print("123")


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
