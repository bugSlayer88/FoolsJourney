# Form implementation generated from reading ui file '.\win_quickfocus_meaning.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FocusDecipher(object):
    def setupUi(self, FocusDecipher):
        FocusDecipher.setObjectName("FocusDecipher")
        FocusDecipher.resize(677, 744)
        self.focus_label = QtWidgets.QLabel(parent=FocusDecipher)
        self.focus_label.setGeometry(QtCore.QRect(450, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_label.setFont(font)
        self.focus_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.focus_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.focus_label.setObjectName("focus_label")
        self.obs_img = QtWidgets.QLabel(parent=FocusDecipher)
        self.obs_img.setGeometry(QtCore.QRect(180, 580, 315, 120))
        self.obs_img.setAutoFillBackground(True)
        self.obs_img.setText("")
        self.obs_img.setObjectName("obs_img")
        self.focus_img = QtWidgets.QLabel(parent=FocusDecipher)
        self.focus_img.setGeometry(QtCore.QRect(460, 110, 175, 260))
        self.focus_img.setAutoFillBackground(True)
        self.focus_img.setText("")
        self.focus_img.setObjectName("focus_img")
        self.letgo_label = QtWidgets.QLabel(parent=FocusDecipher)
        self.letgo_label.setGeometry(QtCore.QRect(30, 20, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_label.setFont(font)
        self.letgo_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.letgo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.letgo_label.setObjectName("letgo_label")
        self.you_label = QtWidgets.QLabel(parent=FocusDecipher)
        self.you_label.setGeometry(QtCore.QRect(240, 110, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_label.setFont(font)
        self.you_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.you_label.setObjectName("you_label")
        self.you_img = QtWidgets.QLabel(parent=FocusDecipher)
        self.you_img.setGeometry(QtCore.QRect(250, 200, 175, 260))
        self.you_img.setAutoFillBackground(True)
        self.you_img.setText("")
        self.you_img.setObjectName("you_img")
        self.letgo_img = QtWidgets.QLabel(parent=FocusDecipher)
        self.letgo_img.setGeometry(QtCore.QRect(40, 110, 175, 260))
        self.letgo_img.setAutoFillBackground(True)
        self.letgo_img.setText("")
        self.letgo_img.setObjectName("letgo_img")
        self.obs_label = QtWidgets.QLabel(parent=FocusDecipher)
        self.obs_label.setGeometry(QtCore.QRect(240, 490, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_label.setFont(font)
        self.obs_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.obs_label.setObjectName("obs_label")
        self.letgo_title = QtWidgets.QLabel(parent=FocusDecipher)
        self.letgo_title.setGeometry(QtCore.QRect(30, 60, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_title.setFont(font)
        self.letgo_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.letgo_title.setAutoFillBackground(True)
        self.letgo_title.setText("")
        self.letgo_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.letgo_title.setObjectName("letgo_title")
        self.you_title = QtWidgets.QLabel(parent=FocusDecipher)
        self.you_title.setGeometry(QtCore.QRect(240, 150, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_title.setFont(font)
        self.you_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_title.setAutoFillBackground(True)
        self.you_title.setText("")
        self.you_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.you_title.setObjectName("you_title")
        self.focus_title = QtWidgets.QLabel(parent=FocusDecipher)
        self.focus_title.setGeometry(QtCore.QRect(450, 60, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_title.setFont(font)
        self.focus_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.focus_title.setAutoFillBackground(True)
        self.focus_title.setText("")
        self.focus_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.focus_title.setObjectName("focus_title")
        self.obs_title = QtWidgets.QLabel(parent=FocusDecipher)
        self.obs_title.setGeometry(QtCore.QRect(240, 530, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_title.setFont(font)
        self.obs_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_title.setAutoFillBackground(True)
        self.obs_title.setText("")
        self.obs_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.obs_title.setObjectName("you_title_2")

        self.retranslateUi(FocusDecipher)
        QtCore.QMetaObject.connectSlotsByName(FocusDecipher)

    def retranslateUi(self, FocusDecipher):
        _translate = QtCore.QCoreApplication.translate
        FocusDecipher.setWindowTitle(_translate("FocusDecipher", "Form"))
        self.focus_label.setText(_translate("FocusDecipher", "Focus On"))
        self.letgo_label.setText(_translate("FocusDecipher", "Let Go Of"))
        self.you_label.setText(_translate("FocusDecipher", "Where You Are Now"))
        self.obs_label.setText(_translate("FocusDecipher", "Your Obstacle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FocusDecipher = QtWidgets.QWidget()
    ui = Ui_FocusDecipher()
    ui.setupUi(FocusDecipher)
    FocusDecipher.show()
    sys.exit(app.exec())
