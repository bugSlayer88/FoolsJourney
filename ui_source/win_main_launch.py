# Form implementation generated from reading ui file '.\win_main_launch.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainLaunchWindow(object):
    def setupUi(self, MainLaunchWindow):
        MainLaunchWindow.setObjectName("MainLaunchWindow")
        MainLaunchWindow.resize(584, 290)
        self.centralwidget = QtWidgets.QWidget(parent=MainLaunchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 509, 223))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.intro_label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        self.intro_label.setFont(font)
        self.intro_label.setObjectName("intro_label")
        self.verticalLayout.addWidget(self.intro_label)
        self.dec_opt_radio = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        self.dec_opt_radio.setFont(font)
        self.dec_opt_radio.setObjectName("dec_opt_radio")
        self.verticalLayout.addWidget(self.dec_opt_radio)
        self.read_opt_radio = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        self.read_opt_radio.setFont(font)
        self.read_opt_radio.setObjectName("read_opt_radio")
        self.verticalLayout.addWidget(self.read_opt_radio)
        self.card_layout_combo = QtWidgets.QComboBox(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        self.card_layout_combo.setFont(font)
        self.card_layout_combo.setCurrentText("")
        self.card_layout_combo.setObjectName("card_layout_combo")
        self.verticalLayout.addWidget(self.card_layout_combo)
        self.show_cards_btn = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Cormorant Infant SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        self.show_cards_btn.setFont(font)
        self.show_cards_btn.setObjectName("show_cards_btn")
        self.verticalLayout.addWidget(self.show_cards_btn)
        MainLaunchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainLaunchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 22))
        self.menubar.setObjectName("menubar")
        MainLaunchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainLaunchWindow)
        self.statusbar.setObjectName("statusbar")
        MainLaunchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainLaunchWindow)
        QtCore.QMetaObject.connectSlotsByName(MainLaunchWindow)

    def retranslateUi(self, MainLaunchWindow):
        _translate = QtCore.QCoreApplication.translate
        MainLaunchWindow.setWindowTitle(_translate("MainLaunchWindow", "MainWindow"))
        self.intro_label.setText(_translate("MainLaunchWindow", "Hello! What do you want to do?:"))
        self.dec_opt_radio.setText(_translate("MainLaunchWindow", "Decipher cards I\'ve already pulled"))
        self.read_opt_radio.setText(_translate("MainLaunchWindow", "Get a full reading here"))
        self.show_cards_btn.setText(_translate("MainLaunchWindow", "Show Me The Cards"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainLaunchWindow = QtWidgets.QMainWindow()
    ui = Ui_MainLaunchWindow()
    ui.setupUi(MainLaunchWindow)
    MainLaunchWindow.show()
    sys.exit(app.exec())
