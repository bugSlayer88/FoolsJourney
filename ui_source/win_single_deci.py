# Form implementation generated from reading ui file '.\win_single_deci_02.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SingleDecipher(object):
    def setupUi(self, SingleDecipher):
        SingleDecipher.setObjectName("SingleDecipher")
        SingleDecipher.resize(340, 485)
        self.card_img = QtWidgets.QLabel(parent=SingleDecipher)
        self.card_img.setGeometry(QtCore.QRect(80, 30, 175, 315))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.card_img.setFont(font)
        self.card_img.setText("")
        self.card_img.setObjectName("card_img")
        self.single_combo = QtWidgets.QComboBox(parent=SingleDecipher)
        self.single_combo.setGeometry(QtCore.QRect(30, 380, 280, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.single_combo.setFont(font)
        self.single_combo.setObjectName("single_combo")
        self.decipher_btn = QtWidgets.QPushButton(parent=SingleDecipher)
        self.decipher_btn.setGeometry(QtCore.QRect(70, 430, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.retranslateUi(SingleDecipher)
        QtCore.QMetaObject.connectSlotsByName(SingleDecipher)

    def retranslateUi(self, SingleDecipher):
        _translate = QtCore.QCoreApplication.translate
        SingleDecipher.setWindowTitle(_translate("SingleDecipher", "Form"))
        self.decipher_btn.setText(_translate("SingleDecipher", "Show Explanation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingleDecipher = QtWidgets.QWidget()
    ui = Ui_SingleDecipher()
    ui.setupUi(SingleDecipher)
    SingleDecipher.show()
    sys.exit(app.exec())
