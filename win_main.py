from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Simple Window")
        # self.setWindowIcon(QIcon('images/apple_browser_icon_001.png'))

        self.create_reading_button()

    def create_reading_button(self):
        # do hbox thing
        hbox = QHBoxLayout()
        # create button
        button1 = QPushButton("Reading")
        # add connection when clicked
        button1.clicked.connect(self.reading_clicked)
        # add button to hbox
        hbox.addWidget(button1)

        self.setLayout(hbox)


    def reading_clicked(self):
        print('clicked!')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())