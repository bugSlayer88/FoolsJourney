from PyQt6 import QtCore, QtGui, QtWidgets
import create_deck
import create_spreads
import meanings_dictionary

deck = create_deck.Deck()
deck.shuffle()
simple_spread = create_spreads.SimpleThreeCardSpread()
keywords_major = meanings_dictionary.major_key_dict
keywords_minor = meanings_dictionary.minor_key_dict


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(735, 235)
        self.past_button = QtWidgets.QPushButton(parent=Form)
        self.past_button.setGeometry(QtCore.QRect(30, 65, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        self.past_button.setFont(font)
        self.past_button.setObjectName("past_button")

        self.past_button.clicked.connect(self.past_click)

        self.present_button = QtWidgets.QPushButton(parent=Form)
        self.present_button.setGeometry(QtCore.QRect(275, 65, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        self.present_button.setFont(font)
        self.present_button.setObjectName("present_button")

        self.present_button.clicked.connect(self.present_click)

        self.future_button = QtWidgets.QPushButton(parent=Form)
        self.future_button.setGeometry(QtCore.QRect(520, 65, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.future_button.setFont(font)
        self.future_button.setObjectName("future_button")

        self.future_button.clicked.connect(self.future_click)

        self.past_label = QtWidgets.QLabel(parent=Form)
        self.past_label.setGeometry(QtCore.QRect(30, 30, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.past_label.setFont(font)
        self.past_label.setText("")
        self.past_label.setObjectName("past_label")

        self.present_label = QtWidgets.QLabel(parent=Form)
        self.present_label.setGeometry(QtCore.QRect(275, 30, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.present_label.setFont(font)
        self.present_label.setText("")
        self.present_label.setObjectName("present_label")

        self.future_label = QtWidgets.QLabel(parent=Form)
        self.future_label.setGeometry(QtCore.QRect(520, 30, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.future_label.setFont(font)
        self.future_label.setText("")
        self.future_label.setObjectName("future_label")

        self.future_key_btn = QtWidgets.QPushButton(parent=Form)
        self.future_key_btn.setGeometry(QtCore.QRect(520, 180, 175, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.future_key_btn.setFont(font)
        self.future_key_btn.setObjectName("future_key_btn")

        self.present_key_btn = QtWidgets.QPushButton(parent=Form)
        self.present_key_btn.setGeometry(QtCore.QRect(275, 180, 175, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.present_key_btn.setFont(font)
        self.present_key_btn.setObjectName("present_key_btn")

        self.past_key_btn = QtWidgets.QPushButton(parent=Form)
        self.past_key_btn.setGeometry(QtCore.QRect(30, 180, 175, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.past_key_btn.setFont(font)
        self.past_key_btn.setObjectName("past_key_btn")

        self.past_key_btn.clicked.connect(self.past_key_click)

        self.past_key = QtWidgets.QLabel(parent=Form)
        self.past_key.setGeometry(QtCore.QRect(30, 110, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.past_key.setFont(font)
        self.past_key.setText("")
        self.past_key.setObjectName("past_key")

        self.present_key = QtWidgets.QLabel(parent=Form)
        self.present_key.setGeometry(QtCore.QRect(275, 110, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.present_key.setFont(font)
        self.present_key.setText("")
        self.present_key.setObjectName("present_key")

        self.future_key = QtWidgets.QLabel(parent=Form)
        self.future_key.setGeometry(QtCore.QRect(520, 110, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.future_key.setFont(font)
        self.future_key.setText("")
        self.future_key.setObjectName("future_key")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def past_click(self):
        past_card = simple_spread.past_card()
        self.past_label.setText(str(past_card))
        self.past_button.setDisabled(True)
        return past_card

    def present_click(self):
        present_card = simple_spread.present_card()
        self.present_label.setText(str(present_card))
        self.present_button.setDisabled(True)

    def future_click(self):
        future_card = simple_spread.future_card()
        self.future_label.setText(str(future_card))
        self.future_button.setDisabled(True)

    def past_key_click(self):
        past_card = self.past_click()
        words = past_card.keyword
        self.past_key.setText(str(words))
        self.past_key_btn.setDisabled(True)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.past_button.setText(_translate("Form", "Past Card"))
        self.present_button.setText(_translate("Form", "Present Card"))
        self.future_button.setText(_translate("Form", "Future Card"))
        self.future_key_btn.setText(_translate("Form", "Future Key Words"))
        self.present_key_btn.setText(_translate("Form", "Present Key Words"))
        self.past_key_btn.setText(_translate("Form", "Past Key Words"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
