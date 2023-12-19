from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

from win_three_meaning import Ui_ThreeExplainPopup

import create_deck

import meanings_dictionary

from tarot_spreads.simple_three_input import SimpleThreeCard

main_meaning = meanings_dictionary.all_full_dict

deck = create_deck.Deck()

cards = deck.list_cards()


class Ui_ThreeDecipher(object):
    def setupUi(self, UiThreeDecipher):
        UiThreeDecipher.setObjectName("UiThreeDecipher")
        UiThreeDecipher.resize(707, 505)

        # UiThreeDecipher.setStyleSheet("background-color: #D2BFFF")

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)

        self.pas_img = QtWidgets.QLabel(parent=UiThreeDecipher)
        self.pas_img.setGeometry(QtCore.QRect(60, 60, 175, 315))
        self.pas_img.setAutoFillBackground(True)
        self.pas_img.setText("")
        self.pas_img.setPixmap(pixmap)
        self.pas_img.setObjectName("pas_img")

        self.pre_img = QtWidgets.QLabel(parent=UiThreeDecipher)
        self.pre_img.setGeometry(QtCore.QRect(270, 60, 175, 315))
        self.pre_img.setAutoFillBackground(True)
        self.pre_img.setText("")
        self.pre_img.setPixmap(pixmap)
        self.pre_img.setObjectName("pre_img")

        self.fut_img = QtWidgets.QLabel(parent=UiThreeDecipher)
        self.fut_img.setGeometry(QtCore.QRect(480, 60, 175, 315))
        self.fut_img.setAutoFillBackground(True)
        self.fut_img.setText("")
        self.fut_img.setPixmap(pixmap)
        self.fut_img.setObjectName("fut_img")

        self.pas_combo = QtWidgets.QComboBox(parent=UiThreeDecipher)
        self.pas_combo.setGeometry(QtCore.QRect(60, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pas_combo.setFont(font)
        self.pas_combo.setObjectName("pas_combo")
        self.pas_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.pas_combo.addItem('Select Card')
        self.pas_combo.addItems(cards)

        self.pas_combo.currentTextChanged.connect(self.pas_combo_update)

        self.pre_combo = QtWidgets.QComboBox(parent=UiThreeDecipher)
        self.pre_combo.setGeometry(QtCore.QRect(270, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pre_combo.setFont(font)
        self.pre_combo.setObjectName("pre_combo")
        self.pre_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.pre_combo.addItem('Select Card')
        self.pre_combo.addItems(cards)

        self.pre_combo.currentTextChanged.connect(self.pre_combo_update)

        self.fut_combo = QtWidgets.QComboBox(parent=UiThreeDecipher)
        self.fut_combo.setGeometry(QtCore.QRect(480, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.fut_combo.setFont(font)
        self.fut_combo.setObjectName("fut_combo")
        self.fut_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.fut_combo.addItem('Select Card')
        self.fut_combo.addItems(cards)

        self.fut_combo.currentTextChanged.connect(self.fut_combo_update)

        self.pas_label = QtWidgets.QLabel(parent=UiThreeDecipher)
        self.pas_label.setGeometry(QtCore.QRect(50, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pas_label.setFont(font)
        self.pas_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pas_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pas_label.setObjectName("pas_label")

        self.pres_label = QtWidgets.QLabel(parent=UiThreeDecipher)
        self.pres_label.setGeometry(QtCore.QRect(260, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.pres_label.setFont(font)
        self.pres_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pres_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pres_label.setObjectName("pres_label")

        self.fut_label = QtWidgets.QLabel(parent=UiThreeDecipher)
        self.fut_label.setGeometry(QtCore.QRect(470, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.fut_label.setFont(font)
        self.fut_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.fut_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fut_label.setObjectName("fut_label")

        self.decipher_btn = QtWidgets.QPushButton(parent=UiThreeDecipher)
        self.decipher_btn.setGeometry(QtCore.QRect(179, 450, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")
        self.decipher_btn.setStyleSheet('background-color: #E6DCFF')
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
        # self.decipher_btn.clicked.connect(self.read_summary)

        self.retranslateUi(UiThreeDecipher)
        QtCore.QMetaObject.connectSlotsByName(UiThreeDecipher)

    def pas_combo_update(self):
        pas_selected = self.pas_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(pas_selected.replace(" ", "_"))
        self.pas_card_img = QPixmap(pic_path).scaled(175, 315)
        self.pas_img.setPixmap(self.pas_card_img)

    def pre_combo_update(self):
        pre_selected = self.pre_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(pre_selected.replace(" ", "_"))
        self.pre_card_img = QPixmap(pic_path).scaled(175, 315)
        self.pre_img.setPixmap(self.pre_card_img)

    def fut_combo_update(self):
        fut_selected = self.fut_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(fut_selected.replace(" ", "_"))
        self.fut_card_img = QPixmap(pic_path).scaled(175, 315)
        self.fut_img.setPixmap(self.fut_card_img)

    def read_summary(self):
        past_card = self.pas_combo.currentText()
        present_card = self.pre_combo.currentText()
        future_card = self.fut_combo.currentText()
        print(future_card)
        # print(tarot_spread.quick_summary())
        card_list = SimpleThreeCard(past_card, present_card, future_card)
        print(card_list)
        summary = card_list.quick_summary(past_card, present_card, future_card)
        print(summary)
        # return summary.quick_summary()

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ThreeExplainPopup()
        self.ui.setupUi(self.window)

        pas_card_selected = self.pas_combo.currentText()
        pre_card_selected = self.pre_combo.currentText()
        fut_card_selected = self.fut_combo.currentText()

        if pas_card_selected == "Select Card" or pre_card_selected == "Select Card" or fut_card_selected == ("Select "
                                                                                                             "Card"):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No card selected, please select a card")
            msg.exec()
        else:
            self.ui.pas_card_title.setText(pas_card_selected)
            self.ui.pas_card_title.setWordWrap(True)

            self.ui.pre_card_title.setText(pre_card_selected)
            self.ui.pre_card_title.setWordWrap(True)

            self.ui.fut_card_title.setText(fut_card_selected)
            self.ui.fut_card_title.setWordWrap(True)

            get_pas_meaning = main_meaning[str(pas_card_selected)]

            self.ui.pas_desc.setText(get_pas_meaning)
            self.ui.pas_desc.setWordWrap(True)

            get_pre_meaning = main_meaning[str(pre_card_selected)]

            self.ui.pre_desc.setText(get_pre_meaning)
            self.ui.pre_desc.setWordWrap(True)

            get_fut_meaning = main_meaning[str(fut_card_selected)]

            self.ui.fut_desc.setText(get_fut_meaning)
            self.ui.fut_desc.setWordWrap(True)

            self.window.show()

    def retranslateUi(self, UiThreeDecipher):
        _translate = QtCore.QCoreApplication.translate
        UiThreeDecipher.setWindowTitle(_translate("UiThreeDecipher", "Classic Three Card Decipher"))
        self.pas_label.setText(_translate("UiThreeDecipher", "Past"))
        self.pres_label.setText(_translate("UiThreeDecipher", "Present"))
        self.fut_label.setText(_translate("UiThreeDecipher", "Future"))
        self.decipher_btn.setText(_translate("UiThreeDecipher", "Show Explanation"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    UiThreeDecipher = QtWidgets.QWidget()
    ui = Ui_ThreeDecipher()
    ui.setupUi(UiThreeDecipher)
    UiThreeDecipher.show()
    sys.exit(app.exec())
