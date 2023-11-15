from PyQt6 import QtCore, QtGui, QtWidgets
import create_deck
import create_spreads

deck = create_deck.Deck()
deck.shuffle()
simple_spread = create_spreads.SimpleThreeCard()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(735, 200)
        self.past_button = QtWidgets.QPushButton(parent=Form)
        self.past_button.setGeometry(QtCore.QRect(30, 105, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        self.past_button.setFont(font)
        self.past_button.setObjectName("past_button")

        self.past_button.clicked.connect(self.past_click)

        self.present_button = QtWidgets.QPushButton(parent=Form)
        self.present_button.setGeometry(QtCore.QRect(275, 105, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        self.present_button.setFont(font)
        self.present_button.setObjectName("present_button")

        self.present_button.clicked.connect(self.present_click)

        self.future_button = QtWidgets.QPushButton(parent=Form)
        self.future_button.setGeometry(QtCore.QRect(520, 105, 155, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        font.setBold(False)
        self.future_button.setFont(font)
        self.future_button.setObjectName("future_button")

        self.future_button.clicked.connect(self.future_click)

        self.past_label = QtWidgets.QLabel(parent=Form)
        self.past_label.setGeometry(QtCore.QRect(30, 70, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.past_label.setFont(font)
        self.past_label.setText("")
        self.past_label.setObjectName("past_label")

        self.present_label = QtWidgets.QLabel(parent=Form)
        self.present_label.setGeometry(QtCore.QRect(275, 70, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.present_label.setFont(font)
        self.present_label.setText("")
        self.present_label.setObjectName("present_label")

        self.future_label = QtWidgets.QLabel(parent=Form)
        self.future_label.setGeometry(QtCore.QRect(520, 70, 155, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.future_label.setFont(font)
        self.future_label.setText("")
        self.future_label.setObjectName("future_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def past_click(self):
        past_card = simple_spread.past_card()
        self.past_label.setText(str(past_card))
        self.past_button.setDisabled(True)

    def present_click(self):
        present_card = simple_spread.present_card()
        self.present_label.setText(str(present_card))
        self.present_button.setDisabled(True)

    def future_click(self):
        future_card = simple_spread.future_card()
        self.future_label.setText(str(future_card))
        self.future_button.setDisabled(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.past_button.setText(_translate("Form", "Past Card"))
        self.present_button.setText(_translate("Form", "Present Card"))
        self.future_button.setText(_translate("Form", "Future Card"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
