from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_calculator(object):
    def setupUi(self, window_calculator):
        window_calculator.setObjectName("window_calculator")
        window_calculator.resize(395, 450)
        window_calculator.setStyleSheet("background-color: rgb(241, 244, 243);")
        window_calculator.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(window_calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.button_four = QtWidgets.QPushButton(self.centralwidget)
        self.button_four.setGeometry(QtCore.QRect(10, 220, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_four.setFont(font)
        self.button_four.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;")
        self.button_four.setObjectName("button_four")
        self.button_five = QtWidgets.QPushButton(self.centralwidget)
        self.button_five.setGeometry(QtCore.QRect(105, 220, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_five.setFont(font)
        self.button_five.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;")
        self.button_five.setObjectName("button_five")
        self.button_three = QtWidgets.QPushButton(self.centralwidget)
        self.button_three.setGeometry(QtCore.QRect(200, 285, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_three.setFont(font)
        self.button_three.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;")
        self.button_three.setObjectName("button_three")
        self.percentage_button = QtWidgets.QPushButton(self.centralwidget)
        self.percentage_button.setGeometry(QtCore.QRect(200, 90, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.percentage_button.setFont(font)
        self.percentage_button.setStyleSheet("background-color: rgb(252, 248, 246);\n"
                                             "border-color: rgb(166, 166, 166);\n"
                                             "border-width: 1px;\n"
                                             "border-style:solid;;\n"
                                             "border-radius: 4;")
        self.percentage_button.setObjectName("percentage_button")
        self.button_one = QtWidgets.QPushButton(self.centralwidget)
        self.button_one.setGeometry(QtCore.QRect(10, 285, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_one.setFont(font)
        self.button_one.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;\n"
                                      "border-radius: 4;")
        self.button_one.setObjectName("button_one")
        self.button_seven = QtWidgets.QPushButton(self.centralwidget)
        self.button_seven.setGeometry(QtCore.QRect(10, 155, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_seven.setFont(font)
        self.button_seven.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;")
        self.button_seven.setObjectName("button_seven")
        self.button_nine = QtWidgets.QPushButton(self.centralwidget)
        self.button_nine.setGeometry(QtCore.QRect(200, 155, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_nine.setFont(font)
        self.button_nine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;")
        self.button_nine.setObjectName("button_nine")
        self.esc_button = QtWidgets.QPushButton(self.centralwidget)
        self.esc_button.setGeometry(QtCore.QRect(105, 90, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.esc_button.setFont(font)
        self.esc_button.setStyleSheet("background-color: rgb(252, 248, 246);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;;\n"
                                      "border-radius: 4;")
        self.esc_button.setObjectName("esc_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(10, 350, 185, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.zero_button.setFont(font)
        self.zero_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;")
        self.zero_button.setObjectName("zero_button")
        self.button_six = QtWidgets.QPushButton(self.centralwidget)
        self.button_six.setGeometry(QtCore.QRect(200, 220, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_six.setFont(font)
        self.button_six.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;\n"
                                      "border-radius: 4;")
        self.button_six.setObjectName("button_six")
        self.button_eight = QtWidgets.QPushButton(self.centralwidget)
        self.button_eight.setGeometry(QtCore.QRect(105, 155, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_eight.setFont(font)
        self.button_eight.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;")
        self.button_eight.setObjectName("button_eight")
        self.button_two = QtWidgets.QPushButton(self.centralwidget)
        self.button_two.setGeometry(QtCore.QRect(105, 285, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_two.setFont(font)
        self.button_two.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;\n"
                                      "border-radius: 4;")
        self.button_two.setObjectName("button_two")
        self.division_button = QtWidgets.QPushButton(self.centralwidget)
        self.division_button.setGeometry(QtCore.QRect(295, 90, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.division_button.setFont(font)
        self.division_button.setStyleSheet("background-color: rgb(252, 248, 246);\n"
                                           "border-color: rgb(166, 166, 166);\n"
                                           "border-width: 1px;\n"
                                           "border-style:solid;;\n"
                                           "border-radius: 4;")
        self.division_button.setObjectName("division_button")
        self.multiplication_button = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication_button.setGeometry(QtCore.QRect(295, 155, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.multiplication_button.setFont(font)
        self.multiplication_button.setStyleSheet("background-color: rgb(252, 248, 246);\n"
                                                 "border-color: rgb(166, 166, 166);\n"
                                                 "border-width: 1px;\n"
                                                 "border-style:solid;\n"
                                                 "border-radius: 4;")
        self.multiplication_button.setObjectName("multiplication_button")
        self.subtraction_button = QtWidgets.QPushButton(self.centralwidget)
        self.subtraction_button.setGeometry(QtCore.QRect(295, 220, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.subtraction_button.setFont(font)
        self.subtraction_button.setStyleSheet("background-color: rgb(252, 248, 246);\n"
                                              "border-color: rgb(166, 166, 166);\n"
                                              "border-width: 1px;\n"
                                              "border-style:solid;\n"
                                              "border-radius: 4;")
        self.subtraction_button.setObjectName("subtraction_button")
        self.addition_button = QtWidgets.QPushButton(self.centralwidget)
        self.addition_button.setGeometry(QtCore.QRect(295, 285, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addition_button.setFont(font)
        self.addition_button.setStyleSheet("background-color: rgb(252, 248, 246);\n"
                                           "border-color: rgb(166, 166, 166);\n"
                                           "border-width: 1px;\n"
                                           "border-style:solid;\n"
                                           "border-radius: 4;")
        self.addition_button.setObjectName("addition_button")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 10, 375, 70))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setToolTip("")
        self.display.setStyleSheet("background-color: rgb(239, 244, 245);\n"
                                   "border-color: rgb(166, 166, 166);\n"
                                   "border-width: 1px;\n"
                                   "border-style:solid;\n"
                                   "border-radius: 5;")
        self.display.setText("")
        self.display.setObjectName("display")
        self.ac_button = QtWidgets.QPushButton(self.centralwidget)
        self.ac_button.setGeometry(QtCore.QRect(10, 90, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ac_button.setFont(font)
        self.ac_button.setStyleSheet("background-color: rgb(252, 248, 246);\n"
                                     "border-color: rgb(166, 166, 166);\n"
                                     "border-width: 1px;\n"
                                     "border-style:solid;\n"
                                     "border-radius: 4;")
        self.ac_button.setObjectName("ac_button")
        self.point_button = QtWidgets.QPushButton(self.centralwidget)
        self.point_button.setGeometry(QtCore.QRect(200, 350, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.point_button.setFont(font)
        self.point_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;")
        self.point_button.setObjectName("point_button")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(295, 350, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.equal_button.setFont(font)
        self.equal_button.setStyleSheet("background-color: rgb(0, 159, 170);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;")
        self.equal_button.setObjectName("equal_button")
        window_calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 21))
        self.menubar.setObjectName("menubar")
        window_calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_calculator)
        self.statusbar.setObjectName("statusbar")
        window_calculator.setStatusBar(self.statusbar)

        self.retranslateUi(window_calculator)
        QtCore.QMetaObject.connectSlotsByName(window_calculator)

    def retranslateUi(self, window_calculator):
        _translate = QtCore.QCoreApplication.translate
        window_calculator.setWindowTitle(_translate("window_calculator", "Calculadora Python"))
        self.button_four.setText(_translate("window_calculator", "4"))
        self.button_five.setText(_translate("window_calculator", "5"))
        self.button_three.setText(_translate("window_calculator", "3"))
        self.percentage_button.setText(_translate("window_calculator", "%"))
        self.button_one.setText(_translate("window_calculator", "1"))
        self.button_seven.setText(_translate("window_calculator", "7"))
        self.button_nine.setText(_translate("window_calculator", "9"))
        self.esc_button.setText(_translate("window_calculator", "Esc"))
        self.zero_button.setText(_translate("window_calculator", "0"))
        self.button_six.setText(_translate("window_calculator", "6"))
        self.button_eight.setText(_translate("window_calculator", "8"))
        self.button_two.setText(_translate("window_calculator", "2"))
        self.division_button.setText(_translate("window_calculator", "/"))
        self.multiplication_button.setText(_translate("window_calculator", "*"))
        self.subtraction_button.setText(_translate("window_calculator", "-"))
        self.addition_button.setText(_translate("window_calculator", "+"))
        self.ac_button.setText(_translate("window_calculator", "AC"))
        self.point_button.setText(_translate("window_calculator", "."))
        self.equal_button.setText(_translate("window_calculator", "="))


if __name__ == "__main__":

    from sys import argv, exit
    app = QtWidgets.QApplication(argv)
    window_calculator = QtWidgets.QMainWindow()
    ui = Ui_window_calculator()
    ui.setupUi(window_calculator)
    window_calculator.show()
    exit(app.exec_())
