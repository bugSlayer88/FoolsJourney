import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

import create_deck

import meanings_dictionary

from win_single_meaning import Ui_Decipher

image_dir = 'images/marseille'

main_meaning = meanings_dictionary.all_full_dict

deck = create_deck.Deck()

deck.shuffle()



class Ui_SingleReading(object):
    def setupUi(self, UiSingleReading):
        UiSingleReading.setObjectName("UiSingleReading")
        UiSingleReading.resize(340, 485)

        self.decipher_btn = QtWidgets.QPushButton(parent=UiSingleReading)
        self.decipher_btn.setGeometry(QtCore.QRect(70, 430, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")
        self.decipher_btn.setStyleSheet('''
        QPushButton {
            border:2px solid #aaa;
            border-radius: 5px;
        }
        QPushButton:pressed {
            background-color: #772EFF
        }
        ''')

        self.decipher_btn.clicked.connect(self.launch_decipher_window)

        self.card_img = QtWidgets.QLabel(parent=UiSingleReading)
        self.card_img.setGeometry(QtCore.QRect(80, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img.setFont(font)
        self.card_img.setAutoFillBackground(True)
        self.card_img.setText("")
        self.card_img.setObjectName("card_img")

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)
        self.card_img.setPixmap(pixmap)

        self.draw_btn = QtWidgets.QPushButton(parent=UiSingleReading)
        self.draw_btn.setGeometry(QtCore.QRect(30, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.draw_btn.setFont(font)
        self.draw_btn.setObjectName("draw_btn")
        self.draw_btn.setStyleSheet('''
        QPushButton {
            border:2px solid #aaa;
            border-radius: 5px;
        }
        QPushButton:pressed {
            background-color: #772EFF
        }
        ''')

        self.draw_btn.clicked.connect(self.draw_card)

        self.retranslateUi(UiSingleReading)
        QtCore.QMetaObject.connectSlotsByName(UiSingleReading)

    def draw_card(self):
        one_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(one_card).replace(" ", "_"))
        self.card_image = QPixmap(pic_path).scaled(175, 315)
        self.card_img.setPixmap(self.card_image)
        self.draw_btn.setText(str(one_card))

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Decipher()
        self.ui.setupUi(self.window)

        card_drawn = self.draw_btn.text()

        if card_drawn == 'Draw Card':
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No card drawn, please draw a card")
            msg.exec()
        else:
            self.ui.card_label.setText(str(card_drawn))
            get_card_meaning = main_meaning[str(card_drawn)]
            self.ui.card_meaning_label.setText(get_card_meaning)
            self.ui.card_meaning_label.setWordWrap(True)

            self.window.show()

    def retranslateUi(self, UiSingleReading):
        _translate = QtCore.QCoreApplication.translate
        UiSingleReading.setWindowTitle(_translate("UiSingleReading", "Single Card Reading"))
        self.decipher_btn.setText(_translate("UiSingleReading", "Show Explanation"))
        self.draw_btn.setText(_translate("UiSingleReading", "Draw Card"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiSingleReading = QtWidgets.QWidget()
    ui = Ui_SingleReading()
    ui.setupUi(UiSingleReading)
    UiSingleReading.show()
    sys.exit(app.exec())
