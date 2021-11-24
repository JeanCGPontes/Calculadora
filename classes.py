import functions

from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 395, 450)  # Setting the window size and position.
        self.setWindowTitle("Calculadora PyQt5")  # Window title setting.
        self.setStyleSheet('background-color: rgb(241, 244, 243);')  # Window style setting.

        number_button_style = ("""QPushButton {background-color: rgb(255, 255, 255);
                                               border-color: rgb(166, 166, 166);
                                               border-width: 1px;
                                               border-style:solid;
                                               border-radius: 4;}
                                             
                                  QPushButton:hover {background-color: rgb(235, 235, 235)}""")
        style_of_math_operation_buttons = ("""QPushButton {background-color: rgba(13, 202, 174, 160);
                                                           border-color: rgb(166, 166, 166);
                                                           border-width: 1px;
                                                           border-style:solid;
                                                           border-radius: 4;}

                                              QPushButton:hover {background-color: rgb(13, 202, 174, 200)}""")
        equal_button_style = ("""QPushButton {background-color: rgba(0, 135, 159, 180);
                                 border-color: rgb(166, 166, 166);
                                 border-width: 1px;
                                 border-style: solid;
                                 border-radius: 4;}

                                 QPushButton:hover {background-color: rgba(0, 135, 159, 200);}""")
        label_style = ("""background-color: rgb(252, 252, 252);
                          border-color: rgb(166, 166, 166);
                          border-width: 1px;
                          border-style:solid;
                          border-radius: 5;""")

        self.math_expression = ''

        self.label_font = functions.get_font("Century Gothic", False, 24)
        self.button_font = functions.get_font("Miriam Libre", True, 16)

        self.display = self.create_label('', 10, 10, 375, 70, label_style)
        self.button_0 = self.create_button('0', 10, 350, 185, 60, number_button_style)
        self.button_1 = self.create_button('1', 10, 285, 90, 60, number_button_style)
        self.button_2 = self.create_button('2', 105, 285, 90, 60, number_button_style)
        self.button_3 = self.create_button('3', 200, 285, 90, 60, number_button_style)
        self.button_4 = self.create_button('4', 10, 220, 90, 60, number_button_style)
        self.button_5 = self.create_button('5', 105, 220, 90, 60, number_button_style)
        self.button_6 = self.create_button('6', 200, 220, 90, 60, number_button_style)
        self.button_7 = self.create_button('7', 10, 155, 90, 60, number_button_style)
        self.button_8 = self.create_button('8', 105, 155, 90, 60, number_button_style)
        self.button_9 = self.create_button('9', 200, 155, 90, 60, number_button_style)
        self.point_button = self.create_button('.', 200, 350, 90, 60, number_button_style)
        self.equal_button = self.create_button('=', 295, 350, 90, 60, equal_button_style)
        self.addition_button = self.create_button('+', 295, 285, 90, 60, style_of_math_operation_buttons)
        self.subtraction_button = self.create_button('-', 295, 220, 90, 60, style_of_math_operation_buttons)
        self.multiplication_button = self.create_button('*', 295, 155, 90, 60, style_of_math_operation_buttons)
        self.division_button = self.create_button('/', 295, 90, 90, 60, style_of_math_operation_buttons)
        self.percentage_button = self.create_button('%', 200, 90, 90, 60, style_of_math_operation_buttons)
        self.esc_button = self.create_button('Esc', 105, 90, 90, 60, style_of_math_operation_buttons)
        self.ac_button = self.create_button('AC', 10, 90, 90, 60, style_of_math_operation_buttons)

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
        self.esc_button.clicked.connect(self.click_esc_button)
        self.ac_button.clicked.connect(self.click_ac_button)

        self.show()  # Show all the widgets.

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
        self.math_expression = f"{eval(self.math_expression)}"
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
        pass

    def click_esc_button(self):
        self.math_expression = self.math_expression.replace(f'{self.math_expression[-1]}', '')
        self.display.setText(self.math_expression)

    def click_ac_button(self):
        self.math_expression = ''
        self.display.setText(self.math_expression)
