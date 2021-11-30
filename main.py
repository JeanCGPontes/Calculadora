import classes
import sys


if __name__ == '__main__':
    app = classes.QtWidgets.QApplication(sys.argv)
    window = classes.Calculator()
    sys.exit(app.exec_())
