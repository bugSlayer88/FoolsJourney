from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UiQuickFocusReading(object):
    def setupUi(self, UiQuickFocusReading):
        UiQuickFocusReading.setObjectName("UiQuickFocusReading")
        UiQuickFocusReading.resize(675, 865)
        self.focus_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.focus_label.setGeometry(QtCore.QRect(450, 10, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_label.setFont(font)
        self.focus_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.focus_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.focus_label.setObjectName("focus_label")
        self.obs_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.obs_img.setGeometry(QtCore.QRect(180, 560, 315, 175))
        self.obs_img.setAutoFillBackground(True)
        self.obs_img.setText("")
        self.obs_img.setObjectName("obs_img")
        self.decipher_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.decipher_btn.setGeometry(QtCore.QRect(160, 810, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")
        self.focus_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.focus_img.setGeometry(QtCore.QRect(460, 50, 175, 315))
        self.focus_img.setAutoFillBackground(True)
        self.focus_img.setText("")
        self.focus_img.setObjectName("focus_img")
        self.letgo_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.letgo_label.setGeometry(QtCore.QRect(30, 10, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_label.setFont(font)
        self.letgo_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.letgo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.letgo_label.setObjectName("letgo_label")
        self.you_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.you_label.setGeometry(QtCore.QRect(240, 100, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_label.setFont(font)
        self.you_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.you_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.you_label.setObjectName("you_label")
        self.you_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.you_img.setGeometry(QtCore.QRect(250, 140, 175, 315))
        self.you_img.setAutoFillBackground(True)
        self.you_img.setText("")
        self.you_img.setObjectName("you_img")
        self.letgo_img = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.letgo_img.setGeometry(QtCore.QRect(40, 50, 175, 315))
        self.letgo_img.setAutoFillBackground(True)
        self.letgo_img.setText("")
        self.letgo_img.setObjectName("letgo_img")
        self.obs_label = QtWidgets.QLabel(parent=UiQuickFocusReading)
        self.obs_label.setGeometry(QtCore.QRect(240, 520, 195, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_label.setFont(font)
        self.obs_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.obs_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.obs_label.setObjectName("obs_label")
        self.letgo_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.letgo_btn.setGeometry(QtCore.QRect(40, 390, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.letgo_btn.setFont(font)
        self.letgo_btn.setObjectName("letgo_btn")
        self.you_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.you_btn.setGeometry(QtCore.QRect(250, 480, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.you_btn.setFont(font)
        self.you_btn.setObjectName("you_btn")
        self.focus_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.focus_btn.setGeometry(QtCore.QRect(460, 390, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.focus_btn.setFont(font)
        self.focus_btn.setObjectName("focus_btn")
        self.obs_btn = QtWidgets.QPushButton(parent=UiQuickFocusReading)
        self.obs_btn.setGeometry(QtCore.QRect(250, 760, 175, 26))
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        self.obs_btn.setFont(font)
        self.obs_btn.setObjectName("obs_btn")

        self.retranslateUi(UiQuickFocusReading)
        QtCore.QMetaObject.connectSlotsByName(UiQuickFocusReading)

    def retranslateUi(self, UiQuickFocusReading):
        _translate = QtCore.QCoreApplication.translate
        UiQuickFocusReading.setWindowTitle(_translate("UiQuickFocusReading", "Focus Reading"))
        self.focus_label.setText(_translate("UiQuickFocusReading", "Focus On"))
        self.decipher_btn.setText(_translate("UiQuickFocusReading", "Show Explanation"))
        self.letgo_label.setText(_translate("UiQuickFocusReading", "Let Go Of"))
        self.you_label.setText(_translate("UiQuickFocusReading", "Where You Are Now"))
        self.obs_label.setText(_translate("UiQuickFocusReading", "Your Obstacle"))
        self.letgo_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))
        self.you_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))
        self.focus_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))
        self.obs_btn.setText(_translate("UiQuickFocusReading", "Draw Card"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UiQuickFocusReading = QtWidgets.QWidget()
    ui = Ui_UiQuickFocusReading()
    ui.setupUi(UiQuickFocusReading)
    UiQuickFocusReading.show()
    sys.exit(app.exec())
