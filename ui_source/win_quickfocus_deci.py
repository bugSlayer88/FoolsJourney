# Form implementation generated from reading ui file '.\win_quickfocus_deci.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UiQuickFocusDecipher(object):
    def setupUi(self, UiQuickFocusDecipher):
        UiQuickFocusDecipher.setObjectName("UiQuickFocusDecipher")
        UiQuickFocusDecipher.resize(675, 865)
        self.focus_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.focus_label.setGeometry(QtCore.QRect(450, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_label.setFont(font)
        self.focus_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.focus_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.focus_label.setObjectName("focus_label")
        self.you_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.you_img.setGeometry(QtCore.QRect(250, 150, 175, 315))
        self.you_img.setAutoFillBackground(True)
        self.you_img.setText("")
        self.you_img.setObjectName("you_img")
        self.you_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.you_label.setGeometry(QtCore.QRect(240, 110, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_label.setFont(font)
        self.you_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.you_label.setObjectName("you_label")
        self.you_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.you_combo.setGeometry(QtCore.QRect(250, 490, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_combo.setFont(font)
        self.you_combo.setObjectName("you_combo")
        self.focus_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.focus_combo.setGeometry(QtCore.QRect(460, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_combo.setFont(font)
        self.focus_combo.setObjectName("focus_combo")
        self.focus_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.focus_img.setGeometry(QtCore.QRect(460, 60, 175, 315))
        self.focus_img.setAutoFillBackground(True)
        self.focus_img.setText("")
        self.focus_img.setObjectName("focus_img")
        self.letgo_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.letgo_label.setGeometry(QtCore.QRect(30, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_label.setFont(font)
        self.letgo_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.letgo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.letgo_label.setObjectName("letgo_label")
        self.decipher_btn = QtWidgets.QPushButton(parent=UiQuickFocusDecipher)
        self.decipher_btn.setGeometry(QtCore.QRect(160, 820, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")
        self.letgo_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.letgo_img.setGeometry(QtCore.QRect(40, 60, 175, 315))
        self.letgo_img.setAutoFillBackground(True)
        self.letgo_img.setText("")
        self.letgo_img.setObjectName("letgo_img")
        self.letgo_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.letgo_combo.setGeometry(QtCore.QRect(40, 400, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_combo.setFont(font)
        self.letgo_combo.setObjectName("letgo_combo")
        self.obs_combo = QtWidgets.QComboBox(parent=UiQuickFocusDecipher)
        self.obs_combo.setGeometry(QtCore.QRect(250, 770, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_combo.setFont(font)
        self.obs_combo.setObjectName("obs_combo")
        self.obs_label = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.obs_label.setGeometry(QtCore.QRect(240, 530, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_label.setFont(font)
        self.obs_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.obs_label.setObjectName("obs_label")
        self.obs_img = QtWidgets.QLabel(parent=UiQuickFocusDecipher)
        self.obs_img.setGeometry(QtCore.QRect(180, 570, 315, 175))
        self.obs_img.setAutoFillBackground(True)
        self.obs_img.setText("")
        self.obs_img.setObjectName("obs_img")

        self.retranslateUi(UiQuickFocusDecipher)
        QtCore.QMetaObject.connectSlotsByName(UiQuickFocusDecipher)

    def retranslateUi(self, UiQuickFocusDecipher):
        _translate = QtCore.QCoreApplication.translate
        UiQuickFocusDecipher.setWindowTitle(_translate("UiQuickFocusDecipher", "Form"))
        self.focus_label.setText(_translate("UiQuickFocusDecipher", "Focus On"))
        self.you_label.setText(_translate("UiQuickFocusDecipher", "Where You Are Now"))
        self.letgo_label.setText(_translate("UiQuickFocusDecipher", "Let Go Of"))
        self.decipher_btn.setText(_translate("UiQuickFocusDecipher", "Show Explanation"))
        self.obs_label.setText(_translate("UiQuickFocusDecipher", "Your Obstacle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiQuickFocusDecipher = QtWidgets.QWidget()
    ui = Ui_UiQuickFocusDecipher()
    ui.setupUi(UiQuickFocusDecipher)
    UiQuickFocusDecipher.show()
    sys.exit(app.exec())