# Form implementation generated from reading ui file 'show_one_card_001.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(190, 342)
        self.card_label = QtWidgets.QLabel(parent=Form)
        self.card_label.setGeometry(QtCore.QRect(20, 20, 135, 255))
        self.card_label.setText("")
        self.card_label.setObjectName("card_label")
        self.card_combo = QtWidgets.QComboBox(parent=Form)
        self.card_combo.setGeometry(QtCore.QRect(20, 290, 135, 22))
        self.card_combo.setObjectName("card_combo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
