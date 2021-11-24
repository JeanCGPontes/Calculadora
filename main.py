import classes
import sys


if __name__ == '__main__':
    application = classes.QtWidgets.QApplication(sys.argv)
    window = classes.MainWindow()
    sys.exit(application.exec_())
