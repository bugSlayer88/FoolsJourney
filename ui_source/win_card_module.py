# Form implementation generated from reading ui file '.\win_card_module.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CardModule(object):
    def setupUi(self, CardModule):
        CardModule.setObjectName("CardModule")
        CardModule.resize(254, 469)
        self.card_combo = QtWidgets.QComboBox(parent=CardModule)
        self.card_combo.setGeometry(QtCore.QRect(20, 430, 211, 22))
        self.card_combo.setObjectName("card_combo")
        self.card_img = QtWidgets.QLabel(parent=CardModule)
        self.card_img.setGeometry(QtCore.QRect(40, 60, 181, 341))
        self.card_img.setText("")
        self.card_img.setObjectName("card_img")
        self.card_title = QtWidgets.QLabel(parent=CardModule)
        self.card_title.setGeometry(QtCore.QRect(40, 10, 171, 21))
        self.card_title.setText("")
        self.card_title.setObjectName("card_title")

        self.retranslateUi(CardModule)
        QtCore.QMetaObject.connectSlotsByName(CardModule)

    def retranslateUi(self, CardModule):
        _translate = QtCore.QCoreApplication.translate
        CardModule.setWindowTitle(_translate("CardModule", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardModule = QtWidgets.QWidget()
    ui = Ui_CardModule()
    ui.setupUi(CardModule)
    CardModule.show()
    sys.exit(app.exec())
