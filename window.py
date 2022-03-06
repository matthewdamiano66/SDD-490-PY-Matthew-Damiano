
import sys
from tkinter import Widget
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


def main():
    dx =700
    dy = 500
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(dx, dy)
    w.setWindowTitle('Sprint 4')
    w.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()