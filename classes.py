import functions

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(350, 200, 391, 466)  # Setting the window size and position.
        self.setWindowTitle("Calculadora PyQt5")  # Window title setting.
        self.setWindowIcon(QtGui.QIcon('images/calculator_icon.png'))
        self.setStyleSheet('background-color: rgb(241, 244, 243);')  # Window style setting.

        self.number_button_style = ("""QPushButton {background-color: rgb(255, 255, 255);
                                               border-color: rgb(166, 166, 166);
                                               border-width: 1px;
                                               border-style:solid;
                                               border-radius: 3;}
                                             
                                  QPushButton:hover {background-color: rgb(235, 235, 235)}
                                  
                                  QPushButton:pressed {{background-color: rgb(235, 235, 235)}}""")

        self.style_of_math_operation_buttons = ("""QPushButton {background-color: rgba(13, 202, 174, 168);
                                                           border-color: rgb(166, 166, 166);
                                                           border-width: 1px;
                                                           border-style:solid;
                                                           border-radius: 3;}

                                              QPushButton:hover {background-color: rgb(13, 202, 174, 200)}""")
        self.equal_button_style = ("""QPushButton {background-color: rgba(0, 135, 159, 180);
                                 border-color: rgb(166, 166, 166);
                                 border-width: 1px;
                                 border-style: solid;
                                 border-radius: 3;}

                                 QPushButton:hover {background-color: rgba(0, 135, 159, 200);}""")
        self.label_style = ("""background-color: rgb(252, 252, 252);
                          border-color: rgb(166, 166, 166);
                          border-width: 1px;
                          border-style:solid;
                          border-radius: 3;""")

        self.math_expression = ''

        self.label_font = functions.get_font("Century Gothic", False, 24)
        self.button_font = functions.get_font("Miriam Libre", True, 16)

        self.display = self.create_label('', 5, 5, 382, 88, self.label_style)
        self.button_0 = self.create_button('0', 5, 378, 190, 68, self.number_button_style)
        self.button_1 = self.create_button('1', 5, 308, 94, 68, self.number_button_style)
        self.button_2 = self.create_button('2', 101, 308, 94, 68, self.number_button_style)
        self.button_3 = self.create_button('3', 197, 308, 94, 68, self.number_button_style)
        self.button_4 = self.create_button('4', 5, 238, 94, 68, self.number_button_style)
        self.button_5 = self.create_button('5', 101, 238, 94, 68, self.number_button_style)
        self.button_6 = self.create_button('6', 197, 238, 94, 68, self.number_button_style)
        self.button_7 = self.create_button('7', 5, 168, 94, 68, self.number_button_style)
        self.button_8 = self.create_button('8', 101, 168, 94, 68, self.number_button_style)
        self.button_9 = self.create_button('9', 197, 168, 94, 68, self.number_button_style)
        self.point_button = self.create_button('.', 197, 378, 94, 68, self.number_button_style)
        self.equal_button = self.create_button('=', 293, 378, 94, 68, self.equal_button_style)
        self.addition_button = self.create_button('+', 293, 308, 94, 68, self.style_of_math_operation_buttons)
        self.subtraction_button = self.create_button('-', 293, 238, 94, 68, self.style_of_math_operation_buttons)
        self.multiplication_button = self.create_button('*', 293, 168, 94, 68, self.style_of_math_operation_buttons)
        self.division_button = self.create_button('/', 293, 98, 94, 68, self.style_of_math_operation_buttons)
        self.percentage_button = self.create_button('%', 197, 98, 94, 68, self.style_of_math_operation_buttons)
        self.esc_button = self.create_button('Esc', 101, 98, 94, 68, self.style_of_math_operation_buttons)
        self.ac_button = self.create_button('AC', 5, 98, 94, 68, self.style_of_math_operation_buttons)

        self.button_0.clicked.connect(self.click_0_button)
        self.button_1.clicked.connect(self.click_1_button)
        self.button_2.clicked.connect(self.click_2_button)
        self.button_3.clicked.connect(self.click_3_button)
        self.button_4.clicked.connect(self.click_4_button)
        self.button_5.clicked.connect(self.click_5_button)
        self.button_6.clicked.connect(self.click_6_button)
        self.button_7.clicked.connect(self.click_7_button)
        self.button_8.clicked.connect(self.click_8_button)
        self.button_9.clicked.connect(self.click_9_button)
        self.point_button.clicked.connect(self.click_point_button)
        self.equal_button.clicked.connect(self.click_equal_button)
        self.addition_button.clicked.connect(self.click_addition_button)
        self.subtraction_button.clicked.connect(self.click_subtraction_button)
        self.multiplication_button.clicked.connect(self.click_multiplication_button)
        self.division_button.clicked.connect(self.click_division_button)
        self.percentage_button.clicked.connect(self.click_percentage_button)
        self.esc_button.clicked.connect(self.click_esc_button)
        self.ac_button.clicked.connect(self.click_ac_button)

        self.show()  # Show all the widgets.

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_0: self.button_0.click()
        elif event.key() == Qt.Key.Key_1: self.button_1.click()
        elif event.key() == Qt.Key.Key_2: self.button_2.click()
        elif event.key() == Qt.Key.Key_3: self.button_3.click()
        elif event.key() == Qt.Key.Key_4: self.button_4.click()
        elif event.key() == Qt.Key.Key_5: self.button_5.click()
        elif event.key() == Qt.Key.Key_6: self.button_6.click()
        elif event.key() == Qt.Key.Key_7: self.button_7.click()
        elif event.key() == Qt.Key.Key_8: self.button_8.click()
        elif event.key() == Qt.Key.Key_9: self.button_9.click()
        elif event.key() == Qt.Key.Key_Delete: self.ac_button.click()
        elif event.key() == Qt.Key.Key_Backspace: self.esc_button.click()
        elif event.key() == Qt.Key.Key_Equal: self.equal_button.click()
        elif event.key() == Qt.Key.Key_Enter: self.equal_button.click()
        elif event.key() == Qt.Key.Key_Plus: self.addition_button.click()
        elif event.key() == Qt.Key.Key_Minus: self.subtraction_button.click()
        elif event.key() == Qt.Key.Key_Asterisk: self.multiplication_button.click()
        elif event.key() == Qt.Key.Key_Slash: self.division_button.click()
        elif event.key() == Qt.Key.Key_Percent: self.percentage_button.click()
        elif event.key() == Qt.Key.Key_Period: self.point_button.click()

        else: pass

    def create_label(self, content: str, x_position: int, y_position: int, width: int, height: int, style: str):
        label = QtWidgets.QLabel(self)
        label.setText(content)
        label.setGeometry(x_position, y_position, width, height)
        label.setStyleSheet(style)
        label.setFont(self.label_font)
        return label

    def create_button(self, content: str, x_position: int, y_position: int, width: int, height: int, style: str):
        button = QtWidgets.QPushButton(self)
        button.setText(content)
        button.setGeometry(x_position, y_position, width, height)
        button.setStyleSheet(style)
        button.setFont(self.button_font)
        return button

    def click_0_button(self):
        self.math_expression += '0'
        self.display.setText(self.math_expression)

    def click_1_button(self):
        self.math_expression += '1'
        self.display.setText(self.math_expression)

    def click_2_button(self):
        self.math_expression += '2'
        self.display.setText(self.math_expression)

    def click_3_button(self):
        self.math_expression += '3'
        self.display.setText(self.math_expression)

    def click_4_button(self):
        self.math_expression += '4'
        self.display.setText(self.math_expression)

    def click_5_button(self):
        self.math_expression += '5'
        self.display.setText(self.math_expression)

    def click_6_button(self):
        self.math_expression += '6'
        self.display.setText(self.math_expression)

    def click_7_button(self):
        self.math_expression += '7'
        self.display.setText(self.math_expression)

    def click_8_button(self):
        self.math_expression += '8'
        self.display.setText(self.math_expression)

    def click_9_button(self):
        self.math_expression += '9'
        self.display.setText(self.math_expression)

    def click_point_button(self):
        self.math_expression += '.'
        self.display.setText(self.math_expression)

    def click_equal_button(self):
        if '%' in self.math_expression:
            try:
                self.math_expression = str(functions.solve_percentage(self.math_expression))
                self.display.setText(self.math_expression)

            except ValueError:
                self.display.setText('Error')

        else:
            try:
                self.math_expression = f"{eval(self.math_expression)}"
                self.display.setText(self.math_expression)

            except SyntaxError or ValueError:
                self.math_expression = ''
                self.display.setText(self.math_expression)

    def click_addition_button(self):
        self.math_expression += '+'
        self.display.setText(self.math_expression)

    def click_subtraction_button(self):
        self.math_expression += '-'
        self.display.setText(self.math_expression)

    def click_multiplication_button(self):
        self.math_expression += '*'
        self.display.setText(self.math_expression)

    def click_division_button(self):
        self.math_expression += '/'
        self.display.setText(self.math_expression)

    def click_percentage_button(self):
        self.math_expression += '%'
        self.display.setText(self.math_expression)

    def click_esc_button(self):
        try:
            self.math_expression = self.math_expression[:-1]
            self.display.setText(self.math_expression)

        except IndexError:
            self.math_expression = ''
            self.display.setText(self.math_expression)

    def click_ac_button(self):
        self.math_expression = ''
        self.display.setText(self.math_expression)
