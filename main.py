from PyQt6 import QtWidgets
import window


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = window.Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
