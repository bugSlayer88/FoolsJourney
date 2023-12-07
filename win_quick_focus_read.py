import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import QMessageBox

import create_deck

import meanings_dictionary

from tarot_spreads.quick_focus import QuickFocus
from win_quick_focus_meaning import Ui_FocusDecipher

image_dir = 'images/marseille'
main_meaning = meanings_dictionary.all_full_dict

deck = create_deck.Deck()
deck.shuffle()
cards = deck.list_cards()


class Ui_QuickFocusReading(object):
    def setupUi(self, UiQuickFocusReading):
        UiQuickFocusReading.setObjectName("UiQuickFocusReading")
        UiQuickFocusReading.resize(675, 865)

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)

        self.focus_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.focus_label.setGeometry(QtCore.QRect(450, 10, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_label.setFont(font)
        self.focus_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.focus_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.focus_label.setObjectName("focus_label")

        self.obs_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.obs_img.setGeometry(QtCore.QRect(180, 560, 315, 175))
        self.obs_img.setAutoFillBackground(True)
        self.obs_img.setText("")
        self.obs_img.setObjectName("obs_img")
        rotate_obs_img = pixmap.transformed(QTransform().rotate(90))
        self.obs_img.setPixmap(rotate_obs_img)

        self.decipher_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.decipher_btn.setGeometry(QtCore.QRect(160, 810, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.decipher_btn.clicked.connect(self.launch_decipher_window)

        self.focus_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.focus_img.setGeometry(QtCore.QRect(460, 50, 175, 315))
        self.focus_img.setAutoFillBackground(True)
        self.focus_img.setText("")
        self.focus_img.setObjectName("focus_img")
        self.focus_img.setPixmap(pixmap)

        self.letgo_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.letgo_label.setGeometry(QtCore.QRect(30, 10, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_label.setFont(font)
        self.letgo_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.letgo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.letgo_label.setObjectName("letgo_label")

        self.you_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.you_label.setGeometry(QtCore.QRect(240, 100, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_label.setFont(font)
        self.you_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.you_label.setObjectName("you_label")

        self.you_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.you_img.setGeometry(QtCore.QRect(250, 140, 175, 315))
        self.you_img.setAutoFillBackground(True)
        self.you_img.setText("")
        self.you_img.setObjectName("you_img")
        self.you_img.setPixmap(pixmap)

        self.letgo_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.letgo_img.setGeometry(QtCore.QRect(40, 50, 175, 315))
        self.letgo_img.setAutoFillBackground(True)
        self.letgo_img.setText("")
        self.letgo_img.setObjectName("letgo_img")
        self.letgo_img.setPixmap(pixmap)

        self.obs_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.obs_label.setGeometry(QtCore.QRect(240, 520, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_label.setFont(font)
        self.obs_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.obs_label.setObjectName("obs_label")

        self.letgo_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.letgo_btn.setGeometry(QtCore.QRect(40, 390, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_btn.setFont(font)
        self.letgo_btn.setObjectName("letgo_btn")

        self.letgo_btn.clicked.connect(self.draw_let_go_card)

        self.you_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.you_btn.setGeometry(QtCore.QRect(250, 480, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_btn.setFont(font)
        self.you_btn.setObjectName("you_btn")

        self.you_btn.clicked.connect(self.draw_you_card)

        self.focus_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.focus_btn.setGeometry(QtCore.QRect(460, 390, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_btn.setFont(font)
        self.focus_btn.setObjectName("focus_btn")

        self.focus_btn.clicked.connect(self.draw_focus_card)

        self.obs_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.obs_btn.setGeometry(QtCore.QRect(250, 760, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_btn.setFont(font)
        self.obs_btn.setObjectName("obs_btn")

        self.obs_btn.clicked.connect(self.draw_obs_card)

        self.retranslateUi(UiQuickFocusReading)
        QtCore.QMetaObject.connectSlotsByName(UiQuickFocusReading)

    def draw_you_card(self):
        you_card = QuickFocus().current_you_card
        pic_path = 'images/marseille/{}.png'.format(str(you_card).replace(" ", "_"))
        self.you_image = QPixmap(pic_path).scaled(175, 315)
        self.you_img.setPixmap(self.you_image)
        self.you_btn.setText(str(you_card))
        self.you_btn.setDisabled(True)

    def draw_obs_card(self):
        obs_card = QuickFocus().obstacle_card
        pic_path = 'images/marseille/{}.png'.format(str(obs_card).replace(" ", "_"))
        self.obs_image = QPixmap(pic_path).scaled(175, 315)
        rotate_obs_img = self.obs_image.transformed(QTransform().rotate(90))
        self.obs_img.setPixmap(rotate_obs_img)
        self.obs_btn.setText(str(obs_card))
        self.obs_btn.setDisabled(True)

    def draw_let_go_card(self):
        let_go_card = QuickFocus().let_go_card
        pic_path = 'images/marseille/{}.png'.format(str(let_go_card).replace(" ", "_"))
        self.let_go_image = QPixmap(pic_path).scaled(175, 315)
        self.letgo_img.setPixmap(self.let_go_image)
        self.letgo_btn.setText(str(let_go_card))
        self.letgo_btn.setDisabled(True)

    def draw_focus_card(self):
        focus_card = QuickFocus().focus_on_card
        pic_path = 'images/marseille/{}.png'.format(str(focus_card).replace(" ", "_"))
        self.focus_image = QPixmap(pic_path).scaled(175, 315)
        self.focus_img.setPixmap(self.focus_image)
        self.focus_btn.setText(str(focus_card))
        self.focus_btn.setDisabled(True)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_FocusDecipher()
        self.ui.setupUi(self.window)

        you_drawn = self.you_btn.text()
        obs_drawn = self.obs_btn.text()
        let_go_drawn = self.letgo_btn.text()
        focus_drawn = self.focus_btn.text()

        if you_drawn == "Draw Card" or obs_drawn == "Draw Card" or let_go_drawn == "Draw Card" or focus_drawn == "Draw Card":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No card selected, please select a card")
            msg.exec()
        else:
            self.ui.you_title.setText(str(you_drawn))
            self.ui.obs_title.setText(str(obs_drawn))
            self.ui.letgo_title.setText(str(let_go_drawn))
            self.ui.focus_title.setText(str(focus_drawn))

            get_you_meaning = main_meaning[str(you_drawn)]
            self.ui.you_img.setText(get_you_meaning)
            self.ui.you_img.setWordWrap(True)

            get_obs_meaning = main_meaning[str(obs_drawn)]
            self.ui.obs_img.setText(get_obs_meaning)
            self.ui.obs_img.setWordWrap(True)

            get_let_go_meaning = main_meaning[str(let_go_drawn)]
            self.ui.letgo_img.setText(get_let_go_meaning)
            self.ui.letgo_img.setWordWrap(True)

            get_focus_meaning = main_meaning[str(focus_drawn)]
            self.ui.focus_img.setText(get_focus_meaning)
            self.ui.focus_img.setWordWrap(True)

            self.window.show()

    def retranslateUi(self, UiQuickFocusReading):
        _translate = QtCore.QCoreApplication.translate
        UiQuickFocusReading.setWindowTitle(_translate("UiQuickFocusReading", "Focus Reading"))
        self.focus_label.setText(_translate("UiQuickFocusReading", "Focus On"))
        self.decipher_btn.setText(_translate("UiQuickFocusReading", "Show Explanation"))
        self.letgo_label.setText(_translate("UiQuickFocusReading", "Let Go Of"))
        self.you_label.setText(_translate("UiQuickFocusReading", "Where You Are Now"))
        self.obs_label.setText(_translate("UiQuickFocusReading", "Your Obstacle"))
        self.letgo_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))
        self.you_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))
        self.focus_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))
        self.obs_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    UiQuickFocusReading = QtWidgets.QWidget()
    ui = Ui_QuickFocusReading()
    ui.setupUi(UiQuickFocusReading)
    UiQuickFocusReading.show()
    sys.exit(app.exec())
