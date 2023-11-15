from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QTransform

from win_celtic_meaning import Ui_CelticDecipherMeanings

import create_deck
import meanings_dictionary

main_meaning_major = meanings_dictionary.major_full_dict
main_meaning_minor = meanings_dictionary.minor_full_dict
main_meaning = meanings_dictionary.all_full_dict

deck = create_deck.Deck()
cards = deck.list_cards()


class Ui_CelticDecipher(object):
    def setupUi(self, UiCelticDecipher):
        UiCelticDecipher.setObjectName("UiCelticDecipher")
        UiCelticDecipher.resize(670, 920)

        self.unw_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.unw_label.setGeometry(QtCore.QRect(510, 640, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.unw_label.setFont(font)
        self.unw_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.unw_label.setObjectName("unw_label")

        self.unw_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.unw_combo.setGeometry(QtCore.QRect(500, 820, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.unw_combo.setFont(font)

        self.unw_combo.addItem('Select Card')
        self.unw_combo.addItems(cards)

        self.unw_combo.currentTextChanged.connect(self.unw_combo_update)

        self.unw_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.unw_img.setGeometry(QtCore.QRect(510, 660, 88, 158))
        self.unw_img.setAutoFillBackground(True)
        self.unw_img.setText("")
        self.unw_img.setObjectName("unw_img")

        self.hom_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.hom_label.setGeometry(QtCore.QRect(530, 430, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.hom_label.setFont(font)
        self.hom_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.hom_label.setObjectName("hom_label")

        self.hom_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.hom_combo.setGeometry(QtCore.QRect(500, 610, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.hom_combo.setFont(font)
        self.hom_combo.setObjectName("hom_combo")

        self.hom_combo.addItem('Select Card')
        self.hom_combo.addItems(cards)

        self.hom_combo.currentTextChanged.connect(self.hom_combo_update)

        self.hom_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.hom_img.setGeometry(QtCore.QRect(510, 450, 88, 158))
        self.hom_img.setAutoFillBackground(True)
        self.hom_img.setText("")
        self.hom_img.setObjectName("hom_img")

        self.hnf_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.hnf_label.setGeometry(QtCore.QRect(490, 220, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.hnf_label.setFont(font)
        self.hnf_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.hnf_label.setObjectName("hnf_label")

        self.hnf_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.hnf_combo.setGeometry(QtCore.QRect(500, 400, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.hnf_combo.setFont(font)
        self.hnf_combo.setObjectName("hnf_combo")

        self.hnf_combo.addItem('Select Card')
        self.hnf_combo.addItems(cards)

        self.hnf_combo.currentTextChanged.connect(self.hnf_combo_update)

        self.hnf_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.hnf_img.setGeometry(QtCore.QRect(510, 240, 88, 158))
        self.hnf_img.setAutoFillBackground(True)
        self.hnf_img.setText("")
        self.hnf_img.setObjectName("hnf_img")

        self.ans_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.ans_label.setGeometry(QtCore.QRect(520, 10, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.ans_label.setFont(font)
        self.ans_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ans_label.setObjectName("ans_label")

        self.ans_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.ans_combo.setGeometry(QtCore.QRect(500, 190, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.ans_combo.setFont(font)
        self.ans_combo.setObjectName("ans_combo")

        self.ans_combo.addItem('Select Card')
        self.ans_combo.addItems(cards)

        self.ans_combo.currentTextChanged.connect(self.ans_combo_update)

        self.ans_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.ans_img.setGeometry(QtCore.QRect(510, 30, 88, 158))
        self.ans_img.setAutoFillBackground(True)
        self.ans_img.setText("")
        self.ans_img.setObjectName("ans_img")

        self.bef_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.bef_combo.setGeometry(QtCore.QRect(360, 490, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.bef_combo.setFont(font)
        self.bef_combo.setObjectName("bef_combo")

        self.bef_combo.addItem('Select Card')
        self.bef_combo.addItems(cards)

        self.bef_combo.currentTextChanged.connect(self.bef_combo_update)

        self.bef_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.bef_img.setGeometry(QtCore.QRect(370, 330, 88, 158))
        self.bef_img.setAutoFillBackground(True)
        self.bef_img.setText("")
        self.bef_img.setObjectName("bef_img")

        self.bef_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.bef_label.setGeometry(QtCore.QRect(380, 310, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.bef_label.setFont(font)
        self.bef_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bef_label.setObjectName("bef_label")

        self.blo_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.blo_img.setGeometry(QtCore.QRect(200, 640, 88, 158))
        self.blo_img.setAutoFillBackground(True)
        self.blo_img.setText("")
        self.blo_img.setObjectName("blo_img")

        self.blo_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.blo_combo.setGeometry(QtCore.QRect(190, 800, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.blo_combo.setFont(font)
        self.blo_combo.setObjectName("blo_combo")

        self.blo_combo.addItem('Select Card')
        self.blo_combo.addItems(cards)

        self.blo_combo.currentTextChanged.connect(self.blo_combo_update)

        self.blo_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.blo_label.setGeometry(QtCore.QRect(200, 620, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.blo_label.setFont(font)
        self.blo_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.blo_label.setObjectName("blo_label")

        self.bhi_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.bhi_label.setGeometry(QtCore.QRect(30, 310, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.bhi_label.setFont(font)
        self.bhi_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bhi_label.setObjectName("bhi_label")

        self.bhi_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.bhi_combo.setGeometry(QtCore.QRect(20, 490, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.bhi_combo.setFont(font)
        self.bhi_combo.setObjectName("bhi_combo")

        self.bhi_combo.addItem('Select Card')
        self.bhi_combo.addItems(cards)

        self.bhi_combo.currentTextChanged.connect(self.bhi_combo_update)

        self.bhi_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.bhi_img.setGeometry(QtCore.QRect(30, 330, 88, 158))
        self.bhi_img.setAutoFillBackground(True)
        self.bhi_img.setText("")
        self.bhi_img.setObjectName("bhi_img")

        self.abv_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.abv_label.setGeometry(QtCore.QRect(190, 20, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.abv_label.setFont(font)
        self.abv_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.abv_label.setObjectName("abv_label")

        self.abv_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.abv_combo.setGeometry(QtCore.QRect(180, 200, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.abv_combo.setFont(font)
        self.abv_combo.setObjectName("abv_combo")

        self.abv_combo.addItem('Select Card')
        self.abv_combo.addItems(cards)

        self.abv_combo.currentTextChanged.connect(self.abv_combo_update)

        self.abv_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.abv_img.setGeometry(QtCore.QRect(190, 40, 88, 158))
        self.abv_img.setAutoFillBackground(True)
        self.abv_img.setText("")
        self.abv_img.setObjectName("abv_img")

        self.obs_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.obs_label.setGeometry(QtCore.QRect(210, 450, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.obs_label.setFont(font)
        self.obs_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_label.setObjectName("obs_label")

        self.obs_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.obs_combo.setGeometry(QtCore.QRect(190, 570, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.obs_combo.setFont(font)
        self.obs_combo.setObjectName("obs_combo")

        self.obs_combo.addItem('Select Card')
        self.obs_combo.addItems(cards)

        self.obs_combo.currentTextChanged.connect(self.obs_combo_update)

        self.obs_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.obs_img.setGeometry(QtCore.QRect(170, 480, 158, 88))
        self.obs_img.setAutoFillBackground(True)
        self.obs_img.setText("")
        self.obs_img.setObjectName("obs_img")

        self.you_img = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.you_img.setGeometry(QtCore.QRect(200, 250, 88, 158))
        self.you_img.setAutoFillBackground(True)
        self.you_img.setText("")
        self.you_img.setObjectName("you_img")

        self.you_label = QtWidgets.QLabel(parent=UiCelticDecipher)
        self.you_label.setGeometry(QtCore.QRect(220, 230, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.you_label.setFont(font)
        self.you_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_label.setObjectName("you_label")

        self.you_combo = QtWidgets.QComboBox(parent=UiCelticDecipher)
        self.you_combo.setGeometry(QtCore.QRect(190, 410, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.you_combo.setFont(font)
        self.you_combo.setObjectName("you_combo")

        self.you_combo.addItem('Select Card')
        self.you_combo.addItems(cards)

        self.you_combo.currentTextChanged.connect(self.you_combo_update)

        self.decipher_btn = QtWidgets.QPushButton(parent=UiCelticDecipher)
        self.decipher_btn.setGeometry(QtCore.QRect(100, 875, 470, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(20)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.decipher_btn.clicked.connect(self.launch_decipher_window)

        self.retranslateUi(UiCelticDecipher)
        QtCore.QMetaObject.connectSlotsByName(UiCelticDecipher)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_CelticDecipherMeanings()
        self.ui.setupUi(self.window)

        you_card_selected = self.you_combo.currentText()
        obs_card_selected = self.obs_combo.currentText()
        abv_card_selected = self.abv_combo.currentText()
        blo_card_selected = self.blo_combo.currentText()
        bhi_card_selected = self.bhi_combo.currentText()
        bef_card_selected = self.bef_combo.currentText()
        unw_card_selected = self.unw_combo.currentText()
        hom_card_selected = self.hom_combo.currentText()
        hnf_card_selected = self.hnf_combo.currentText()
        ans_card_selected = self.ans_combo.currentText()

        self.ui.you_card_title.setText(you_card_selected + ' Meaning:')
        self.ui.you_card_title.setWordWrap(True)

        self.ui.obs_card_title.setText(obs_card_selected + ' Meaning:')
        self.ui.obs_card_title.setWordWrap(True)

        self.ui.abv_card_title.setText(abv_card_selected + ' Meaning:')
        self.ui.abv_card_title.setWordWrap(True)

        self.ui.blo_card_title.setText(blo_card_selected + ' Meaning:')
        self.ui.blo_card_title.setWordWrap(True)

        self.ui.bhi_card_title.setText(bhi_card_selected + ' Meaning:')
        self.ui.bhi_card_title.setWordWrap(True)

        self.ui.bef_card_title.setText(bef_card_selected + ' Meaning:')
        self.ui.bef_card_title.setWordWrap(True)

        self.ui.unw_card_title.setText(unw_card_selected + ' Meaning:')
        self.ui.unw_card_title.setWordWrap(True)

        self.ui.hom_card_title.setText(hom_card_selected + ' Meaning:')
        self.ui.hom_card_title.setWordWrap(True)

        self.ui.hnf_card_title.setText(hnf_card_selected + ' Meaning:')
        self.ui.hnf_card_title.setWordWrap(True)

        self.ui.ans_card_title.setText(ans_card_selected + ' Meaning:')
        self.ui.ans_card_title.setWordWrap(True)

        first_cards = cards[:22]

        get_you_meaning = ''
        if you_card_selected in first_cards:
            get_you_meaning = main_meaning_major[str(you_card_selected)]
        if you_card_selected not in first_cards:
            get_you_meaning = main_meaning_minor[str(you_card_selected)]

        self.ui.you_desc.setText(get_you_meaning)
        self.ui.you_desc.setWordWrap(True)

        get_obs_meaning = ''
        if obs_card_selected in first_cards:
            get_obs_meaning = main_meaning_major[str(obs_card_selected)]
        if obs_card_selected not in first_cards:
            get_obs_meaning = main_meaning_minor[str(obs_card_selected)]

        self.ui.obs_desc.setText(get_obs_meaning)
        self.ui.obs_desc.setWordWrap(True)

        get_abv_meaning = ''
        if abv_card_selected in first_cards:
            get_abv_meaning = main_meaning_major[str(abv_card_selected)]
        if abv_card_selected not in first_cards:
            get_abv_meaning = main_meaning_minor[str(abv_card_selected)]

        self.ui.abv_desc.setText(get_abv_meaning)
        self.ui.abv_desc.setWordWrap(True)

        get_blo_meaning = ''
        if blo_card_selected in first_cards:
            get_blo_meaning = main_meaning_major[str(blo_card_selected)]
        if blo_card_selected not in first_cards:
            get_blo_meaning = main_meaning_minor[str(blo_card_selected)]

        self.ui.blo_desc.setText(get_blo_meaning)
        self.ui.blo_desc.setWordWrap(True)

        get_bhi_meaning = ''
        if bhi_card_selected in first_cards:
            get_bhi_meaning = main_meaning_major[str(bhi_card_selected)]
        if bhi_card_selected not in first_cards:
            get_bhi_meaning = main_meaning_minor[str(bhi_card_selected)]

        self.ui.bhi_desc.setText(get_bhi_meaning)
        self.ui.bhi_desc.setWordWrap(True)

        get_bef_meaning = ''
        if bef_card_selected in first_cards:
            get_bef_meaning = main_meaning_major[str(bef_card_selected)]
        if bef_card_selected not in first_cards:
            get_bef_meaning = main_meaning_minor[str(bef_card_selected)]

        self.ui.bef_desc.setText(get_bef_meaning)
        self.ui.bef_desc.setWordWrap(True)

        get_unw_meaning = ''
        if unw_card_selected in first_cards:
            get_unw_meaning = main_meaning_major[str(unw_card_selected)]
        if unw_card_selected not in first_cards:
            get_unw_meaning = main_meaning_minor[str(unw_card_selected)]

        self.ui.unw_desc.setText(get_unw_meaning)
        self.ui.unw_desc.setWordWrap(True)

        get_hom_meaning = ''
        if hom_card_selected in first_cards:
            get_hom_meaning = main_meaning_major[str(hom_card_selected)]
        if hom_card_selected not in first_cards:
            get_hom_meaning = main_meaning_minor[str(hom_card_selected)]

        self.ui.hom_desc.setText(get_hom_meaning)
        self.ui.hom_desc.setWordWrap(True)

        get_hnf_meaning = ''
        if hnf_card_selected in first_cards:
            get_hnf_meaning = main_meaning_major[str(hnf_card_selected)]
        if hnf_card_selected not in first_cards:
            get_hnf_meaning = main_meaning_minor[str(hnf_card_selected)]

        self.ui.hnf_desc.setText(get_hnf_meaning)
        self.ui.hnf_desc.setWordWrap(True)

        get_ans_meaning = ''
        if ans_card_selected in first_cards:
            get_ans_meaning = main_meaning_major[str(ans_card_selected)]
        if ans_card_selected not in first_cards:
            get_ans_meaning = main_meaning_minor[str(ans_card_selected)]

        self.ui.ans_desc.setText(get_ans_meaning)
        self.ui.ans_desc.setWordWrap(True)

        self.window.show()

    def you_combo_update(self):
        you_selected = self.you_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(you_selected.replace(" ", "_"))
        self.you_card_img = QPixmap(pic_path).scaled(88, 158)
        self.you_img.setPixmap(self.you_card_img)

    def obs_combo_update(self):
        obs_selected = self.obs_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(obs_selected.replace(" ", "_"))
        angle = 90
        self.obs_card_img = QPixmap(pic_path).scaled(88, 158)
        pixmap_rotated = self.obs_card_img.transformed(QTransform().rotate(angle))
        self.obs_img.setPixmap(pixmap_rotated)

    def abv_combo_update(self):
        abv_selected = self.abv_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(abv_selected.replace(" ", "_"))
        self.abv_card_img = QPixmap(pic_path).scaled(88, 158)
        self.abv_img.setPixmap(self.abv_card_img)

    def blo_combo_update(self):
        blo_selected = self.blo_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(blo_selected.replace(" ", "_"))
        self.blo_card_img = QPixmap(pic_path).scaled(88, 158)
        self.blo_img.setPixmap(self.blo_card_img)

    def bhi_combo_update(self):
        bhi_selected = self.bhi_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(bhi_selected.replace(" ", "_"))
        self.bhi_card_img = QPixmap(pic_path).scaled(88, 158)
        self.bhi_img.setPixmap(self.bhi_card_img)

    def bef_combo_update(self):
        bef_selected = self.bef_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(bef_selected.replace(" ", "_"))
        self.bef_card_img = QPixmap(pic_path).scaled(88, 158)
        self.bef_img.setPixmap(self.bef_card_img)

    def unw_combo_update(self):
        unw_selected = self.unw_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(unw_selected.replace(" ", "_"))
        self.unw_card_img = QPixmap(pic_path).scaled(88, 158)
        self.unw_img.setPixmap(self.unw_card_img)

    def hom_combo_update(self):
        hom_selected = self.hom_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(hom_selected.replace(" ", "_"))
        self.hom_card_img = QPixmap(pic_path).scaled(88, 158)
        self.hom_img.setPixmap(self.hom_card_img)

    def hnf_combo_update(self):
        hnf_selected = self.hnf_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(hnf_selected.replace(" ", "_"))
        self.hnf_card_img = QPixmap(pic_path).scaled(88, 158)
        self.hnf_img.setPixmap(self.hnf_card_img)

    def ans_combo_update(self):
        ans_selected = self.ans_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(ans_selected.replace(" ", "_"))
        self.ans_card_img = QPixmap(pic_path).scaled(88, 158)
        self.ans_img.setPixmap(self.ans_card_img)

    def retranslateUi(self, UiCelticDecipher):
        _translate = QtCore.QCoreApplication.translate
        UiCelticDecipher.setWindowTitle(_translate("UiCelticDecipher", "Form"))
        self.unw_label.setText(_translate("UiCelticDecipher", "You Now"))
        self.hom_label.setText(_translate("UiCelticDecipher", "Home"))
        self.hnf_label.setText(_translate("UiCelticDecipher", "Hopes and Fears"))
        self.ans_label.setText(_translate("UiCelticDecipher", "Answer"))
        self.bef_label.setText(_translate("UiCelticDecipher", "You Face"))
        self.blo_label.setText(_translate("UiCelticDecipher", "Below You"))
        self.bhi_label.setText(_translate("UiCelticDecipher", "Behind You"))
        self.abv_label.setText(_translate("UiCelticDecipher", "Above You"))
        self.obs_label.setText(_translate("UiCelticDecipher", "Obstacle"))
        self.you_label.setText(_translate("UiCelticDecipher", "You"))
        self.decipher_btn.setText(_translate("UiCelticDecipher", "Decipher Cards"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    UiCelticDecipher = QtWidgets.QWidget()
    ui = Ui_CelticDecipher()
    ui.setupUi(UiCelticDecipher)
    UiCelticDecipher.show()
    sys.exit(app.exec())
