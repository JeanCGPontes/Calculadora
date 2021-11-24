from PyQt5.QtGui import QFont


def get_font(font_name: str, bold: bool, font_size: int):
    font = QFont()
    font.setFamily(font_name)
    font.setBold(bold)
    font.setPointSize(font_size)
    return font


def solve_percentage(math_expression):
    operator_location = math_expression.find('%')
    number_1 = int(math_expression[0:operator_location])
    number_2 = int(math_expression[operator_location+1:len(math_expression)])
    result = (number_1 * number_2)/100
    return result
