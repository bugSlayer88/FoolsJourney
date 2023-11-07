from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 772)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # define QLabel which will become our image
        self.image_01 = QtWidgets.QLabel(parent=Form)
        self.image_01.setText("")
        self.image_01.setObjectName("image_01")

        # define our pixmap path and scale it down
        self.pixmap_01 = QPixmap('images/marseille/01_fool.jpg').scaled(178,315)
        # add pixmap to QLabel
        self.image_01.setPixmap(self.pixmap_01)

        self.horizontalLayout.addWidget(self.image_01)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

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
