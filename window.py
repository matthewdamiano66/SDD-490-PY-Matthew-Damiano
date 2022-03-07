
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IMDB Project 1")
        self.setGeometry(200,200, 1920,1080)
        self.create_widgets()
    def create_widgets(self):
#button for the generation of the top250 data     
        btn = QPushButton("Generate Top 250", self)
        btn.setGeometry(100,500, 300,100)
        btn.setStyleSheet('background-color:Gray')
        btn.setIcon(QIcon("football.png"))
 #button for the generation of the top movies data     
        btn2 = QPushButton("Generate Movies",self)
        btn2.setGeometry(500,500, 300,100)
        btn2.setStyleSheet('background-color:Gray')
        btn2.setIcon(QIcon("football.png"))
#button for the generation of the pop shows data        
        btn3 = QPushButton("Generate Popular Shows",self)
        btn3.setGeometry(900,500, 300,100)
        btn3.setStyleSheet('background-color:Gray')
        btn3.setIcon(QIcon("football.png"))
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
def make_graph():
 print("Window time")
 hi = make_graph()
