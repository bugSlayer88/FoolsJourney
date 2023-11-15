import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

import create_deck
import meanings_dictionary
from win_single_meaning import Ui_Decipher
from tarot_spreads.single_card import SingleCard

main_meaning_major = meanings_dictionary.major_full_dict
main_meaning_minor = meanings_dictionary.minor_full_dict
main_meaning = meanings_dictionary.all_full_dict

image_dir = 'images/marseille'
images = os.listdir(image_dir)
files_path = [os.path.abspath(x) for x in images]

deck = create_deck.Deck()
cards = deck.list_cards()

single_card_drawn = SingleCard.single

class UiSingleDecipher(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(345, 550)

        self.single_img_label = QtWidgets.QLabel(parent=Form)
        self.single_img_label.setGeometry(QtCore.QRect(90, 40, 175, 315))
        self.single_img_label.setText("")
        self.single_img_label.setObjectName("single_img_label")

        self.single_card_combo = QtWidgets.QComboBox(parent=Form)
        self.single_card_combo.setGeometry(QtCore.QRect(90, 430, 175, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(12)
        self.single_card_combo.setFont(font)
        self.single_card_combo.setObjectName("single_card_combo")

        self.single_card_combo.addItem('Select Card')
        self.single_card_combo.addItems(cards)

        self.single_card_combo.currentTextChanged.connect(self.combo_update)

        self.decipher_btn = QtWidgets.QPushButton(parent=Form)
        self.decipher_btn.setGeometry(QtCore.QRect(50, 480, 250, 35))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(16)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.decipher_btn.clicked.connect(self.launch_decipher_window)

        self.select_card_label = QtWidgets.QLabel(parent=Form)
        self.select_card_label.setGeometry(QtCore.QRect(120, 390, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(16)
        self.select_card_label.setFont(font)
        self.select_card_label.setObjectName("select_card_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Decipher()
        self.ui.setupUi(self.window)
        card_selected = self.single_card_combo.currentText()
        self.ui.card_label.setText(card_selected + ' Meaning')

        get_meaning = main_meaning[str(card_selected)]
        self.ui.card_meaning_label.setText(get_meaning)
        self.ui.card_meaning_label.setWordWrap(True)

        self.window.show()


    def combo_update(self):
        single_selected = self.single_card_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(single_selected.replace(" ","_"))
        self.card_image = QPixmap(pic_path).scaled(175,315)
        self.single_img_label.setPixmap(self.card_image)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.decipher_btn.setText(_translate("Form", "Decipher Card"))
        self.select_card_label.setText(_translate("Form", "Select Card:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiSingleDecipher()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
