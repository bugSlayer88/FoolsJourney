# Form implementation generated from reading ui file '.\win_three_meaning.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ThreeExplainPopup(object):
    def setupUi(self, ThreeDecipher):
        ThreeDecipher.setObjectName("ThreeDecipher")
        ThreeDecipher.resize(696, 465)

        self.pas_label = QtWidgets.QLabel(parent=ThreeDecipher)
        self.pas_label.setGeometry(QtCore.QRect(120, 40, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.pas_label.setFont(font)
        self.pas_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pas_label.setObjectName("pas_label")

        self.pre_label = QtWidgets.QLabel(parent=ThreeDecipher)
        self.pre_label.setGeometry(QtCore.QRect(310, 40, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.pre_label.setFont(font)
        self.pre_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pre_label.setObjectName("pre_label")

        self.fut_label = QtWidgets.QLabel(parent=ThreeDecipher)
        self.fut_label.setGeometry(QtCore.QRect(520, 40, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(18)
        self.fut_label.setFont(font)
        self.fut_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.fut_label.setObjectName("fut_label")

        self.pas_desc = QtWidgets.QLabel(parent=ThreeDecipher)
        self.pas_desc.setGeometry(QtCore.QRect(50, 150, 175, 300))
        self.pas_desc.setAutoFillBackground(True)
        self.pas_desc.setText("")
        self.pas_desc.setObjectName("pas_desc")

        self.pre_desc = QtWidgets.QLabel(parent=ThreeDecipher)
        self.pre_desc.setGeometry(QtCore.QRect(260, 150, 175, 300))
        self.pre_desc.setAutoFillBackground(True)
        self.pre_desc.setText("")
        self.pre_desc.setObjectName("pre_desc")

        self.fut_desc = QtWidgets.QLabel(parent=ThreeDecipher)
        self.fut_desc.setGeometry(QtCore.QRect(470, 150, 175, 300))
        self.fut_desc.setAutoFillBackground(True)
        self.fut_desc.setText("")
        self.fut_desc.setObjectName("fut_desc")

        self.fut_card_title = QtWidgets.QLabel(parent=ThreeDecipher)
        self.fut_card_title.setGeometry(QtCore.QRect(470, 80, 175, 44))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.fut_card_title.setFont(font)
        self.fut_card_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.fut_card_title.setText("")
        self.fut_card_title.setObjectName("fut_card_title")

        self.pas_card_title = QtWidgets.QLabel(parent=ThreeDecipher)
        self.pas_card_title.setGeometry(QtCore.QRect(50, 80, 175, 44))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.pas_card_title.setFont(font)
        self.pas_card_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pas_card_title.setText("")
        self.pas_card_title.setObjectName("pas_card_title")

        self.pre_card_title = QtWidgets.QLabel(parent=ThreeDecipher)
        self.pre_card_title.setGeometry(QtCore.QRect(260, 80, 175, 44))
        font = QtGui.QFont()
        font.setFamily("Adobe Hebrew")
        font.setPointSize(14)
        self.pre_card_title.setFont(font)
        self.pre_card_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pre_card_title.setText("")
        self.pre_card_title.setObjectName("pre_card_title")

        self.retranslateUi(ThreeDecipher)
        QtCore.QMetaObject.connectSlotsByName(ThreeDecipher)

    def retranslateUi(self, ThreeDecipher):
        _translate = QtCore.QCoreApplication.translate
        ThreeDecipher.setWindowTitle(_translate("ThreeDecipher", "Form"))
        self.pas_label.setText(_translate("ThreeDecipher", "Past"))
        self.pre_label.setText(_translate("ThreeDecipher", "Present"))
        self.fut_label.setText(_translate("ThreeDecipher", "Future"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThreeDecipher = QtWidgets.QWidget()
    ui = Ui_ThreeExplainPopup()
    ui.setupUi(ThreeDecipher)
    ThreeDecipher.show()
    sys.exit(app.exec())
