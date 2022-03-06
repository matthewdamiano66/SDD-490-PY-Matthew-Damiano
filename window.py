
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IMDB Project 1")
        self.setGeometry(200,200, 500,500)
 
        self.create_widgets()
 
 
    def create_widgets(self):
        btn = QPushButton("Generate", self)
        btn.setGeometry(100,100, 200,100)
        btn.setStyleSheet('background-color:Gray')
        btn.setIcon(QIcon("football.png"))
 
 
 
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())