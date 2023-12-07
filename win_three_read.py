import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

import create_deck

import meanings_dictionary
from tarot_spreads.simple_three import SimpleThreeCard

from win_three_meaning import Ui_ThreeExplainPopup

image_dir = 'images/marseille'

main_meaning = meanings_dictionary.all_full_dict

tarot_spread = SimpleThreeCard()

deck = create_deck.Deck()
deck.shuffle()
cards = deck.list_cards()

class Ui_ThreeReading(object):
    def setupUi(self, UiThreeReading):
        UiThreeReading.setObjectName("UiThreeReading")
        UiThreeReading.resize(707, 502)

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)

        self.fut_img = QtWidgets.QLabel(parent=UiThreeReading)
        self.fut_img.setGeometry(QtCore.QRect(480, 60, 175, 315))
        self.fut_img.setAutoFillBackground(True)
        self.fut_img.setText("")
        self.fut_img.setObjectName("fut_img")
        self.fut_img.setPixmap(pixmap)

        self.decipher_btn = QtWidgets.QPushButton(parent=UiThreeReading)
        self.decipher_btn.setGeometry(QtCore.QRect(179, 450, 361, 30))
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

        self.pre_label = QtWidgets.QLabel(parent=UiThreeReading)
        self.pre_label.setGeometry(QtCore.QRect(260, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pre_label.setFont(font)
        self.pre_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pre_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pre_label.setObjectName("pre_label")

        self.pas_img = QtWidgets.QLabel(parent=UiThreeReading)
        self.pas_img.setGeometry(QtCore.QRect(60, 60, 175, 315))
        self.pas_img.setAutoFillBackground(True)
        self.pas_img.setText("")
        self.pas_img.setObjectName("pas_img")
        self.pas_img.setPixmap(pixmap)

        self.pre_img = QtWidgets.QLabel(parent=UiThreeReading)
        self.pre_img.setGeometry(QtCore.QRect(270, 60, 175, 315))
        self.pre_img.setAutoFillBackground(True)
        self.pre_img.setText("")
        self.pre_img.setObjectName("pre_img")
        self.pre_img.setPixmap(pixmap)

        self.fut_label = QtWidgets.QLabel(parent=UiThreeReading)
        self.fut_label.setGeometry(QtCore.QRect(470, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.fut_label.setFont(font)
        self.fut_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.fut_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fut_label.setObjectName("fut_label")

        self.pas_label = QtWidgets.QLabel(parent=UiThreeReading)
        self.pas_label.setGeometry(QtCore.QRect(50, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pas_label.setFont(font)
        self.pas_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pas_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pas_label.setObjectName("pas_label")

        self.pas_btn = QtWidgets.QPushButton(parent=UiThreeReading)
        self.pas_btn.setGeometry(QtCore.QRect(60, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pas_btn.setFont(font)
        self.pas_btn.setObjectName("pas_btn")
        self.pas_btn.setStyleSheet('''
        QPushButton {
            border:2px solid #aaa;
            border-radius: 5px;
        }
        QPushButton:pressed {
            background-color: #772EFF
        }
        ''')

        self.pas_btn.clicked.connect(self.draw_pas_card)

        self.pre_btn = QtWidgets.QPushButton(parent=UiThreeReading)
        self.pre_btn.setGeometry(QtCore.QRect(270, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pre_btn.setFont(font)
        self.pre_btn.setObjectName("pre_btn")
        self.pre_btn.setStyleSheet('''
        QPushButton {
            border:2px solid #aaa;
            border-radius: 5px;
        }
        QPushButton:pressed {
            background-color: #772EFF
        }
        ''')

        self.pre_btn.clicked.connect(self.draw_pre_card)

        self.fut_btn = QtWidgets.QPushButton(parent=UiThreeReading)
        self.fut_btn.setGeometry(QtCore.QRect(480, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.fut_btn.setFont(font)
        self.fut_btn.setObjectName("fut_btn")
        self.fut_btn.setStyleSheet('''
        QPushButton {
            border:2px solid #aaa;
            border-radius: 5px;
        }
        QPushButton:pressed {
            background-color: #772EFF
        }
        ''')

        self.fut_btn.clicked.connect(self.draw_fut_card)

        self.retranslateUi(UiThreeReading)
        QtCore.QMetaObject.connectSlotsByName(UiThreeReading)

    def draw_pas_card(self):
        pas_card = SimpleThreeCard().past_card
        pic_path = 'images/marseille/{}.png'.format(str(pas_card).replace(" ", "_"))
        self.pas_image = QPixmap(pic_path).scaled(175, 315)
        self.pas_img.setPixmap(self.pas_image)
        self.pas_btn.setText(str(pas_card))
        self.pas_btn.setDisabled(True)

    def draw_pre_card(self):
        pre_card = SimpleThreeCard().present_card
        pic_path = 'images/marseille/{}.png'.format(str(pre_card).replace(" ", "_"))
        self.pre_image = QPixmap(pic_path).scaled(175, 315)
        self.pre_img.setPixmap(self.pre_image)
        self.pre_btn.setText(str(pre_card))
        self.pre_btn.setDisabled(True)

    def draw_fut_card(self):
        fut_card = SimpleThreeCard().future_card
        pic_path = 'images/marseille/{}.png'.format(str(fut_card).replace(" ", "_"))
        self.fut_image = QPixmap(pic_path).scaled(175, 315)
        self.fut_img.setPixmap(self.fut_image)
        self.fut_btn.setText(str(fut_card))
        self.fut_btn.setDisabled(True)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ThreeExplainPopup()
        self.ui.setupUi(self.window)

        pas_drawn = self.pas_btn.text()
        pre_drawn = self.pre_btn.text()
        fut_drawn = self.fut_btn.text()

        if pas_drawn == 'Draw Card' or pre_drawn == 'Draw Card' or fut_drawn == 'Draw Card':
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No cards drawn, please draw a card")
            msg.exec()

        else:
            self.ui.pas_card_title.setText(str(pas_drawn))
            self.ui.pas_card_title.setWordWrap(True)

            self.ui.pre_card_title.setText(str(pre_drawn))
            self.ui.pre_card_title.setWordWrap(True)

            self.ui.fut_card_title.setText(str(fut_drawn))
            self.ui.fut_card_title.setWordWrap(True)

            get_pas_meaning = main_meaning[str(pas_drawn)]
            self.ui.pas_desc.setText(get_pas_meaning)
            self.ui.pas_desc.setWordWrap(True)

            get_pre_meaning = main_meaning[str(pre_drawn)]
            self.ui.pre_desc.setText(get_pre_meaning)
            self.ui.pre_desc.setWordWrap(True)

            get_fut_meaning = main_meaning[str(fut_drawn)]
            self.ui.fut_desc.setText(get_fut_meaning)
            self.ui.fut_desc.setWordWrap(True)

            self.window.show()

    def retranslateUi(self, UiThreeReading):
        _translate = QtCore.QCoreApplication.translate
        UiThreeReading.setWindowTitle(_translate("UiThreeReading", "Classic Three Reading"))
        self.decipher_btn.setText(_translate("UiThreeReading", "Show Explanation"))
        self.pre_label.setText(_translate("UiThreeReading", "Present"))
        self.fut_label.setText(_translate("UiThreeReading", "Future"))
        self.pas_label.setText(_translate("UiThreeReading", "Past"))
        self.pas_btn.setText(_translate("UiThreeReading", "Draw Card"))
        self.pre_btn.setText(_translate("UiThreeReading", "Draw Card"))
        self.fut_btn.setText(_translate("UiThreeReading", "Draw Card"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiThreeReading = QtWidgets.QWidget()
    ui = Ui_ThreeReading()
    ui.setupUi(UiThreeReading)
    UiThreeReading.show()
    sys.exit(app.exec())
