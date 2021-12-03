from PyQt5.QtGui import QFont
import sqlite3


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


def return_theme(theme):
    if theme == 'dark':
        window_theme = ("""QMainWindow {background-color: rgb(21, 21, 21);}  
                           QMenuBar {background-color: rgb(21, 21, 21);
                                     color: rgb(255, 255, 255)}
                           QMenuBar::item{background-color: transparent}
                           QMenuBar::item:selected{background-color: rgb(206, 206, 206);
                                                   color: rgb(0, 0, 0)}
                           QMenu {background-color: rgb(255, 255, 255);
                                  color: rgb(0, 0, 0)}
                           QMenu::item:selected{background-color: rgb(225, 225, 225)}""")

        number_button_style = ("""QPushButton {background-color: rgb(206,206,206);
                                                       border-color: rgb(166, 166, 166);
                                                       border-width: 1px;
                                                       border-style:solid;
                                                       border-radius: 4;}
                                          QPushButton:hover {background-color: rgb(228, 228, 228)}""")

        style_of_math_operation_buttons = ("""QPushButton {background-color: rgb(96, 166, 111);
                                                                   border-color: rgb(166, 166, 166);
                                                                   border-width: 1px;
                                                                   border-style:solid;
                                                                   border-radius: 3;}
                                                      QPushButton:hover {background-color: rgb(96, 166, 111, 200)}""")

        equal_button_style = ("""QPushButton {background-color: rgb(107, 197, 107);
                                                      border-color: rgb(166, 166, 166);
                                                      border-width: 1px;
                                                      border-style: solid;
                                                      border-radius: 4;}
                                         QPushButton:hover {background-color: rgba(107, 197, 107, 200);}""")

        label_style = ("""color: rgb(206, 206, 206);
                                  background-color: rgb(23, 23, 23);    
                                  border-color: rgb(166, 166, 166);
                                  border-width: 1px;
                                  border-style:solid;
                                  border-radius: 3;""")

        return window_theme, number_button_style, style_of_math_operation_buttons, equal_button_style, label_style

    elif theme == 'light':
        window_theme = ("""QMainWindow {background-color: rgb(241, 244, 243)}  
                           QMenuBar {background-color: rgb(241, 244, 243)}
                           QMenuBar::item{background-color: transparent}
                           QMenuBar::item:selected{background-color: rgb(255, 255, 255)}
                           QMenu {background-color: rgb(255, 255, 255);
                                  color: rgb(0, 0, 0)}
                           QMenu::item:selected{background-color: rgb(225, 225, 225)}""")

        number_button_style = ("""QPushButton {background-color: rgb(255, 255, 255);
                                               border-color: rgb(166, 166, 166);
                                               border-width: 1px;
                                               border-style:solid;
                                               border-radius: 3;}
                            QPushButton:hover {background-color: rgb(235, 235, 235)}
                         QPushButton:pressed  {background-color: rgb(235, 235, 235)}""")

        style_of_math_operation_buttons = ("""QPushButton {background-color: rgba(13, 202, 174, 168);
                                                           border-color: rgb(166, 166, 166);
                                                           border-width: 1px;
                                                           border-style:solid;
                                                           border-radius: 3;}
                                        QPushButton:hover {background-color: rgb(13, 202, 174, 200)}""")

        equal_button_style = ("""QPushButton {background-color: rgba(0, 135, 159, 180);
                                              border-color: rgb(166, 166, 166);
                                              border-width: 1px;
                                              border-style: solid;
                                              border-radius: 3;}
                           QPushButton:hover {background-color: rgba(0, 135, 159, 200);}""")

        label_style = ("""background-color: rgb(252, 252, 252);
                          border-color: rgb(166, 166, 166);
                          border-width: 1px;
                          border-style:solid;
                          border-radius: 3;""")

        return window_theme, number_button_style, style_of_math_operation_buttons, equal_button_style, label_style

    else:
        window_theme = ("""QMainWindow {background-color: rgb(241, 244, 243)}  
                                  QMenuBar {background-color: rgb(241, 244, 243)}
                                  QMenuBar::item{background-color: transparent}
                                  QMenuBar::item:selected{background-color: rgb(255, 255, 255)}
                                  QMenu {background-color: rgb(255, 255, 255);
                                         color: rgb(0, 0, 0)}
                                  QMenu::item:selected{background-color: rgb(225, 225, 225)}""")

        number_button_style = ("""QPushButton {background-color: rgb(255, 255, 255);
                                                               border-color: rgb(166, 166, 166);
                                                               border-width: 1px;
                                                               border-style:solid;
                                                               border-radius: 3;}

                                                  QPushButton:hover {background-color: rgb(235, 235, 235)}

                                                  QPushButton:pressed {{background-color: rgb(235, 235, 235)}}""")

        style_of_math_operation_buttons = ("""QPushButton {background-color: rgba(13, 202, 174, 168);
                                                                           border-color: rgb(166, 166, 166);
                                                                           border-width: 1px;
                                                                           border-style:solid;
                                                                           border-radius: 3;}

                                                              QPushButton:hover {background-color: rgb(13, 202, 174, 200)}""")

        equal_button_style = ("""QPushButton {background-color: rgba(0, 135, 159, 180);
                                                 border-color: rgb(166, 166, 166);
                                                 border-width: 1px;
                                                 border-style: solid;
                                                 border-radius: 3;}

                                                 QPushButton:hover {background-color: rgba(0, 135, 159, 200);}""")

        label_style = ("""background-color: rgb(252, 252, 252);
                                          border-color: rgb(166, 166, 166);
                                          border-width: 1px;
                                          border-style:solid;
                                          border-radius: 3;""")

        return window_theme, number_button_style, style_of_math_operation_buttons, equal_button_style, label_style


def connect_database(database_name: str):
    database = sqlite3.connect(database_name)
    return database


def close_database(database):
    database.close()


def set_cursor(database):
    cursor = database.cursor()
    return cursor


def insert_values(cursor, math_expression: str, result: str):
    cursor.execute(f"INSERT INTO historic (math_expression, result) VALUES ('{math_expression}', '{result}')")


def commit(database):
    database.commit()


def get_math_expressions(cursor):
    cursor.execute(f"SELECT math_expression FROM historic")
    values = cursor.fetchall()
    return values


def get_results(cursor):
    cursor.execute(f"SELECT result FROM historic")
    values = cursor.fetchall()
    return values


def delete_all_data(cursor):
    cursor.execute("DELETE FROM historic")
