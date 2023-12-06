import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QTransform

import create_deck
import meanings_dictionary

from win_celtic_meaning import Ui_CelticDecipherMeanings

image_dir = 'images/marseille'
images = os.listdir(image_dir)
files_path = [os.path.abspath(x) for x in images]

main_meaning = meanings_dictionary.all_full_dict

deck = create_deck.Deck()
deck.shuffle()
cards = deck.list_cards()

class Ui_CelticReading(object):
    def setupUi(self, UiCelticReading):
        UiCelticReading.setObjectName("UiCelticReading")
        UiCelticReading.resize(669, 863)

        self.bhi_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.bhi_label.setGeometry(QtCore.QRect(20, 320, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.bhi_label.setFont(font)
        self.bhi_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bhi_label.setObjectName("bhi_label")

        self.ans_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.ans_img.setGeometry(QtCore.QRect(500, 40, 120, 158))
        self.ans_img.setAutoFillBackground(True)
        self.ans_img.setText("")
        self.ans_img.setObjectName("ans_img")

        self.you_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.you_label.setGeometry(QtCore.QRect(220, 220, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.you_label.setFont(font)
        self.you_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_label.setObjectName("you_label")

        self.ans_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.ans_label.setGeometry(QtCore.QRect(510, 20, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.ans_label.setFont(font)
        self.ans_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ans_label.setObjectName("ans_label")

        self.hom_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.hom_label.setGeometry(QtCore.QRect(520, 440, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.hom_label.setFont(font)
        self.hom_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.hom_label.setObjectName("hom_label")

        self.abv_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.abv_label.setGeometry(QtCore.QRect(180, 10, 101, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.abv_label.setFont(font)
        self.abv_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.abv_label.setObjectName("abv_label")

        self.blo_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.blo_img.setGeometry(QtCore.QRect(190, 650, 120, 158))
        self.blo_img.setAutoFillBackground(True)
        self.blo_img.setText("")
        self.blo_img.setObjectName("blo_img")

        self.blo_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.blo_label.setGeometry(QtCore.QRect(200, 620, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.blo_label.setFont(font)
        self.blo_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.blo_label.setObjectName("blo_label")

        self.bef_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.bef_label.setGeometry(QtCore.QRect(370, 320, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.bef_label.setFont(font)
        self.bef_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bef_label.setObjectName("bef_label")

        self.you_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.you_img.setGeometry(QtCore.QRect(190, 240, 120, 158))
        self.you_img.setAutoFillBackground(True)
        self.you_img.setText("")
        self.you_img.setObjectName("you_img")

        self.obs_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.obs_img.setGeometry(QtCore.QRect(170, 460, 158, 120))
        self.obs_img.setAutoFillBackground(True)
        self.obs_img.setText("")
        self.obs_img.setObjectName("obs_img")

        self.hom_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.hom_img.setGeometry(QtCore.QRect(500, 460, 120, 158))
        self.hom_img.setAutoFillBackground(True)
        self.hom_img.setText("")
        self.hom_img.setObjectName("hom_img")

        self.bhi_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.bhi_img.setGeometry(QtCore.QRect(20, 340, 120, 158))
        self.bhi_img.setAutoFillBackground(True)
        self.bhi_img.setText("")
        self.bhi_img.setObjectName("bhi_img")

        self.hnf_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.hnf_img.setGeometry(QtCore.QRect(500, 250, 120, 158))
        self.hnf_img.setAutoFillBackground(True)
        self.hnf_img.setText("")
        self.hnf_img.setObjectName("hnf_img")

        self.abv_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.abv_img.setGeometry(QtCore.QRect(180, 30, 120, 158))
        self.abv_img.setAutoFillBackground(True)
        self.abv_img.setText("")
        self.abv_img.setObjectName("abv_img")

        self.hnf_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.hnf_label.setGeometry(QtCore.QRect(480, 230, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.hnf_label.setFont(font)
        self.hnf_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.hnf_label.setObjectName("hnf_label")

        self.unw_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.unw_label.setGeometry(QtCore.QRect(500, 650, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.unw_label.setFont(font)
        self.unw_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.unw_label.setObjectName("unw_label")

        self.bef_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.bef_img.setGeometry(QtCore.QRect(360, 340, 120, 158))
        self.bef_img.setAutoFillBackground(True)
        self.bef_img.setText("")
        self.bef_img.setObjectName("bef_img")

        self.obs_label = QtWidgets.QLabel(parent=UiCelticReading)
        self.obs_label.setGeometry(QtCore.QRect(200, 430, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.obs_label.setFont(font)
        self.obs_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_label.setObjectName("obs_label")

        self.unw_img = QtWidgets.QLabel(parent=UiCelticReading)
        self.unw_img.setGeometry(QtCore.QRect(500, 670, 120, 158))
        self.unw_img.setAutoFillBackground(True)
        self.unw_img.setText("")
        self.unw_img.setObjectName("unw_img")

        self.abv_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.abv_btn.setGeometry(QtCore.QRect(180, 190, 110, 22))
        self.abv_btn.setText("")
        self.abv_btn.setObjectName("abv_btn")

        self.abv_btn.setText('Draw Card')
        self.abv_btn.clicked.connect(self.draw_abv_card)

        self.ans_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.ans_btn.setGeometry(QtCore.QRect(500, 200, 110, 22))
        self.ans_btn.setText("")
        self.ans_btn.setObjectName("ans_btn")

        self.ans_btn.setText('Draw Card')
        self.ans_btn.clicked.connect(self.draw_ans_card)

        self.hnf_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.hnf_btn.setGeometry(QtCore.QRect(500, 410, 110, 22))
        self.hnf_btn.setText("")
        self.hnf_btn.setObjectName("hnf_btn")

        self.hnf_btn.setText('Draw Card')
        self.hnf_btn.clicked.connect(self.draw_hnf_card)

        self.you_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.you_btn.setGeometry(QtCore.QRect(190, 400, 110, 22))
        self.you_btn.setText("")
        self.you_btn.setObjectName("you_btn")

        self.you_btn.setText('Draw Card')
        self.you_btn.clicked.connect(self.draw_you_card)

        self.bhi_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.bhi_btn.setGeometry(QtCore.QRect(20, 510, 110, 22))
        self.bhi_btn.setText("")
        self.bhi_btn.setObjectName("bhi_btn")

        self.bhi_btn.setText('Draw Card')
        self.bhi_btn.clicked.connect(self.draw_bhi_card)

        self.bef_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.bef_btn.setGeometry(QtCore.QRect(360, 500, 110, 22))
        self.bef_btn.setText("")
        self.bef_btn.setObjectName("bef_btn")

        self.hom_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.hom_btn.setGeometry(QtCore.QRect(500, 620, 110, 22))
        self.hom_btn.setText("")
        self.hom_btn.setObjectName("hom_btn")

        self.blo_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.blo_btn.setGeometry(QtCore.QRect(190, 810, 110, 22))
        self.blo_btn.setText("")
        self.blo_btn.setObjectName("blo_btn")

        self.unw_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.unw_btn.setGeometry(QtCore.QRect(500, 830, 110, 22))
        self.unw_btn.setText("")
        self.unw_btn.setObjectName("unw_btn")

        self.obs_btn = QtWidgets.QPushButton(parent=UiCelticReading)
        self.obs_btn.setGeometry(QtCore.QRect(200, 590, 110, 22))
        self.obs_btn.setText("")
        self.obs_btn.setObjectName("obs_btn")

        self.retranslateUi(UiCelticReading)
        QtCore.QMetaObject.connectSlotsByName(UiCelticReading)

    def draw_you_card(self):
        you_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(you_card).replace(" ", "_"))
        self.you_image = QPixmap(pic_path).scaled(88, 158)
        self.you_img.setPixmap(self.you_image)
        self.you_btn.setText(str(you_card))

    def draw_bhi_card(self):
        bhi_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(bhi_card).replace(" ", "_"))
        self.bhi_image = QPixmap(pic_path).scaled(88, 158)
        self.bhi_img.setPixmap(self.bhi_image)
        self.bhi_btn.setText(str(bhi_card))

    def draw_ans_card(self):
        ans_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(ans_card).replace(" ", "_"))
        self.ans_image = QPixmap(pic_path).scaled(88, 158)
        self.ans_img.setPixmap(self.ans_image)
        self.ans_btn.setText(str(ans_card))

    def draw_hom_card(self):
        hom_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(hom_card).replace(" ", "_"))
        self.hom_image = QPixmap(pic_path).scaled(88, 158)
        self.hom_img.setPixmap(self.hom_image)
        self.hom_btn.setText(str(hom_card))

    def draw_abv_card(self):
        abv_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(abv_card).replace(" ", "_"))
        self.abv_image = QPixmap(pic_path).scaled(88, 158)
        self.abv_img.setPixmap(self.abv_image)
        self.abv_btn.setText(str(abv_card))

    def draw_blo_card(self):
        blo_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(blo_card).replace(" ", "_"))
        self.blo_image = QPixmap(pic_path).scaled(88, 158)
        self.blo_img.setPixmap(self.blo_image)
        self.blo_btn.setText(str(blo_card))

    def draw_bef_card(self):
        bef_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(bef_card).replace(" ", "_"))
        self.bef_image = QPixmap(pic_path).scaled(88, 158)
        self.bef_img.setPixmap(self.bef_image)
        self.bef_btn.setText(str(bef_card))

    def draw_hnf_card(self):
        hnf_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(hnf_card).replace(" ", "_"))
        self.hnf_image = QPixmap(pic_path).scaled(88, 158)
        self.hnf_img.setPixmap(self.hnf_image)
        self.hnf_btn.setText(str(hnf_card))

    def draw_unw_card(self):
        unw_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(unw_card).replace(" ", "_"))
        self.unw_image = QPixmap(pic_path).scaled(88, 158)
        self.unw_img.setPixmap(self.unw_image)
        self.unw_btn.setText(str(unw_card))

    def draw_obs_card(self):
        obs_card = deck.deal()
        pic_path = 'images/marseille/{}.png'.format(str(obs_card).replace(" ", "_"))
        self.obs_image = QPixmap(pic_path).scaled(88, 158)
        pixmap_rotate =self.obs_image.transformed(QTransform().rotate(90))
        self.obs_img.setPixmap(pixmap_rotate)
        self.obs_btn.setText(str(obs_card))

    def retranslateUi(self, UiCelticReading):
        _translate = QtCore.QCoreApplication.translate
        UiCelticReading.setWindowTitle(_translate("UiCelticReading", "Form"))
        self.bhi_label.setText(_translate("UiCelticReading", "Behind You"))
        self.you_label.setText(_translate("UiCelticReading", "You"))
        self.ans_label.setText(_translate("UiCelticReading", "Answer"))
        self.hom_label.setText(_translate("UiCelticReading", "Home"))
        self.abv_label.setText(_translate("UiCelticReading", "Above You"))
        self.blo_label.setText(_translate("UiCelticReading", "Below You"))
        self.bef_label.setText(_translate("UiCelticReading", "You Face"))
        self.hnf_label.setText(_translate("UiCelticReading", "Hopes and Fears"))
        self.unw_label.setText(_translate("UiCelticReading", "You Now"))
        self.obs_label.setText(_translate("UiCelticReading", "Obstacle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiCelticReading = QtWidgets.QWidget()
    ui = Ui_CelticReading()
    ui.setupUi(UiCelticReading)
    UiCelticReading.show()
    sys.exit(app.exec())
