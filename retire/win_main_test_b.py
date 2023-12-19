from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Simple Window")

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()

        view1 = QLabel("View 1")
        view1.setFont(QFont("Times", 20))

        grid_layout.addWidget(view1)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())