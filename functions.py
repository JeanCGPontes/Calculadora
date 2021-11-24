from PyQt5.QtGui import QFont


def get_font(font_name: str, bold: bool, font_size: int):
    font = QFont()
    font.setFamily(font_name)
    font.setBold(bold)
    font.setPointSize(font_size)
    return font
