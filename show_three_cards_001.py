import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

cards = ['Fool', 'Magician', 'Priestess', 'Empress', 'Emperor', 'Hierophant']

image_dir = 'images/marseille'
images = os.listdir(image_dir)
files_path = [os.path.abspath(x) for x in images]


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 523)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(40, 40, 651, 441))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pas_img_label = QtWidgets.QLabel(parent=self.widget)
        self.pas_img_label.setText("")
        self.pas_img_label.setObjectName("pas_img_label")
        self.gridLayout.addWidget(self.pas_img_label, 0, 0, 1, 1)

        self.pre_img_label = QtWidgets.QLabel(parent=self.widget)
        self.pre_img_label.setText("")
        self.pre_img_label.setObjectName("pre_img_label")
        self.gridLayout.addWidget(self.pre_img_label, 0, 1, 1, 1)

        self.fut_img_label = QtWidgets.QLabel(parent=self.widget)
        self.fut_img_label.setText("")
        self.fut_img_label.setObjectName("fut_img_label")
        self.gridLayout.addWidget(self.fut_img_label, 0, 2, 1, 1)

        self.pas_combo = QtWidgets.QComboBox(parent=self.widget)
        self.pas_combo.setObjectName("pas_combo")
        self.gridLayout.addWidget(self.pas_combo, 1, 0, 1, 1)

        self.pas_combo.addItem('Select Card')
        self.pas_combo.addItems(cards)

        self.pas_combo.currentTextChanged.connect(self.pas_combo_update)

        self.pre_combo = QtWidgets.QComboBox(parent=self.widget)
        self.pre_combo.setObjectName("pre_combo")
        self.gridLayout.addWidget(self.pre_combo, 1, 1, 1, 1)

        self.pre_combo.addItem('Select Card')
        self.pre_combo.addItems(cards)

        self.pre_combo.currentTextChanged.connect(self.pre_combo_update)

        self.fut_combo = QtWidgets.QComboBox(parent=self.widget)
        self.fut_combo.setObjectName("fut_combo")
        self.gridLayout.addWidget(self.fut_combo, 1, 2, 1, 1)

        self.fut_combo.addItem('Select Card')
        self.fut_combo.addItems(cards)

        self.fut_combo.currentTextChanged.connect(self.fut_combo_update)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def pas_combo_update(self):
        pas_selected = self.pas_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(pas_selected)
        self.pas_image = QPixmap(pic_path).scaled(175, 315)
        self.pas_img_label.setPixmap(self.pas_image)

    def pre_combo_update(self):
        pre_selected = self.pre_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(pre_selected)
        self.pre_image = QPixmap(pic_path).scaled(175, 315)
        self.pre_img_label.setPixmap(self.pre_image)

    def fut_combo_update(self):
        fut_selected = self.fut_combo.currentText()
        pic_path = 'images/marseille/{}.png'.format(fut_selected)
        self.fut_image = QPixmap(pic_path).scaled(175, 315)
        self.fut_img_label.setPixmap(self.fut_image)

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
