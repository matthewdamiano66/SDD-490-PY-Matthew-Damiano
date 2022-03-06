
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
        btn = QPushButton("Generate Top 250", self)
        btn.setGeometry(100,100, 200,100)
        btn.setStyleSheet('background-color:Gray')
        btn.setIcon(QIcon("football.png"))
 
        btn2 = QPushButton("Generate Movies",self)
        btn2.setGeometry(300,300, 400,100)
        btn2.setStyleSheet('background-color:Gray')
        btn2.setIcon(QIcon("football.png"))
        
        btn3 = QPushButton("Generate Popular Shows",self)
        btn3.setGeometry(500,500, 400,100)
        btn3.setStyleSheet('background-color:Gray')
        btn3.setIcon(QIcon("football.png"))
 

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
def make_graph():
 print("Window time")
 hi = make_graph()
