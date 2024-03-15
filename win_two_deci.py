from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from win_two_meaning import Ui_TwoSingleMeaning

import create_deck
from card_analyzer import get_general_meaning, get_negative_meaning

deck = create_deck.Deck()

cards = deck.list_cards()

class Ui_SingleTwoDecipher(object):
    def setupUi(self, TwoDecipher):
        TwoDecipher.setObjectName("SingleDecipher")
        TwoDecipher.resize(680, 485)

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)

        self.card_img_01 = QtWidgets.QLabel(parent=TwoDecipher)
        self.card_img_01.setGeometry(QtCore.QRect(80, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img_01.setFont(font)
        self.card_img_01.setText("")
        self.card_img_01.setPixmap(pixmap)
        self.card_img_01.setObjectName("card_img_01")

        self.single_combo_01 = QtWidgets.QComboBox(parent=TwoDecipher)
        self.single_combo_01.setGeometry(QtCore.QRect(30, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.single_combo_01.setFont(font)
        self.single_combo_01.setObjectName("single_combo_01")

        self.single_combo_01.addItem('Select Card')
        self.single_combo_01.addItems(cards)

        self.single_combo_01.currentTextChanged.connect(self.card01_combo_update)

        self.decipher_btn = QtWidgets.QPushButton(parent=TwoDecipher)
        self.decipher_btn.setGeometry(QtCore.QRect(230, 430, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.decipher_btn.clicked.connect(self.launch_decipher_window)

        self.single_combo_02 = QtWidgets.QComboBox(parent=TwoDecipher)
        self.single_combo_02.setGeometry(QtCore.QRect(350, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.single_combo_02.setFont(font)
        self.single_combo_02.setObjectName("single_combo_02")

        self.single_combo_02.addItem('Select Card')
        self.single_combo_02.addItems(cards)

        self.single_combo_02.currentTextChanged.connect(self.card02_combo_update)

        self.card_img_02 = QtWidgets.QLabel(parent=TwoDecipher)
        self.card_img_02.setGeometry(QtCore.QRect(400, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img_02.setFont(font)
        self.card_img_02.setText("")
        self.card_img_02.setPixmap(pixmap)
        self.card_img_02.setObjectName("card_img_02")

        self.retranslateUi(TwoDecipher)
        QtCore.QMetaObject.connectSlotsByName(TwoDecipher)

    def card01_combo_update(self):
        card01_selected = self.single_combo_01.currentText()
        pic_path = 'images/marseille/{}.png'.format(card01_selected.replace(" ", "_"))
        self.card_01_img = QPixmap(pic_path).scaled(175,315)
        self.card_img_01.setPixmap(self.card_01_img)

    def card02_combo_update(self):
        card02_selected = self.single_combo_02.currentText()
        pic_path = 'images/marseille/{}.png'.format(card02_selected.replace(" ", "_"))
        self.card_02_img = QPixmap(pic_path).scaled(175,315)
        self.card_img_02.setPixmap(self.card_02_img)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_TwoSingleMeaning()
        self.ui.setupUi(self.window)

        card_01_selected = self.single_combo_01.currentText()
        card_02_selected = self.single_combo_02.currentText()

        if card_01_selected == 'Select Card' or card_02_selected == 'Select Card':
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Not enough cards selected, please select three cards")
            msg.exec()
        else:
            self.ui.card_01_title.setText(card_01_selected)
            self.ui.card_01_title.setWordWrap(True)

            self.ui.card_02_title.setText(card_02_selected)
            self.ui.card_02_title.setWordWrap(True)

            card_01_meaning = get_general_meaning(str(card_01_selected))

            self.ui.card_01_desc.setText(card_01_meaning)
            self.ui.card_01_desc.setWordWrap(True)

            card_01_neg_meaning = get_negative_meaning(str(card_01_selected))

            self.ui.card_01_neg_desc.setText(card_01_neg_meaning)
            self.ui.card_01_neg_desc.setWordWrap(True)

            card_02_meaning = get_general_meaning(str(card_02_selected))

            self.ui.card_02_desc.setText(card_02_meaning)
            self.ui.card_02_desc.setWordWrap(True)

            card_02_neg_meaning = get_negative_meaning(str(card_02_selected))

            self.ui.card_02_neg_desc.setText(card_02_neg_meaning)
            self.ui.card_02_neg_desc.setWordWrap(True)

            self.window.show()

    def retranslateUi(self, SingleTwoDecipher):
        _translate = QtCore.QCoreApplication.translate
        SingleTwoDecipher.setWindowTitle(_translate("SingleTwoDecipher", "Form"))
        self.decipher_btn.setText(_translate("SingleTwoDecipher", "Show Explanation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingleTwoDecipher = QtWidgets.QWidget()
    ui = Ui_SingleTwoDecipher()
    ui.setupUi(SingleTwoDecipher)
    SingleTwoDecipher.show()
    sys.exit(app.exec())
