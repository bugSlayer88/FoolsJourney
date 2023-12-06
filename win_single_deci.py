import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

import create_deck

import meanings_dictionary
from win_single_meaning import Ui_Decipher

main_meaning = meanings_dictionary.all_full_dict

image_dir = 'images/marseille'

deck = create_deck.Deck()

cards = deck.list_cards()

class Ui_SingleDecipher(object):
    def setupUi(self, SingleDecipher):
        SingleDecipher.setObjectName("SingleDecipher")
        SingleDecipher.resize(340, 485)

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)

        self.card_img = QtWidgets.QLabel(parent=SingleDecipher)
        self.card_img.setGeometry(QtCore.QRect(80, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img.setFont(font)
        self.card_img.setText("")
        self.card_img.setObjectName("card_img")
        self.card_img.setPixmap(pixmap)

        self.single_combo = QtWidgets.QComboBox(parent=SingleDecipher)
        self.single_combo.setGeometry(QtCore.QRect(30, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.single_combo.setFont(font)
        self.single_combo.setObjectName("single_combo")
        self.single_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.single_combo.addItem('Select Card')
        self.single_combo.addItems(cards)

        self.single_combo.currentTextChanged.connect(self.combo_update)

        self.decipher_btn = QtWidgets.QPushButton(parent=SingleDecipher)
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

        self.decipher_btn.clicked.connect(self.launch_meaning_window)

        self.retranslateUi(SingleDecipher)
        QtCore.QMetaObject.connectSlotsByName(SingleDecipher)

    def combo_update(self):
        single_selected = self.single_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(single_selected.replace(" ", "_"))
        self.single_card_image = QPixmap(pic_path).scaled(175, 315)
        self.card_img.setPixmap(self.single_card_image)


    def launch_meaning_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Decipher()
        self.ui.setupUi(self.window)

        card_selected = self.single_combo.currentText()
        if card_selected == 'Select Card':
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No card selected, please select a card")
            msg.exec()
        else:
            self.ui.card_label.setText(card_selected)

            get_meaning = main_meaning[str(card_selected)]
            self.ui.card_meaning_label.setText(get_meaning)
            self.ui.card_meaning_label.setWordWrap(True)

            self.window.show()

    def retranslateUi(self, SingleDecipher):
        _translate = QtCore.QCoreApplication.translate
        SingleDecipher.setWindowTitle(_translate("SingleDecipher", "Decipher Single Card"))
        self.decipher_btn.setText(_translate("SingleDecipher", "Show Explanation"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SingleDecipher = QtWidgets.QWidget()
    ui = Ui_SingleDecipher()
    ui.setupUi(SingleDecipher)
    SingleDecipher.show()
    sys.exit(app.exec())
