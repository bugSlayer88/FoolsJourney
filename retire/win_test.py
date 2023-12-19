# import sys
#
# from PyQt6.QtCore import Qt
# from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.label = QLabel("Click in this window")
#         self.setCentralWidget(self.label)
#
#     def mouseMoveEvent(self, e):
#         self.label.setText("mouseMoveEvent")
#
#     def mousePressEvent(self, e):
#         self.label.setText("mousePressEvent")
#
#     def mouseReleaseEvent(self, e):
#         self.label.setText("mouseReleaseEvent")
#
#     def mouseDoubleClickEvent(self, e):
#         self.label.setText("mouseDoubleClickEvent")
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()