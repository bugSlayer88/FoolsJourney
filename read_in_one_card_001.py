from PyQt6 import QtCore, QtGui, QtWidgets
import create_deck
import meanings_dictionary

suits = create_deck.suits
ranks = create_deck.ranks
majors = create_deck.major_arcanas

keywords_major = meanings_dictionary.major_key_dict
keywords_minor = meanings_dictionary.minor_key_dict
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(244, 346)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 201, 311))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.card_01 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.card_01.setFont(font)
        self.card_01.setObjectName("card_01")
        self.gridLayout.addWidget(self.card_01, 0, 0, 1, 2)

        self.card_01_arcana = QtWidgets.QLabel(parent=self.widget)
        self.card_01_arcana.setObjectName("card_01_arcana")
        self.gridLayout.addWidget(self.card_01_arcana, 1, 0, 1, 1)

        self.card_01_major = QtWidgets.QRadioButton(parent=self.widget)
        self.card_01_major.setObjectName("card_01_major")
        self.gridLayout.addWidget(self.card_01_major, 1, 1, 1, 1)

        self.card_01_major.toggled.connect(self.radio_arcana_selected)

        self.card_01_minor = QtWidgets.QRadioButton(parent=self.widget)
        self.card_01_minor.setObjectName("card_01_minor")
        self.gridLayout.addWidget(self.card_01_minor, 2, 1, 1, 1)

        self.card_01_minor.toggled.connect(self.radio_arcana_selected)

        self.card_01_number_combo = QtWidgets.QComboBox(parent=self.widget)
        self.card_01_number_combo.setObjectName("card_01_number_combo")
        self.gridLayout.addWidget(self.card_01_number_combo, 3, 0, 1, 1)

        self.card_01_number_combo.addItem('Select Rank')
        self.card_01_number_combo.addItems(ranks)

        self.card_01_suits_combo = QtWidgets.QComboBox(parent=self.widget)
        self.card_01_suits_combo.setObjectName("card_01_suits_combo")
        self.gridLayout.addWidget(self.card_01_suits_combo, 3, 1, 1, 1)

        self.card_01_suits_combo.addItem("Select Suit")
        self.card_01_suits_combo.addItems(suits)

        self.card_01_suits_combo.currentTextChanged.connect(self.minor_combo_update)

        self.card_01_major_combo = QtWidgets.QComboBox(parent=self.widget)
        self.card_01_major_combo.setObjectName("card_01_major_combo")
        self.gridLayout.addWidget(self.card_01_major_combo, 4, 0, 1, 2)

        self.card_01_major_combo.addItem("Select Card")
        self.card_01_major_combo.addItems(majors)

        self.card_01_major_combo.currentTextChanged.connect(self.major_combo_update)

        self.card_01_mean_btn = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.card_01_mean_btn.setFont(font)
        self.card_01_mean_btn.setObjectName("card_01_mean_btn")
        self.gridLayout.addWidget(self.card_01_mean_btn, 5, 0, 1, 2)

        self.card_01_mean_label = QtWidgets.QLabel(parent=self.widget)
        self.card_01_mean_label.setText("")
        self.card_01_mean_label.setObjectName("card_01_mean_label")
        self.gridLayout.addWidget(self.card_01_mean_label, 6, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def radio_arcana_selected(self):
        if self.card_01_major.isChecked():
            self.card_01_suits_combo.setDisabled(True)
            self.card_01_number_combo.setDisabled(True)
            self.card_01_major_combo.setDisabled(False)
        elif self.card_01_minor.isChecked():
            self.card_01_major_combo.setDisabled(True)
            self.card_01_suits_combo.setDisabled(False)
            self.card_01_number_combo.setDisabled(False)

    def minor_combo_update(self):
        rank_selected = self.card_01_number_combo.currentText()
        minor_keys = keywords_minor[rank_selected]
        self.card_01_mean_label.setText(minor_keys[0])

    def major_combo_update(self):
        major_selected = self.card_01_major_combo.currentText()
        major_keys = keywords_major[major_selected]
        self.card_01_mean_label.setText(major_keys[0])


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.card_01.setText(_translate("Form", "First Card"))
        self.card_01_arcana.setText(_translate("Form", "Arcana"))
        self.card_01_major.setText(_translate("Form", "Major"))
        self.card_01_minor.setText(_translate("Form", "Minor"))
        self.card_01_mean_btn.setText(_translate("Form", "Get Meaning"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
