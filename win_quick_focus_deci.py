import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import QMessageBox

import create_deck

import meanings_dictionary
from win_quick_focus_meaning import Ui_FocusDecipher

main_meaning = meanings_dictionary.all_full_dict

image_dir = 'images/marseille'

deck = create_deck.Deck()
cards = deck.list_cards()

class Ui_QuickFocusDecipher(object):
    def setupUi(self, UiQuickFocusDecipher):
        UiQuickFocusDecipher.setObjectName("UiQuickFocusDecipher")
        UiQuickFocusDecipher.resize(675, 865)

        pixmap = QPixmap('images/marseille/back.png').scaled(175, 315)

        self.focus_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.focus_label.setGeometry(QtCore.QRect(450, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_label.setFont(font)
        self.focus_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.focus_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.focus_label.setObjectName("focus_label")

        self.you_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.you_img.setGeometry(QtCore.QRect(250, 150, 175, 315))
        self.you_img.setAutoFillBackground(True)
        self.you_img.setText("")
        self.you_img.setPixmap(pixmap)
        self.you_img.setObjectName("you_img")

        self.you_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.you_label.setGeometry(QtCore.QRect(240, 110, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_label.setFont(font)
        self.you_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.you_label.setObjectName("you_label")

        self.you_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.you_combo.setGeometry(QtCore.QRect(250, 490, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_combo.setFont(font)
        self.you_combo.setObjectName("you_combo")
        self.you_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.you_combo.addItem('Select Card')
        self.you_combo.addItems(cards)

        self.you_combo.currentTextChanged.connect(self.you_combo_update)

        self.focus_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.focus_combo.setGeometry(QtCore.QRect(460, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_combo.setFont(font)
        self.focus_combo.setObjectName("focus_combo")
        self.focus_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.focus_combo.addItem('Select Card')
        self.focus_combo.addItems(cards)

        self.focus_combo.currentTextChanged.connect(self.focus_combo_update)

        self.focus_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.focus_img.setGeometry(QtCore.QRect(460, 60, 175, 315))
        self.focus_img.setAutoFillBackground(True)
        self.focus_img.setText("")
        self.focus_img.setPixmap(pixmap)
        self.focus_img.setObjectName("focus_img")

        self.letgo_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.letgo_label.setGeometry(QtCore.QRect(30, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_label.setFont(font)
        self.letgo_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.letgo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.letgo_label.setObjectName("letgo_label")

        self.decipher_btn = QtWidgets.QPushButton(parent=UiQuickFocusDecipher)
        self.decipher_btn.setGeometry(QtCore.QRect(160, 820, 361, 30))
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

        self.letgo_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.letgo_img.setGeometry(QtCore.QRect(40, 60, 175, 315))
        self.letgo_img.setAutoFillBackground(True)
        self.letgo_img.setText("")
        self.letgo_img.setPixmap(pixmap)
        self.letgo_img.setObjectName("letgo_img")

        self.letgo_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.letgo_combo.setGeometry(QtCore.QRect(40, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_combo.setFont(font)
        self.letgo_combo.setObjectName("letgo_combo")
        self.letgo_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.letgo_combo.addItem('Select Card')
        self.letgo_combo.addItems(cards)

        self.letgo_combo.currentTextChanged.connect(self.letgo_combo_update)

        self.obs_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.obs_combo.setGeometry(QtCore.QRect(250, 770, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_combo.setFont(font)
        self.obs_combo.setObjectName("obs_combo")
        self.obs_combo.setStyleSheet('''
        QComboBox {
        border:2px solid #aaa;
        border-radius: 5px;
        }
        ''')

        self.obs_combo.addItem('Select Card')
        self.obs_combo.addItems(cards)

        self.obs_combo.currentTextChanged.connect(self.obstacle_combo_update)

        self.obs_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.obs_label.setGeometry(QtCore.QRect(240, 530, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_label.setFont(font)
        self.obs_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.obs_label.setObjectName("obs_label")

        self.obs_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.obs_img.setGeometry(QtCore.QRect(180, 570, 315, 175))
        self.obs_img.setAutoFillBackground(True)
        self.obs_img.setText("")
        angle = 90
        self.obs_img_card = QPixmap(pixmap)
        self.obs_back_rotated = self.obs_img_card.transformed(QTransform().rotate(angle))
        self.obs_img.setPixmap(self.obs_back_rotated)
        self.obs_img.setObjectName("obs_img")

        self.retranslateUi(UiQuickFocusDecipher)
        QtCore.QMetaObject.connectSlotsByName(UiQuickFocusDecipher)

    def you_combo_update(self):
        you_selected = self.you_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(you_selected.replace(" ", "_"))
        self.you_card_img = QPixmap(pic_path).scaled(175,315)
        self.you_img.setPixmap(self.you_card_img)

    def obstacle_combo_update(self):
        obs_selected = self.obs_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(obs_selected.replace(" ", "_"))
        angle = 90
        self.obs_card_img = QPixmap(pic_path).scaled(175,315)
        pixmap_rotated = self.obs_card_img.transformed(QTransform().rotate(angle))
        self.obs_img.setPixmap(pixmap_rotated)

    def letgo_combo_update(self):
        letgo_selected = self.letgo_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(letgo_selected.replace(" ", "_"))
        self.letgo_card_img = QPixmap(pic_path).scaled(175,315)
        self.letgo_img.setPixmap(self.letgo_card_img)

    def focus_combo_update(self):
        focus_selected = self.focus_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(focus_selected.replace(" ", "_"))
        self.focus_card_img = QPixmap(pic_path).scaled(175,315)
        self.focus_img.setPixmap(self.focus_card_img)

    def launch_decipher_window(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_FocusDecipher()
        self.ui.setupUi(self.window)

        you_card_selected = self.you_combo.currentText()
        obs_card_selected = self.obs_combo.currentText()
        letgo_card_selected = self.letgo_combo.currentText()
        focus_card_selected = self.focus_combo.currentText()

        if you_card_selected == "Select Card" or obs_card_selected == "Select Card" or letgo_card_selected == ("Select "
                                                                                                               "Card") or focus_card_selected == "Select Card":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Not enough cards selected, please select more cards")
            msg.exec()
        else:
            self.ui.you_title.setText(you_card_selected)
            self.ui.obs_title.setText(obs_card_selected)
            self.ui.letgo_title.setText(letgo_card_selected)
            self.ui.focus_title.setText(focus_card_selected)

            get_you_meaning = main_meaning[str(you_card_selected)]
            self.ui.you_img.setText(get_you_meaning)
            self.ui.you_img.setWordWrap(True)
            get_obs_meaning = main_meaning[str(obs_card_selected)]
            self.ui.obs_img.setText(get_obs_meaning)
            self.ui.obs_img.setWordWrap(True)
            get_letgo_meaning = main_meaning[str(letgo_card_selected)]
            self.ui.letgo_img.setText(get_letgo_meaning)
            self.ui.letgo_img.setWordWrap(True)
            get_focus_meaning = main_meaning[str(focus_card_selected)]
            self.ui.focus_img.setText(get_focus_meaning)
            self.ui.focus_img.setWordWrap(True)

            self.window.show()

    def retranslateUi(self, UiQuickFocusDecipher):
        _translate = QtCore.QCoreApplication.translate
        UiQuickFocusDecipher.setWindowTitle(_translate("UiQuickFocusDecipher", "Quick Focus Decipher"))
        self.focus_label.setText(_translate("UiQuickFocusDecipher", "Focus On"))
        self.you_label.setText(_translate("UiQuickFocusDecipher", "Where You Are Now"))
        self.letgo_label.setText(_translate("UiQuickFocusDecipher", "Let Go Of"))
        self.decipher_btn.setText(_translate("UiQuickFocusDecipher", "Show Explanation"))
        self.obs_label.setText(_translate("UiQuickFocusDecipher", "Your Obstacle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiQuickFocusDecipher = QtWidgets.QWidget()
    ui = Ui_QuickFocusDecipher()
    ui.setupUi(UiQuickFocusDecipher)
    UiQuickFocusDecipher.show()
    sys.exit(app.exec())
