#-----------------------Kütüphane-----------------------#
#-------------------------------------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Arayuz_1_1 import *


#-----------------------Uygulama------------------------#
#-------------------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


#-----------------------Fonksiyonlar------------------------#
#-----------------------------------------------------------#
def SAYILAR():
    print("None")




#-----------------------Buttons-----------------------------#
#-----------------------------------------------------------#
ui.btn_0.clicked.connect(SAYILAR)


#-----------------------END-----------------------------#
#-------------------------------------------------------#

sys.exit(Uygulama.exec_())