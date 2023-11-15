from PyQt6 import QtCore, QtGui, QtWidgets

from win_three_deci import Ui_ThreeDecipher
from win_single_deci import UiSingleDecipher
from win_celtic_deci import Ui_CelticDecipher

from win_three_read import Ui_ThreeReading

spreads = ['Single Card', 'Simple Three Cards', 'Celtic Cross', 'Quick Focus']


class Ui_MainTarotWindow(object):
    # def open_decipher_window(self):
    #     spread_selected = self.spread_combo.currentText()
    #     self.window = QtWidgets.QWidget()
    #     if spread_selected == 'Single Card':
    #         self.ui = UiSingleDecipher()
    #     if spread_selected == 'Simple Three Cards':
    #         self.ui = Ui_ThreeDecipher()
    #     if spread_selected == 'Celtic Cross':
    #         self.ui = Ui_CelticDecipher()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

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
        self.reading_btn.setGeometry(QtCore.QRect(40, 200, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gelo")
        font.setPointSize(16)
        self.reading_btn.setFont(font)
        self.reading_btn.setObjectName("reading_btn")

        self.decipher_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decipher_btn.clicked.connect(self.open_decipher_window)

        self.decipher_btn.setGeometry(QtCore.QRect(310, 200, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gelo")
        font.setPointSize(16)
        self.decipher_btn.setFont(font)
        self.decipher_btn.setObjectName("decipher_btn")

        self.spread_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.spread_label.setGeometry(QtCore.QRect(60, 90, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Gelo Light")
        font.setPointSize(22)
        self.spread_label.setFont(font)
        self.spread_label.setObjectName("spread_label")

        self.spread_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.spread_combo.setGeometry(QtCore.QRect(60, 140, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Gelo")
        font.setPointSize(16)
        self.spread_combo.setFont(font)
        self.spread_combo.setObjectName("spread_combo")

        self.spread_combo.addItems(spreads)

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

    def open_decipher_window(self):
        spread_selected = self.spread_combo.currentText()
        self.window = QtWidgets.QWidget()
        if spread_selected == 'Single Card':
            self.ui = UiSingleDecipher()
        if spread_selected == 'Simple Three Cards':
            self.ui = Ui_ThreeDecipher()
        if spread_selected == 'Celtic Cross':
            self.ui = Ui_CelticDecipher()
        self.ui.setupUi(self.window)
        self.window.show()

    def decipher_update(self):
        spread_selected = self.spread_combo.currentText()
        return spread_selected

    def open_reading_window(self):
        spread_selected = self.spread_combo.currentText()
        self.window = QtWidgets.QWidget()
        if spread_selected == 'Single Card':
            # self.ui = UiSingleDec
        if spread_selected == 'Simple Three Cards':
            self.ui = Ui_ThreeReading()
        if spread_selected == 'Celtic Cross':
            # self.ui = Ui_CelticDecipher()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, MainTarotWindow):
        _translate = QtCore.QCoreApplication.translate
        MainTarotWindow.setWindowTitle(_translate("MainTarotWindow", "MainWindow"))
        self.intro_label.setText(_translate("MainTarotWindow", "Hello! What do you want to do?"))
        self.reading_btn.setText(_translate("MainTarotWindow", "Get a Reading"))
        self.decipher_btn.setText(_translate("MainTarotWindow", "Decipher a Reading"))
        self.spread_label.setText(_translate("MainTarotWindow", "Please Select a Tarot Spread:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainTarotWindow = QtWidgets.QMainWindow()
    ui = Ui_MainTarotWindow()
    ui.setupUi(MainTarotWindow)
    MainTarotWindow.show()
    sys.exit(app.exec())
