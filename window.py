import math

from PyQt6 import QtCore, QtGui, QtWidgets


BTN_COLOR = "background-color: rgb(58, 20, 60);color: rgb(255, 255, 255)"


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 60))
        self.label.setMargin(10)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);color: black;")
        self.label.setObjectName("label")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 60, 75, 75))
        self.pushButton_1.setStyleSheet(BTN_COLOR)
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(75, 60, 75, 75))
        self.pushButton_2.setStyleSheet(BTN_COLOR)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 60, 75, 75))
        self.pushButton_3.setStyleSheet(BTN_COLOR)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 135, 75, 75))
        self.pushButton_4.setStyleSheet(BTN_COLOR)
        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 135, 75, 75))
        self.pushButton_6.setStyleSheet(BTN_COLOR)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(75, 135, 75, 75))
        self.pushButton_5.setStyleSheet(BTN_COLOR)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 210, 75, 75))
        self.pushButton_7.setStyleSheet(BTN_COLOR)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(75, 210, 75, 75))
        self.pushButton_8.setStyleSheet(BTN_COLOR)
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 210, 75, 75))
        self.pushButton_9.setStyleSheet(BTN_COLOR)
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 285, 75, 75))
        self.pushButton_0.setStyleSheet(BTN_COLOR)
        self.pushButton_0.setObjectName("pushButton_0")

        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(75, 285, 75, 75))
        self.pushButton_dot.setStyleSheet(BTN_COLOR)
        self.pushButton_dot.setObjectName("pushButton_dot")

        self.pushButton_result = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_result.setGeometry(QtCore.QRect(225, 285, 150, 75))
        self.pushButton_result.setStyleSheet(BTN_COLOR)
        self.pushButton_result.setObjectName("pushButton_result")

        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(225, 60, 75, 75))
        self.pushButton_minus.setStyleSheet(BTN_COLOR)
        self.pushButton_minus.setObjectName("pushButton_minus")

        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(300, 60, 75, 75))
        self.pushButton_plus.setStyleSheet(BTN_COLOR)
        self.pushButton_plus.setObjectName("pushButton_plus_2")

        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(225, 135, 75, 75))
        self.pushButton_multiply.setStyleSheet(BTN_COLOR)
        self.pushButton_multiply.setObjectName("pushButton_multiply")

        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(300, 135, 75, 75))
        self.pushButton_divide.setStyleSheet(BTN_COLOR)
        self.pushButton_divide.setObjectName("pushButton_divide")

        self.pushButton_exponent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exponent.setGeometry(QtCore.QRect(225, 210, 75, 75))
        self.pushButton_exponent.setStyleSheet(BTN_COLOR)
        self.pushButton_exponent.setObjectName("pushButton_exponent")

        self.pushButton_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqrt.setGeometry(QtCore.QRect(300, 210, 75, 75))
        self.pushButton_sqrt.setStyleSheet(BTN_COLOR)
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")

        self.pushButton_cos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cos.setGeometry(QtCore.QRect(0, 360, 75, 75))
        self.pushButton_cos.setStyleSheet(BTN_COLOR)
        self.pushButton_cos.setObjectName("pushButton_cos")

        self.pushButton_sin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sin.setGeometry(QtCore.QRect(75, 360, 75, 75))
        self.pushButton_sin.setStyleSheet(BTN_COLOR)
        self.pushButton_sin.setObjectName("pushButton_sin")

        self.pushButton_tan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tan.setGeometry(QtCore.QRect(150, 360, 75, 75))
        self.pushButton_tan.setStyleSheet(BTN_COLOR)
        self.pushButton_tan.setObjectName("pushButton_tan")

        self.pushButton_cot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cot.setGeometry(QtCore.QRect(225, 360, 75, 75))
        self.pushButton_cot.setStyleSheet(BTN_COLOR)
        self.pushButton_cot.setObjectName("pushButton_cot")

        self.pushButton_log = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_log.setGeometry(QtCore.QRect(300, 360, 75, 75))
        self.pushButton_log.setStyleSheet(BTN_COLOR)
        self.pushButton_log.setObjectName("pushButton_log")

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(150, 285, 75, 75))
        self.pushButton_cancel.setStyleSheet(BTN_COLOR)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.clickButton()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_result.setText(_translate("MainWindow", "="))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_multiply.setText(_translate("MainWindow", "*"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_exponent.setText(_translate("MainWindow", "x^2"))
        self.pushButton_sqrt.setText(_translate("MainWindow", "√ "))
        self.pushButton_cos.setText(_translate("MainWindow", "cos"))
        self.pushButton_sin.setText(_translate("MainWindow", "sin"))
        self.pushButton_tan.setText(_translate("MainWindow", "tan"))
        self.pushButton_cot.setText(_translate("MainWindow", "cot"))
        self.pushButton_log.setText(_translate("MainWindow", "log"))
        self.pushButton_cancel.setText(_translate("MainWindow", "C"))

    def clickButton(self):
        self.pushButton_0.clicked.connect(lambda: self.writeSymbol(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda: self.writeSymbol(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.writeSymbol(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.writeSymbol(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.writeSymbol(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.writeSymbol(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.writeSymbol(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.writeSymbol(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.writeSymbol(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.writeSymbol(self.pushButton_9.text()))
        self.pushButton_plus.clicked.connect(lambda: self.writeSymbol(self.pushButton_plus.text()))
        self.pushButton_minus.clicked.connect(lambda: self.writeSymbol(self.pushButton_minus.text()))
        self.pushButton_multiply.clicked.connect(lambda: self.writeSymbol(self.pushButton_multiply.text()))
        self.pushButton_divide.clicked.connect(lambda: self.writeSymbol(self.pushButton_divide.text()))
        self.pushButton_exponent.clicked.connect(lambda: self.writeSymbol("**2"))
        self.pushButton_sqrt.clicked.connect(lambda: self.sqrt())
        self.pushButton_cos.clicked.connect(lambda: self.cos())
        self.pushButton_sin.clicked.connect(lambda: self.sin())
        self.pushButton_tan.clicked.connect(lambda: self.tan())
        self.pushButton_cot.clicked.connect(lambda: self.cot())
        self.pushButton_dot.clicked.connect(lambda: self.writeSymbol(self.pushButton_dot.text()))
        self.pushButton_log.clicked.connect(lambda: self.log())
        self.pushButton_cancel.clicked.connect(lambda: self.clearLabel())
        self.pushButton_result.clicked.connect(self.result)

    def writeSymbol(self, symbol):
        self.label.setText(self.label.text() + symbol)

    def clearLabel(self):
        self.label.setText('')

    def sqrt(self):
        number = self.label.text()
        self.clearLabel()
        self.label.setText(f"math.sqrt({number})")
        self.result()

    def cos(self):
        number = self.label.text()
        self.clearLabel()
        self.label.setText(f"math.cos({number})")
        self.result()

    def sin(self):
        number = self.label.text()
        self.clearLabel()
        self.label.setText(f"math.sin({number})")
        self.result()

    def tan(self):
        number = self.label.text()
        self.clearLabel()
        self.label.setText(f"math.tan({number})")
        self.result()

    def cot(self):
        number = self.label.text()
        self.clearLabel()
        self.label.setText(f"math.cos({number}) / math.sin({number})")
        self.result()

    def log(self):
        number = self.label.text()
        self.clearLabel()
        self.label.setText(f"math.log10({number})")
        self.result()

    def result(self):
        result = compile(self.label.text(), "<string>", "eval")
        self.label.setText(str(eval(result)))
