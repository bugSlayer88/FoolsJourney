# Form implementation generated from reading ui file '.\launch_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainTarotWindow(object):
    def setupUi(self, MainTarotWindow):
        MainTarotWindow.setObjectName("MainTarotWindow")
        MainTarotWindow.resize(603, 295)
        self.centralwidget = QtWidgets.QWidget(parent=MainTarotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.intro_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.intro_label.setGeometry(QtCore.QRect(40, 30, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Gelo Light")
        font.setPointSize(28)
        self.intro_label.setFont(font)
        self.intro_label.setObjectName("intro_label")
        self.reading_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reading_btn.setGeometry(QtCore.QRect(40, 170, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gelo")
        font.setPointSize(16)
        self.reading_btn.setFont(font)
        self.reading_btn.setObjectName("reading_btn")
        self.decipher_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decipher_btn.setGeometry(QtCore.QRect(310, 170, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gelo")
        font.setPointSize(16)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")
        self.spread_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.spread_combo.setGeometry(QtCore.QRect(60, 100, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Gelo")
        font.setPointSize(16)
        self.spread_combo.setFont(font)
        self.spread_combo.setObjectName("spread_combo")
        MainTarotWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainTarotWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 22))
        self.menubar.setObjectName("menubar")
        MainTarotWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainTarotWindow)
        self.statusbar.setObjectName("statusbar")
        MainTarotWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainTarotWindow)
        QtCore.QMetaObject.connectSlotsByName(MainTarotWindow)

    def retranslateUi(self, MainTarotWindow):
        _translate = QtCore.QCoreApplication.translate
        MainTarotWindow.setWindowTitle(_translate("MainTarotWindow", "MainWindow"))
        self.intro_label.setText(_translate("MainTarotWindow", "Hello! What do you want to do?"))
        self.reading_btn.setText(_translate("MainTarotWindow", "Get a Reading"))
        self.decipher_btn.setText(_translate("MainTarotWindow", "Decipher a Reading"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainTarotWindow = QtWidgets.QMainWindow()
    ui = Ui_MainTarotWindow()
    ui.setupUi(MainTarotWindow)
    MainTarotWindow.show()
    sys.exit(app.exec())