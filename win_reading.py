from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys
import create_deck
import create_spreads

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 1000,500)
        self.setWindowTitle("The App!")

        self.create_reading_button()

    def create_reading_button(self):
        # do hbox thing
        hbox = QHBoxLayout()
        # create button
        reading_button = QPushButton("Reading")
        # add connection when clicked
        reading_button.clicked.connect(self.reading_clicked)
        self.label = QLabel("CARDS!")

        # add button to hbox
        hbox.addWidget(reading_button)
        hbox.addWidget(self.label)

        self.setLayout(hbox)


    def reading_clicked(self):
        deck = create_deck.Deck()
        deck.shuffle()
        simple = create_spreads.SimpleThreeCard()
        self.label.setText(str(simple))
        print(simple)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()