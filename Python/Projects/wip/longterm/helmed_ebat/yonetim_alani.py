#-----------------------Kütüphane-----------------------#
#-------------------------------------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Arayuz_1_3 import *


#-----------------------Uygulama------------------------#
#-------------------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


#-----------------------Fonksiyonlar------------------------#
#-----------------------------------------------------------#

def TEMIZLE():
    ui.en.clear()
    ui.boy.clear()
    ui.sonuc_alan.clear()

TEMIZLE()

def ALANHESAPLA():
    def_en = ui.en.value()
    def_boy = ui.boy.value()

    formul = (def_en * def_boy)/10000

    ui.sonuc_alan.setText(str(formul) + " m²")


def BELIRLE():
    ui.comboBox.setItemData(0, 360)

BELIRLE()

def HESAPLA():
    print(ui.comboBox.currentData() * 2)


def CIKIS():
    sys.exit(Uygulama.exec_())

#-----------------------Buttons-------------------------#
#-------------------------------------------------------#

ui.btn_H_Alan.clicked.connect(ALANHESAPLA)
ui.btn_Hesapla.clicked.connect(HESAPLA)
ui.btn_Sifirla.clicked.connect(TEMIZLE)
ui.btn_Cikis.clicked.connect(CIKIS)

#-----------------------END-----------------------------#
#-------------------------------------------------------#

sys.exit(Uygulama.exec_())
