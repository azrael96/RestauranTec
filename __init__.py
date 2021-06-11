import sys
import InterfaceManager as Window

from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window.generarMain()
    sys.exit(app.exec_())
