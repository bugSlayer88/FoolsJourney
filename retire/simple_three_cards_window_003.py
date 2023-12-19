from PyQt6 import QtCore, QtGui, QtWidgets
import create_deck
import create_spreads
from tarot_spreads.simple_three import SimpleThreeCard
import meanings_dictionary


deck = create_deck.Deck()
deck.shuffle()
# simple_spread = create_spreads.SimpleThreeCard()
simple_spread = SimpleThreeCard()
keywords_major = meanings_dictionary.major_key_dict
keywords_minor = meanings_dictionary.minor_key_dict

# creating these now so that the card is drawn only once
# should I get this from the ui or should i figure out how to only run the function once?
past_card = simple_spread.past()
present_card = simple_spread.present()
future_card = simple_spread.future()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(692, 600)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 621, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.past_label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.past_label.setFont(font)
        self.past_label.setText("")
        self.past_label.setObjectName("past_label")
        self.gridLayout.addWidget(self.past_label, 0, 0, 1, 1)

        self.present_label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.present_label.setFont(font)
        self.present_label.setText("")
        self.present_label.setObjectName("present_label")
        self.gridLayout.addWidget(self.present_label, 0, 1, 1, 1)

        self.future_label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.future_label.setFont(font)
        self.future_label.setText("")
        self.future_label.setObjectName("future_label")
        self.gridLayout.addWidget(self.future_label, 0, 2, 1, 1)

        self.past_button = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        self.past_button.setFont(font)
        self.past_button.setObjectName("past_button")
        self.gridLayout.addWidget(self.past_button, 1, 0, 1, 1)

        self.past_button.clicked.connect(self.past_click)

        self.present_button = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        self.present_button.setFont(font)
        self.present_button.setObjectName("present_button")
        self.gridLayout.addWidget(self.present_button, 1, 1, 1, 1)

        self.present_button.clicked.connect(self.present_click)

        self.future_button = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.future_button.setFont(font)
        self.future_button.setObjectName("future_button")
        self.gridLayout.addWidget(self.future_button, 1, 2, 1, 1)

        self.future_button.clicked.connect(self.future_click)

        self.widget1 = QtWidgets.QWidget(parent=Form)
        self.widget1.setGeometry(QtCore.QRect(30, 130, 621, 131))
        self.widget1.setObjectName("widget1")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.past_key_label = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.past_key_label.setFont(font)
        self.past_key_label.setText("")
        self.past_key_label.setObjectName("past_key_label")
        self.gridLayout_2.addWidget(self.past_key_label, 0, 0, 1, 1)

        self.present_key_label = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.present_key_label.setFont(font)
        self.present_key_label.setText("")
        self.present_key_label.setObjectName("present_key_label")
        self.gridLayout_2.addWidget(self.present_key_label, 0, 1, 1, 1)
        self.future_key_label = QtWidgets.QLabel(parent=self.widget1)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.future_key_label.setFont(font)
        self.future_key_label.setText("")
        self.future_key_label.setObjectName("future_key_label")
        self.gridLayout_2.addWidget(self.future_key_label, 0, 2, 1, 1)

        self.past_key_btn = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.past_key_btn.setFont(font)
        self.past_key_btn.setObjectName("past_key_btn")
        self.gridLayout_2.addWidget(self.past_key_btn, 1, 0, 1, 1)

        self.past_key_btn.clicked.connect(self.past_key_click)

        self.present_key_btn = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.present_key_btn.setFont(font)
        self.present_key_btn.setObjectName("present_key_btn")
        self.gridLayout_2.addWidget(self.present_key_btn, 1, 1, 1, 1)

        self.present_key_btn.clicked.connect(self.present_key_click)

        self.future_key_btn = QtWidgets.QPushButton(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.future_key_btn.setFont(font)
        self.future_key_btn.setObjectName("future_key_btn")
        self.gridLayout_2.addWidget(self.future_key_btn, 1, 2, 1, 1)

        self.future_key_btn.clicked.connect(self.future_key_click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def past_click(self):
        self.past_label.setText(str(past_card))
        self.past_button.setDisabled(True)

    def present_click(self):
        self.present_label.setText(str(present_card))
        self.present_button.setDisabled(True)

    def future_click(self):
        self.future_label.setText(str(future_card))
        self.future_button.setDisabled(True)

    def past_key_click(self):
        words = past_card.keyword
        self.past_key_label.setText(str(words))
        self.past_key_btn.setDisabled(True)

    def present_key_click(self):
        words = present_card.keyword
        self.present_key_label.setText(str(words))
        self.present_key_btn.setDisabled(True)

    def future_key_click(self):
        words = future_card.keyword
        self.future_key_label.setText(str(words))
        self.future_key_btn.setDisabled(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.past_button.setText(_translate("Form", "Past Card"))
        self.present_button.setText(_translate("Form", "Present Card"))
        self.future_button.setText(_translate("Form", "Future Card"))
        self.past_key_btn.setText(_translate("Form", "Past Key Words"))
        self.present_key_btn.setText(_translate("Form", "Present Key Words"))
        self.future_key_btn.setText(_translate("Form", "Future Key Words"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
