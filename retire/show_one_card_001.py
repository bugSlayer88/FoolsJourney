import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

cards = ['Fool', 'Magician', 'Priestess', 'Empress', 'Emperor', 'Hierophant']
image_dir = 'images/marseille'
images = os.listdir(image_dir)
files_path = [os.path.abspath(x) for x in images]

class Ui_Form(object):
    def __init__(self):
        self.image = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 342)

        self.card_label = QtWidgets.QLabel(parent=Form)
        self.card_label.setGeometry(QtCore.QRect(20, 20, 135, 255))
        self.card_label.setText("")
        self.card_label.setObjectName("card_label")

        self.card_combo = QtWidgets.QComboBox(parent=Form)
        self.card_combo.setGeometry(QtCore.QRect(20, 290, 135, 22))
        self.card_combo.setObjectName("card_combo")

        self.card_combo.addItem('Select Card')
        self.card_combo.addItems(cards)
        self.card_combo.currentTextChanged.connect(self.combo_update)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def combo_update(self):
        item_selected = self.card_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(item_selected)
        self.image = QPixmap(pic_path).scaled(135,255)
        self.card_label.setPixmap(self.image)


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
