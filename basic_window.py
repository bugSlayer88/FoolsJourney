from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Simple Window")

        # self.setWindowIcon(QIcon('images/marseille/01_fool.jpg'))
        # 712 x 1260

        self.label = QLabel('FOOL!')

        self.pixmap = QPixmap('images/marseille/01_fool.jpg')


        self.label.setPixmap(self.pixmap)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        vbox.addWidget(self.label)

        vbox.addLayout(hbox)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
