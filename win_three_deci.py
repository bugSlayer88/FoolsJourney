from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from win_three_meaning import Ui_ThreeSingleMeaning

import create_deck
from card_analyzer import get_general_meaning, get_negative_meaning

deck = create_deck.Deck()

cards = deck.list_cards()


class Ui_SingleThreeDecipher(object):
    def setupUi(self, SingleDecipher):
        SingleDecipher.setObjectName("SingleDecipher")
        SingleDecipher.resize(962, 485)

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)

        self.card_img_01 = QtWidgets.QLabel(parent=SingleDecipher)
        self.card_img_01.setGeometry(QtCore.QRect(70, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img_01.setFont(font)
        self.card_img_01.setText("")
        self.card_img_01.setPixmap(pixmap)
        self.card_img_01.setObjectName("card_img_01")

        self.single_combo_01 = QtWidgets.QComboBox(parent=SingleDecipher)
        self.single_combo_01.setGeometry(QtCore.QRect(20, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.single_combo_01.setFont(font)
        self.single_combo_01.setObjectName("single_combo_01")

        self.single_combo_01.addItem('Select Card')
        self.single_combo_01.addItems(cards)

        self.single_combo_01.currentTextChanged.connect(self.card01_combo_update)

        self.decipher_btn = QtWidgets.QPushButton(parent=SingleDecipher)
        self.decipher_btn.setGeometry(QtCore.QRect(380, 430, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.decipher_btn.clicked.connect(self.launch_decipher_window)

        self.single_combo_02 = QtWidgets.QComboBox(parent=SingleDecipher)
        self.single_combo_02.setGeometry(QtCore.QRect(340, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.single_combo_02.setFont(font)
        self.single_combo_02.setObjectName("single_combo_02")

        self.single_combo_02.addItem('Select Card')
        self.single_combo_02.addItems(cards)

        self.single_combo_02.currentTextChanged.connect(self.card02_combo_update)

        self.card_img_02 = QtWidgets.QLabel(parent=SingleDecipher)
        self.card_img_02.setGeometry(QtCore.QRect(390, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img_02.setFont(font)
        self.card_img_02.setText("")
        self.card_img_02.setPixmap(pixmap)
        self.card_img_02.setObjectName("card_img_02")

        self.card_img_03 = QtWidgets.QLabel(parent=SingleDecipher)
        self.card_img_03.setGeometry(QtCore.QRect(710, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img_03.setFont(font)
        self.card_img_03.setText("")
        self.card_img_03.setPixmap(pixmap)
        self.card_img_03.setObjectName("card_img_03")

        self.single_combo_03 = QtWidgets.QComboBox(parent=SingleDecipher)
        self.single_combo_03.setGeometry(QtCore.QRect(660, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.single_combo_03.setFont(font)
        self.single_combo_03.setObjectName("single_combo_03")

        self.single_combo_03.addItem('Select Card')
        self.single_combo_03.addItems(cards)

        self.single_combo_03.currentTextChanged.connect(self.card03_combo_update)

        self.retranslateUi(SingleDecipher)
        QtCore.QMetaObject.connectSlotsByName(SingleDecipher)

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

    def card03_combo_update(self):
        card03_selected = self.single_combo_03.currentText()
        pic_path = 'images/marseille/{}.png'.format(card03_selected.replace(" ", "_"))
        self.card_03_img = QPixmap(pic_path).scaled(175,315)
        self.card_img_03.setPixmap(self.card_03_img)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ThreeSingleMeaning()
        self.ui.setupUi(self.window)

        card_01_selected = self.single_combo_01.currentText()
        card_02_selected = self.single_combo_02.currentText()
        card_03_selected = self.single_combo_03.currentText()

        if card_01_selected == 'Select Card' or card_02_selected == 'Select Card' or card_03_selected == 'Select Card':
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Not enough cards selected, please select three cards")
            msg.exec()
        else:
            self.ui.card_01_title.setText(card_01_selected)
            self.ui.card_01_title.setWordWrap(True)

            self.ui.card_02_title.setText(card_02_selected)
            self.ui.card_02_title.setWordWrap(True)

            self.ui.card_03_title.setText(card_03_selected)
            self.ui.card_03_title.setWordWrap(True)

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

            card_03_meaning = get_general_meaning(str(card_03_selected))

            self.ui.card_03_desc.setText(card_03_meaning)
            self.ui.card_03_desc.setWordWrap(True)

            card_03_neg_meaning = get_negative_meaning(str(card_03_selected))

            self.ui.card_03_neg_desc.setText(card_03_neg_meaning)
            self.ui.card_03_neg_desc.setWordWrap(True)

            self.window.show()



    def retranslateUi(self, SingleDecipher):
        _translate = QtCore.QCoreApplication.translate
        SingleDecipher.setWindowTitle(_translate("SingleDecipher", "Form"))
        self.decipher_btn.setText(_translate("SingleDecipher", "Show Explanation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingleDecipher = QtWidgets.QWidget()
    ui = Ui_SingleThreeDecipher()
    ui.setupUi(SingleDecipher)
    SingleDecipher.show()
    sys.exit(app.exec())
