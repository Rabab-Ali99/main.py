from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

MainUi, _ = loadUiType('untitled.ui')


class MyApp(QMainWindow, MainUi):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.b0.clicked.connect(self.clicked_0)
        self.b1.clicked.connect(self.clicked_1)
        self.b2.clicked.connect(self.clicked_2)
        self.b3.clicked.connect(self.clicked_3)
        self.b4.clicked.connect(self.clicked_4)
        self.b5.clicked.connect(self.clicked_5)
        self.b6.clicked.connect(self.clicked_6)
        self.b7.clicked.connect(self.clicked_7)
        self.b8.clicked.connect(self.clicked_8)
        self.b9.clicked.connect(self.clicked_9)
        self.b_del.clicked.connect(self.del_btn)
        self.b_equ.clicked.connect(self.equ_btn)
        self.b_add.clicked.connect(self.add_btn)
        self.b_min.clicked.connect(self.min_btn)
        self.b_mul.clicked.connect(self.mul_btn)
        self.b_div.clicked.connect(self.div_btn)

    def clicked_0(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "0")

    def clicked_1(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "1")

    def clicked_2(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "2")

    def clicked_3(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "3")

    def clicked_4(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "4")

    def clicked_5(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "5")

    def clicked_6(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "6")

    def clicked_7(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "7")

    def clicked_8(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "8")

    def clicked_9(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + "9")

    def add_btn(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + " + ")

    def min_btn(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + " - ")

    def div_btn(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + " / ")

    def mul_btn(self):
        previoustext = self.out.text()
        self.out.setText(previoustext + " * ")

    def del_btn(self):
        self.out.setText("")

    def equ_btn(self):
        gettext = self.out.text()
        text = gettext.split(" ", 3)
        result = int(text[0]) + int(text[2])
        if text[1] == '+':
            result = int(text[0]) + int(text[2])
        elif text[1] == '-':
            result = int(text[0]) - int(text[2])
        elif text[1] == '*':
            result = int(text[0]) * int(text[2])
        elif text[1] == '/':
            result = int(text[0]) / int(text[2])

        self.out.setText(str(result))


app = QApplication(sys.argv)
x = MyApp()
app.exec()
