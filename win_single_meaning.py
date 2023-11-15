from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Decipher(object):
    def setupUi(self, Decipher):
        Decipher.setObjectName("Decipher")
        Decipher.resize(465, 297)
        self.card_meaning_label = QtWidgets.QLabel(parent=Decipher)
        self.card_meaning_label.setGeometry(QtCore.QRect(50, 100, 371, 161))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.card_meaning_label.setFont(font)
        self.card_meaning_label.setText("")
        self.card_meaning_label.setObjectName("card_meaning_label")
        self.card_label = QtWidgets.QLabel(parent=Decipher)
        self.card_label.setGeometry(QtCore.QRect(50, 20, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(16)
        font.setBold(True)
        self.card_label.setFont(font)
        self.card_label.setText("")
        self.card_label.setObjectName("card_label")

        self.retranslateUi(Decipher)
        QtCore.QMetaObject.connectSlotsByName(Decipher)

    def retranslateUi(self, Decipher):
        _translate = QtCore.QCoreApplication.translate
        Decipher.setWindowTitle(_translate("Decipher", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Decipher = QtWidgets.QWidget()
    ui = Ui_Decipher()
    ui.setupUi(Decipher)
    Decipher.show()
    sys.exit(app.exec())
