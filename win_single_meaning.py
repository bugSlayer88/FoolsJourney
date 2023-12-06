
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Decipher(object):
    def setupUi(self, Decipher):
        Decipher.setObjectName("Decipher")
        Decipher.resize(262, 360)
        self.card_meaning_label = QtWidgets.QLabel(parent=Decipher)
        self.card_meaning_label.setGeometry(QtCore.QRect(40, 70, 175, 260))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.card_meaning_label.setFont(font)
        self.card_meaning_label.setText("")
        self.card_meaning_label.setObjectName("card_meaning_label")
        self.card_label = QtWidgets.QLabel(parent=Decipher)
        self.card_label.setGeometry(QtCore.QRect(30, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_label.setFont(font)
        self.card_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.card_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.card_label.setText("")
        self.card_label.setObjectName("card_label")

        self.retranslateUi(Decipher)
        QtCore.QMetaObject.connectSlotsByName(Decipher)

    def retranslateUi(self, Decipher):
        _translate = QtCore.QCoreApplication.translate
        Decipher.setWindowTitle(_translate("Decipher", "Single Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Decipher = QtWidgets.QWidget()
    ui = Ui_Decipher()
    ui.setupUi(Decipher)
    Decipher.show()
    sys.exit(app.exec())
