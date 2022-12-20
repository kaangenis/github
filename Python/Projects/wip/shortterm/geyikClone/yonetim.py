import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from main import *

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

















sys.exit(Uygulama.exec_())