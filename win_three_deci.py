from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

from win_three_meaning import Ui_ThreeExplainPopup

import create_deck
import meanings_dictionary

main_meaning = meanings_dictionary.all_full_dict

deck = create_deck.Deck()
cards = deck.list_cards()


class Ui_ThreeDecipher(object):
    def setupUi(self, ThreeCardDeci):
        ThreeCardDeci.setObjectName("UiThreeDecipher")
        ThreeCardDeci.resize(707, 559)

        self.pas_img = QtWidgets.QLabel(parent=ThreeCardDeci)
        self.pas_img.setGeometry(QtCore.QRect(60, 90, 175, 315))
        self.pas_img.setAutoFillBackground(True)
        self.pas_img.setText("")
        self.pas_img.setObjectName("pas_img")

        self.pre_img = QtWidgets.QLabel(parent=ThreeCardDeci)
        self.pre_img.setGeometry(QtCore.QRect(270, 90, 175, 315))
        self.pre_img.setAutoFillBackground(True)
        self.pre_img.setText("")
        self.pre_img.setObjectName("pre_img")

        self.fut_img = QtWidgets.QLabel(parent=ThreeCardDeci)
        self.fut_img.setGeometry(QtCore.QRect(480, 90, 175, 315))
        self.fut_img.setAutoFillBackground(True)
        self.fut_img.setText("")
        self.fut_img.setObjectName("fut_img")

        self.pas_combo = QtWidgets.QComboBox(parent=ThreeCardDeci)
        self.pas_combo.setGeometry(QtCore.QRect(60, 460, 175, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.pas_combo.setFont(font)
        self.pas_combo.setObjectName("pas_combo")

        self.pas_combo.addItem('Select Card')
        self.pas_combo.addItems(cards)

        self.pas_combo.currentTextChanged.connect(self.pas_combo_update)

        self.pre_combo = QtWidgets.QComboBox(parent=ThreeCardDeci)
        self.pre_combo.setGeometry(QtCore.QRect(270, 460, 175, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.pre_combo.setFont(font)
        self.pre_combo.setObjectName("pre_combo")

        self.pre_combo.addItem('Select Card')
        self.pre_combo.addItems(cards)

        self.pre_combo.currentTextChanged.connect(self.pre_combo_update)

        self.fut_combo = QtWidgets.QComboBox(parent=ThreeCardDeci)
        self.fut_combo.setGeometry(QtCore.QRect(480, 460, 175, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.fut_combo.setFont(font)
        self.fut_combo.setObjectName("fut_combo")

        self.fut_combo.addItem('Select Card')
        self.fut_combo.addItems(cards)

        self.fut_combo.currentTextChanged.connect(self.fut_combo_update)

        self.pas_label = QtWidgets.QLabel(parent=ThreeCardDeci)
        self.pas_label.setGeometry(QtCore.QRect(130, 40, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.pas_label.setFont(font)
        self.pas_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pas_label.setObjectName("pas_label")

        self.pre_label = QtWidgets.QLabel(parent=ThreeCardDeci)
        self.pre_label.setGeometry(QtCore.QRect(320, 40, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.pre_label.setFont(font)
        self.pre_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pre_label.setObjectName("pres_label")

        self.fut_label = QtWidgets.QLabel(parent=ThreeCardDeci)
        self.fut_label.setGeometry(QtCore.QRect(530, 40, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.fut_label.setFont(font)
        self.fut_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.fut_label.setObjectName("fut_label")

        self.decipher_btn = QtWidgets.QPushButton(parent=ThreeCardDeci)
        self.decipher_btn.setGeometry(QtCore.QRect(179, 510, 361, 35))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(16)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.decipher_btn.clicked.connect(self.launch_decipher_window)

        self.retranslateUi(ThreeCardDeci)
        QtCore.QMetaObject.connectSlotsByName(ThreeCardDeci)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ThreeExplainPopup()
        self.ui.setupUi(self.window)
        pas_card_selected = self.pas_combo.currentText()
        pre_card_selected = self.pre_combo.currentText()
        fut_card_selected = self.fut_combo.currentText()

        self.ui.pas_card_title.setText(pas_card_selected + ' Meaning:')
        self.ui.pas_card_title.setWordWrap(True)

        self.ui.pre_card_title.setText(pre_card_selected + ' Meaning:')
        self.ui.pre_card_title.setWordWrap(True)

        self.ui.fut_card_title.setText(fut_card_selected + ' Meaning:')
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

    def pas_combo_update(self):
        pas_selected = self.pas_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(pas_selected.replace(" ","_"))
        self.pas_card_img = QPixmap(pic_path).scaled(175,315)
        self.pas_img.setPixmap(self.pas_card_img)

    def pre_combo_update(self):
        pre_selected = self.pre_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(pre_selected.replace(" ","_"))
        self.pre_card_img = QPixmap(pic_path).scaled(175,315)
        self.pre_img.setPixmap(self.pre_card_img)

    def fut_combo_update(self):
        fut_selected = self.fut_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(fut_selected.replace(" ","_"))
        self.fut_card_img = QPixmap(pic_path).scaled(175,315)
        self.fut_img.setPixmap(self.fut_card_img)

    def retranslateUi(self, UiThreeDecipher):
        _translate = QtCore.QCoreApplication.translate
        UiThreeDecipher.setWindowTitle(_translate("UiThreeDecipher", "Form"))
        self.pas_label.setText(_translate("UiThreeDecipher", "Past"))
        self.pre_label.setText(_translate("UiThreeDecipher", "Present"))
        self.fut_label.setText(_translate("UiThreeDecipher", "Future"))
        self.decipher_btn.setText(_translate("UiThreeDecipher", "Decipher Cards"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiThreeDecipher = QtWidgets.QWidget()
    ui = Ui_ThreeDecipher()
    ui.setupUi(UiThreeDecipher)
    UiThreeDecipher.show()
    sys.exit(app.exec())
