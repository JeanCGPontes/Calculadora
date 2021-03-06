# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_reference.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_calculator(object):
    def setupUi(self, window_calculator):
        window_calculator.setObjectName("window_calculator")
        window_calculator.resize(391, 490)
        window_calculator.setStyleSheet("background-color: rgb(21, 21, 21);")
        window_calculator.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(window_calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.button_four = QtWidgets.QPushButton(self.centralwidget)
        self.button_four.setGeometry(QtCore.QRect(5, 238, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_four.setFont(font)
        self.button_four.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(206,206,206);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color: rgb(228, 228, 228)}")
        self.button_four.setObjectName("button_four")
        self.button_five = QtWidgets.QPushButton(self.centralwidget)
        self.button_five.setGeometry(QtCore.QRect(101, 238, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_five.setFont(font)
        self.button_five.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(206,206,206);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color: rgb(228, 228, 228)}")
        self.button_five.setObjectName("button_five")
        self.button_three = QtWidgets.QPushButton(self.centralwidget)
        self.button_three.setGeometry(QtCore.QRect(197, 308, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_three.setFont(font)
        self.button_three.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(206,206,206);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(228, 228, 228)}")
        self.button_three.setObjectName("button_three")
        self.percentage_button = QtWidgets.QPushButton(self.centralwidget)
        self.percentage_button.setGeometry(QtCore.QRect(197, 98, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.percentage_button.setFont(font)
        self.percentage_button.setStyleSheet("QPushButton {\n"
                                             "background-color: rgb(96, 166, 111);\n"
                                             "border-color: rgb(166, 166, 166);\n"
                                             "border-width: 1px;\n"
                                             "border-style:solid;\n"
                                             "border-radius: 3;}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "background-color: rgb(96, 166, 111, 200)}\n"
                                             "")
        self.percentage_button.setObjectName("percentage_button")
        self.button_one = QtWidgets.QPushButton(self.centralwidget)
        self.button_one.setGeometry(QtCore.QRect(5, 308, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_one.setFont(font)
        self.button_one.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(206,206,206);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;\n"
                                      "border-radius: 4;}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(228, 228, 228)}")
        self.button_one.setObjectName("button_one")
        self.button_seven = QtWidgets.QPushButton(self.centralwidget)
        self.button_seven.setGeometry(QtCore.QRect(5, 168, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_seven.setFont(font)
        self.button_seven.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(206,206,206);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(228, 228, 228)}")
        self.button_seven.setObjectName("button_seven")
        self.button_nine = QtWidgets.QPushButton(self.centralwidget)
        self.button_nine.setGeometry(QtCore.QRect(197, 168, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_nine.setFont(font)
        self.button_nine.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(206,206,206);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color: rgb(228, 228, 228)}")
        self.button_nine.setObjectName("button_nine")
        self.esc_button = QtWidgets.QPushButton(self.centralwidget)
        self.esc_button.setGeometry(QtCore.QRect(101, 98, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.esc_button.setFont(font)
        self.esc_button.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(96, 166, 111);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;\n"
                                      "border-radius: 3;}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(96, 166, 111, 200)}\n"
                                      "")
        self.esc_button.setObjectName("esc_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(5, 378, 190, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.zero_button.setFont(font)
        self.zero_button.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(206,206,206);\n"
                                       "border-color: rgb(166, 166, 166);\n"
                                       "border-width: 1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius: 4;}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color: rgb(228, 228, 228)}")
        self.zero_button.setObjectName("zero_button")
        self.button_six = QtWidgets.QPushButton(self.centralwidget)
        self.button_six.setGeometry(QtCore.QRect(197, 238, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_six.setFont(font)
        self.button_six.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(206,206,206);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;\n"
                                      "border-radius: 4;}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(228, 228, 228)}")
        self.button_six.setObjectName("button_six")
        self.button_eight = QtWidgets.QPushButton(self.centralwidget)
        self.button_eight.setGeometry(QtCore.QRect(101, 168, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_eight.setFont(font)
        self.button_eight.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(206,206,206);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(228, 228, 228)}")
        self.button_eight.setObjectName("button_eight")
        self.button_two = QtWidgets.QPushButton(self.centralwidget)
        self.button_two.setGeometry(QtCore.QRect(101, 308, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_two.setFont(font)
        self.button_two.setStyleSheet("QPushButton {\n"
                                      "background-color: rgb(206,206,206);\n"
                                      "border-color: rgb(166, 166, 166);\n"
                                      "border-width: 1px;\n"
                                      "border-style:solid;\n"
                                      "border-radius: 4;}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(228, 228, 228)}")
        self.button_two.setObjectName("button_two")
        self.division_button = QtWidgets.QPushButton(self.centralwidget)
        self.division_button.setGeometry(QtCore.QRect(293, 98, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.division_button.setFont(font)
        self.division_button.setStyleSheet("QPushButton {\n"
                                           "background-color: rgb(96, 166, 111);\n"
                                           "border-color: rgb(166, 166, 166);\n"
                                           "border-width: 1px;\n"
                                           "border-style:solid;\n"
                                           "border-radius: 3;}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background-color: rgb(96, 166, 111, 200)}\n"
                                           "")
        self.division_button.setObjectName("division_button")
        self.multiplication_button = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication_button.setGeometry(QtCore.QRect(293, 168, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.multiplication_button.setFont(font)
        self.multiplication_button.setStyleSheet("QPushButton {\n"
                                                 "background-color: rgb(96, 166, 111);\n"
                                                 "border-color: rgb(166, 166, 166);\n"
                                                 "border-width: 1px;\n"
                                                 "border-style:solid;\n"
                                                 "border-radius: 4;}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "background-color: rgb(96, 166, 111, 200)}")
        self.multiplication_button.setObjectName("multiplication_button")
        self.subtraction_button = QtWidgets.QPushButton(self.centralwidget)
        self.subtraction_button.setGeometry(QtCore.QRect(293, 238, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.subtraction_button.setFont(font)
        self.subtraction_button.setStyleSheet("QPushButton {\n"
                                              "background-color: rgb(96, 166, 111);\n"
                                              "border-color: rgb(166, 166, 166);\n"
                                              "border-width: 1px;\n"
                                              "border-style:solid;\n"
                                              "border-radius: 4;}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "background-color: rgb(96, 166, 111, 200)}")
        self.subtraction_button.setObjectName("subtraction_button")
        self.addition_button = QtWidgets.QPushButton(self.centralwidget)
        self.addition_button.setGeometry(QtCore.QRect(293, 308, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addition_button.setFont(font)
        self.addition_button.setStyleSheet("QPushButton {\n"
                                           "background-color: rgb(96, 166, 111);\n"
                                           "border-color: rgb(166, 166, 166);\n"
                                           "border-width: 1px;\n"
                                           "border-style:solid;\n"
                                           "border-radius: 4;}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background-color: rgb(96, 166, 111, 200)}")
        self.addition_button.setObjectName("addition_button")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(5, 5, 382, 88))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setToolTip("")
        self.display.setStyleSheet("color: rgb(206, 206, 206);\n"
                                   "background-color: rgb(23, 23, 23);\n"
                                   "border-color: rgb(166, 166, 166);\n"
                                   "border-width: 1px;\n"
                                   "border-style:solid;\n"
                                   "border-radius: 3;")
        self.display.setText("")
        self.display.setObjectName("display")
        self.ac_button = QtWidgets.QPushButton(self.centralwidget)
        self.ac_button.setGeometry(QtCore.QRect(5, 98, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ac_button.setFont(font)
        self.ac_button.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(96, 166, 111);\n"
                                     "border-color: rgb(166, 166, 166);\n"
                                     "border-width: 1px;\n"
                                     "border-style:solid;\n"
                                     "border-radius: 3;}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background-color: rgb(96, 166, 111, 200)}\n"
                                     "")
        self.ac_button.setObjectName("ac_button")
        self.point_button = QtWidgets.QPushButton(self.centralwidget)
        self.point_button.setGeometry(QtCore.QRect(197, 378, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.point_button.setFont(font)
        self.point_button.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(206,206,206);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style:solid;\n"
                                        "border-radius: 4;}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(228, 228, 228)}")
        self.point_button.setObjectName("point_button")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(293, 378, 94, 68))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.equal_button.setFont(font)
        self.equal_button.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(107, 197, 107);\n"
                                        "border-color: rgb(166, 166, 166);\n"
                                        "border-width: 1px;\n"
                                        "border-style: solid;\n"
                                        "border-radius: 4;}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgba(107, 197, 107, 200);}")
        self.equal_button.setObjectName("equal_button")
        window_calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuDesign = QtWidgets.QMenu(self.menubar)
        self.menuDesign.setObjectName("menuDesign")
        self.menuTema = QtWidgets.QMenu(self.menuDesign)
        self.menuTema.setObjectName("menuTema")
        window_calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_calculator)
        self.statusbar.setObjectName("statusbar")
        window_calculator.setStatusBar(self.statusbar)
        self.actionLight = QtWidgets.QAction(window_calculator)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtWidgets.QAction(window_calculator)
        self.actionDark.setObjectName("actionDark")
        self.menuTema.addAction(self.actionLight)
        self.menuTema.addAction(self.actionDark)
        self.menuDesign.addAction(self.menuTema.menuAction())
        self.menubar.addAction(self.menuDesign.menuAction())

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
        self.menuDesign.setTitle(_translate("window_calculator", "Design"))
        self.menuTema.setTitle(_translate("window_calculator", "Tema"))
        self.actionLight.setText(_translate("window_calculator", "Light"))
        self.actionDark.setText(_translate("window_calculator", "Dark"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window_calculator = QtWidgets.QMainWindow()
    ui = Ui_window_calculator()
    ui.setupUi(window_calculator)
    window_calculator.show()
    sys.exit(app.exec_())
