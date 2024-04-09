from PyQt6 import QtCore, QtGui, QtWidgets

import psycopg2 as pg2

import create_deck

deck = create_deck.Deck()
cards = deck.list_cards()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(647, 416)
        self.basic_rad = QtWidgets.QRadioButton(parent=Form)
        self.basic_rad.setGeometry(QtCore.QRect(14, 70, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(12)
        self.basic_rad.setFont(font)
        self.basic_rad.setObjectName("basic_rad")
        self.neg_rad = QtWidgets.QRadioButton(parent=Form)
        self.neg_rad.setGeometry(QtCore.QRect(140, 70, 144, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(12)
        self.neg_rad.setFont(font)
        self.neg_rad.setObjectName("neg_rad")
        self.meaning_lbl = QtWidgets.QLabel(parent=Form)
        self.meaning_lbl.setGeometry(QtCore.QRect(9, 156, 616, 251))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(12)
        self.meaning_lbl.setFont(font)
        self.meaning_lbl.setText("")
        self.meaning_lbl.setObjectName("meaning_lbl")

        self.get_mean_lbl = QtWidgets.QPushButton(parent=Form)
        self.get_mean_lbl.setGeometry(QtCore.QRect(130, 100, 381, 27))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.get_mean_lbl.setFont(font)
        self.get_mean_lbl.setObjectName("get_mean_lbl")

        self.get_mean_lbl.clicked.connect(self.search_card)

        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 621, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.card_title_lbl = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        font.setBold(True)
        self.card_title_lbl.setFont(font)
        self.card_title_lbl.setObjectName("card_title_lbl")
        self.horizontalLayout.addWidget(self.card_title_lbl)

        self.card_cmb = QtWidgets.QComboBox(parent=self.widget)
        self.card_cmb.setObjectName("card_cmb")
        self.horizontalLayout.addWidget(self.card_cmb)

        self.card_cmb.addItems(cards)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def search_card(self):
        try:
            mydb = pg2.connect(database="Tarot", user="postgres", password="password")

            cursor = mydb.cursor()

            query = "SELECT card FROM card_meaning"

            cursor.execute(query)

            row = cursor.fetchone()

            if row == None:
                self.meaning_lbl.setText("no card found")
            else:
                self.meaning_lbl.setText("card found")

        except pg2.Error:
            self.meaning_lbl.setText("Error")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.basic_rad.setText(_translate("Form", "Basic Meaning"))
        self.neg_rad.setText(_translate("Form", "Negative Meaning"))
        self.get_mean_lbl.setText(_translate("Form", "Get Meaning"))
        self.card_title_lbl.setText(_translate("Form", "Lookup Card:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
