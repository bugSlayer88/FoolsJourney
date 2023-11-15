import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

import create_deck
import meanings_dictionary

from win_single_meaning import Ui_Decipher

image_dir = 'images/marseille'
images = os.listdir(image_dir)
files_path = [os.path.abspath(x) for x in images]

main_meaning = meanings_dictionary.all_full_dict

deck = create_deck.Deck()
deck.shuffle()
cards = deck.list_cards()

class Ui_SingleReading(object):
    def setupUi(self, UiSingleReading):
        UiSingleReading.setObjectName("UiSingleReading")
        UiSingleReading.resize(269, 558)

        self.card_img = QtWidgets.QLabel(parent=UiSingleReading)
        self.card_img.setGeometry(QtCore.QRect(51, 50, 175, 315))
        self.card_img.setAutoFillBackground(True)
        self.card_img.setText("")
        self.card_img.setObjectName("card_img")

        self.card_label = QtWidgets.QLabel(parent=UiSingleReading)
        self.card_label.setGeometry(QtCore.QRect(80, 20, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.card_label.setFont(font)
        self.card_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.card_label.setObjectName("card_label")

        self.card_btn = QtWidgets.QPushButton(parent=UiSingleReading)
        self.card_btn.setGeometry(QtCore.QRect(50, 440, 175, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(12)
        self.card_btn.setFont(font)
        self.card_btn.setObjectName("card_btn")

        self.card_btn.clicked.connect(self.draw_card)

        self.card_title_label = QtWidgets.QLabel(parent=UiSingleReading)
        self.card_title_label.setGeometry(QtCore.QRect(50, 390, 175, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.card_title_label.setFont(font)
        self.card_title_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.card_title_label.setText("")
        self.card_title_label.setObjectName("card_title_label")

        self.read_cards_btn = QtWidgets.QPushButton(parent=UiSingleReading)
        self.read_cards_btn.setGeometry(QtCore.QRect(20, 490, 225, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.read_cards_btn.setFont(font)
        self.read_cards_btn.setObjectName("read_cards_btn")

        self.read_cards_btn.clicked.connect(self.launch_decipher_window)

        self.retranslateUi(UiSingleReading)
        QtCore.QMetaObject.connectSlotsByName(UiSingleReading)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Decipher()
        self.ui.setupUi(self.window)

        card_drawn = self.card_title_label.text()

        self.ui.card_label.setText(str(card_drawn))

        get_card_meaning = main_meaning[str(card_drawn)]
        self.ui.card_meaning_label.setText(get_card_meaning)
        self.ui.card_meaning_label.setWordWrap(True)

        self.window.show()

    def draw_card(self):
        one_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(one_card).replace(" ", "_"))
        self.card_image = QPixmap(pic_path).scaled(175, 315)
        self.card_img.setPixmap(self.card_image)
        self.card_title_label.setText(str(one_card))

    def retranslateUi(self, UiSingleReading):
        _translate = QtCore.QCoreApplication.translate
        UiSingleReading.setWindowTitle(_translate("UiSingleReading", "Form"))
        self.card_label.setText(_translate("UiSingleReading", "Single Card"))
        self.card_btn.setText(_translate("UiSingleReading", "Draw Card"))
        self.read_cards_btn.setText(_translate("UiSingleReading", "Read My Card!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiSingleReading = QtWidgets.QWidget()
    ui = Ui_SingleReading()
    ui.setupUi(UiSingleReading)
    UiSingleReading.show()
    sys.exit(app.exec())
