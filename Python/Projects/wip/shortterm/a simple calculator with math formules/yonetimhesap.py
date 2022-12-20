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
l1 = []

#-----------------------Fonksiyonlar------------------------#
#-----------------------------------------------------------#
def btn_Sifir():
    ui.btn_0.x = 0
    print(ui.btn_0.x)
    ui.sonuc.insert(str(ui.btn_0.x))

def btn_Bir():
    ui.btn_1.x = 1
    print(ui.btn_1.x)
    ui.sonuc.insert(str(ui.btn_1.x))

def btn_Iki():
    ui.btn_2.x = 2
    print(ui.btn_2.x)
    ui.sonuc.insert(str(ui.btn_2.x))

def btn_Uc():
    ui.btn_3.x = 3
    print(ui.btn_3.x)
    ui.sonuc.insert(str(ui.btn_3.x))

def btn_Dort():
    ui.btn_4.x = 4
    print(ui.btn_4.x)
    ui.sonuc.insert(str(ui.btn_4.x))

def btn_Bes():
    ui.btn_5.x = 5
    print(ui.btn_5.x)
    ui.sonuc.insert(str(ui.btn_5.x))

def btn_Alti():
    ui.btn_6.x = 6
    print(ui.btn_6.x)
    ui.sonuc.insert(str(ui.btn_6.x))

def btn_Yedi():
    ui.btn_7.x = 7
    print(ui.btn_7.x)
    ui.sonuc.insert(str(ui.btn_7.x))

def btn_Sekiz():
    ui.btn_8.x = 8
    print(ui.btn_8.x)
    ui.sonuc.insert(str(ui.btn_8.x))

def btn_Dokuz():
    ui.btn_9.x = 9
    print(ui.btn_9.x)
    ui.sonuc.insert(str(ui.btn_9.x))

def data():
    l1.append(int(ui.sonuc.text()))
    print(l1)

def temizle():
    ui.sonuc.clear()

def toplaSonuc():
    l1.append(int(ui.sonuc.text()))
    esittir = l1[-1] + l1[-2]
    print(esittir)
    ui.sonuc.clear()
    ui.sonuc.insert(str(esittir))

def cikartSonuc():
    l1.append(int(ui.sonuc.text()))
    esittir = l1[-1] - l1[-2]
    print(esittir)
    ui.sonuc.clear()
    ui.sonuc.insert(str(esittir))

def carpmaSonuc():
    l1.append(int(ui.sonuc.text()))
    esittir = l1[-1] * l1[-2]
    print(esittir)
    ui.sonuc.clear()
    ui.sonuc.insert(str(esittir))

def bolmeSonuc():
    l1.append(int(ui.sonuc.text()))
    esittir = l1[-1] / l1[-2]
    print(esittir)
    ui.sonuc.clear()
    ui.sonuc.insert(str(esittir))

#-----------------------Buttons-----------------------------#
#-----------------------------------------------------------#
ui.btn_0.clicked.connect(btn_Sifir)
ui.btn_1.clicked.connect(btn_Bir)
ui.btn_2.clicked.connect(btn_Iki)
ui.btn_3.clicked.connect(btn_Uc)
ui.btn_4.clicked.connect(btn_Dort)
ui.btn_5.clicked.connect(btn_Bes)
ui.btn_6.clicked.connect(btn_Alti)
ui.btn_7.clicked.connect(btn_Yedi)
ui.btn_8.clicked.connect(btn_Sekiz)
ui.btn_9.clicked.connect(btn_Dokuz)

ui.btn_topla.clicked.connect(data)
ui.btn_topla.clicked.connect(temizle)
ui.btn_sil.clicked.connect(toplaSonuc)

ui.btn_cikar.clicked.connect(data)
ui.btn_cikar.clicked.connect(temizle)
ui.btn_sil.clicked.connect(cikartSonuc)

ui.btn_carp.clicked.connect(data)
ui.btn_carp.clicked.connect(temizle)
ui.btn_sil.clicked.connect(carpmaSonuc)

ui.btn_bolme.clicked.connect(data)
ui.btn_bolme.clicked.connect(temizle)
ui.btn_sil.clicked.connect(bolmeSonuc)


#-----------------------END-----------------------------#
#-------------------------------------------------------#

sys.exit(Uygulama.exec_())