import functions
from PyQt5 import QtWidgets, QtGui, QtCore


class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window_theme, self.number_button_style, self.style_of_math_operation_buttons, self.equal_button_style, self.label_style = functions.return_theme('light')
        self.label_font = functions.get_font("Century Gothic", False, 24)
        self.button_font = functions.get_font("Century Gothic", True, 14)

        self.setWindowTitle('Calculadora PyQt5')
        self.setGeometry(350, 200, 391, 490)
        self.setFixedSize(391, 490)
        self.setWindowIcon(QtGui.QIcon('images/calculator_icon.png'))
        self.setStyleSheet(self.window_theme)

        self.math_expression = ''

        self.display = self.create_label('', 5, 25, 382, 88, self.label_style)
        self.button_0 = self.create_button('0', 5, 398, 190, 68, self.number_button_style)
        self.button_1 = self.create_button('1', 5, 328, 94, 68, self.number_button_style)
        self.button_2 = self.create_button('2', 101, 328, 94, 68, self.number_button_style)
        self.button_3 = self.create_button('3', 197, 328, 94, 68, self.number_button_style)
        self.button_4 = self.create_button('4', 5, 258, 94, 68, self.number_button_style)
        self.button_5 = self.create_button('5', 101, 258, 94, 68, self.number_button_style)
        self.button_6 = self.create_button('6', 197, 258, 94, 68, self.number_button_style)
        self.button_7 = self.create_button('7', 5, 188, 94, 68, self.number_button_style)
        self.button_8 = self.create_button('8', 101, 188, 94, 68, self.number_button_style)
        self.button_9 = self.create_button('9', 197, 188, 94, 68, self.number_button_style)
        self.point_button = self.create_button('.', 197, 398, 94, 68, self.number_button_style)
        self.equal_button = self.create_button('=', 293, 398, 94, 68, self.equal_button_style)
        self.addition_button = self.create_button('+', 293, 328, 94, 68, self.style_of_math_operation_buttons)
        self.subtraction_button = self.create_button('-', 293, 258, 94, 68, self.style_of_math_operation_buttons)
        self.multiplication_button = self.create_button('*', 293, 188, 94, 68, self.style_of_math_operation_buttons)
        self.division_button = self.create_button('/', 293, 118, 94, 68, self.style_of_math_operation_buttons)
        self.percentage_button = self.create_button('%', 197, 118, 94, 68, self.style_of_math_operation_buttons)
        self.esc_button = self.create_button('Esc', 101, 118, 94, 68, self.style_of_math_operation_buttons)
        self.ac_button = self.create_button('AC', 5, 118, 94, 68, self.style_of_math_operation_buttons)

        self.button_0.clicked.connect(lambda: self.click_button('0'))
        self.button_1.clicked.connect(lambda: self.click_button('1'))
        self.button_2.clicked.connect(lambda: self.click_button('2'))
        self.button_3.clicked.connect(lambda: self.click_button('3'))
        self.button_4.clicked.connect(lambda: self.click_button('4'))
        self.button_5.clicked.connect(lambda: self.click_button('5'))
        self.button_6.clicked.connect(lambda: self.click_button('6'))
        self.button_7.clicked.connect(lambda: self.click_button('7'))
        self.button_8.clicked.connect(lambda: self.click_button('8'))
        self.button_9.clicked.connect(lambda: self.click_button('9'))
        self.point_button.clicked.connect(lambda: self.click_button('.'))
        self.equal_button.clicked.connect(self.click_equal_button)
        self.addition_button.clicked.connect(lambda: self.click_button('+'))
        self.subtraction_button.clicked.connect(lambda: self.click_button('-'))
        self.multiplication_button.clicked.connect(lambda: self.click_button('*'))
        self.division_button.clicked.connect(lambda: self.click_button('/'))
        self.percentage_button.clicked.connect(lambda: self.click_button('%'))
        self.esc_button.clicked.connect(self.click_esc_button)
        self.ac_button.clicked.connect(self.click_ac_button)

        self.initGUI()

        self.show()

    def initGUI(self):
        menu_bar = self.menuBar()
        menu_bar.setGeometry(0, 0, 391, 20)
        menu_bar.setFont(functions.get_font("Century Gothic", False, 10))
        menu_design = menu_bar.addMenu('&Tema')

        dark_theme_action = QtWidgets.QAction('Escuro', self)
        dark_theme_action.setFont(functions.get_font("Century Gothic", False, 10))
        light_theme_action = QtWidgets.QAction('Claro', self)
        light_theme_action.setFont(functions.get_font("Century Gothic", False, 10))

        menu_design.addAction(dark_theme_action)
        menu_design.addAction(light_theme_action)

        dark_theme_action.triggered.connect(lambda: self.set_theme('dark'))
        light_theme_action.triggered.connect(lambda: self.set_theme('light'))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_0: self.button_0.click()
        elif event.key() == QtCore.Qt.Key.Key_1: self.button_1.click()
        elif event.key() == QtCore.Qt.Key.Key_2: self.button_2.click()
        elif event.key() == QtCore.Qt.Key.Key_3: self.button_3.click()
        elif event.key() == QtCore.Qt.Key.Key_4: self.button_4.click()
        elif event.key() == QtCore.Qt.Key.Key_5: self.button_5.click()
        elif event.key() == QtCore.Qt.Key.Key_6: self.button_6.click()
        elif event.key() == QtCore.Qt.Key.Key_7: self.button_7.click()
        elif event.key() == QtCore.Qt.Key.Key_8: self.button_8.click()
        elif event.key() == QtCore.Qt.Key.Key_9: self.button_9.click()
        elif event.key() == QtCore.Qt.Key.Key_Delete: self.ac_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Backspace: self.esc_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Equal: self.equal_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Enter: self.equal_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Plus: self.addition_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Minus: self.subtraction_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Asterisk: self.multiplication_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Slash: self.division_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Percent: self.percentage_button.click()
        elif event.key() == QtCore.Qt.Key.Key_Period: self.point_button.click()

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

    def click_button(self, value: str):
        self.math_expression += value
        self.display.setText(self.math_expression)

    def click_equal_button(self):
        if '%' in self.math_expression:
            try:
                self.math_expression = str(functions.solve_percentage(self.math_expression))
                self.display.setText(self.math_expression)

            except ValueError:
                self.math_expression = ''
                self.display.setText(self.math_expression)

        else:
            try:
                self.math_expression = f"{eval(self.math_expression)}"
                self.display.setText(self.math_expression)

            except SyntaxError or ValueError:
                self.math_expression = ''
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

    def set_theme(self, theme):
        window_theme, number_button_style, style_of_math_operation_buttons, equal_button_style, label_style = functions.return_theme(theme)
        self.setStyleSheet(window_theme)
        self.button_0.setStyleSheet(number_button_style)
        self.button_1.setStyleSheet(number_button_style)
        self.button_2.setStyleSheet(number_button_style)
        self.button_3.setStyleSheet(number_button_style)
        self.button_4.setStyleSheet(number_button_style)
        self.button_5.setStyleSheet(number_button_style)
        self.button_6.setStyleSheet(number_button_style)
        self.button_7.setStyleSheet(number_button_style)
        self.button_8.setStyleSheet(number_button_style)
        self.button_9.setStyleSheet(number_button_style)
        self.point_button.setStyleSheet(number_button_style)
        self.ac_button.setStyleSheet(style_of_math_operation_buttons)
        self.esc_button.setStyleSheet(style_of_math_operation_buttons)
        self.percentage_button.setStyleSheet(style_of_math_operation_buttons)
        self.division_button.setStyleSheet(style_of_math_operation_buttons)
        self.multiplication_button.setStyleSheet(style_of_math_operation_buttons)
        self.subtraction_button.setStyleSheet(style_of_math_operation_buttons)
        self.addition_button.setStyleSheet(style_of_math_operation_buttons)
        self.equal_button.setStyleSheet(equal_button_style)
        self.display.setStyleSheet(label_style)

        self.update()
