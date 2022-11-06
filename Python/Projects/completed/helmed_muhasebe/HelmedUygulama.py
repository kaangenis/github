#-----------------------Kütüphane-----------------------#
#-------------------------------------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfa7_4 import *


#-----------------------Uygulama------------------------#
#-------------------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_Helmed()
ui.setupUi(penAna)
penAna.show()


#-----------------------Fonksiyonlar------------------------#
#-----------------------------------------------------------#

def K_TEMIZLE():
    ui.agirlik.clear()
    ui.kgspn.clear()
    ui.uzunlukspn.clear()
    ui.fiyat_sonuc.clear()

K_TEMIZLE()


#-----------------------KG'DEN ADET FİYATI------------------------#
#-----------------------------------------------------------------#

#KG >> ADET = ((METRE * AGIRLIK) /1000) * UZUNLUK

def K_LISTELE():
    deger = ui.olcu
    deger.setItemData(0, 120)
    deger.setItemData(1, 140)
    deger.setItemData(2, 130)
    deger.setItemData(3, 160)
    deger.setItemData(4, 155)
    deger.setItemData(5, 170)
    deger.setItemData(6, 200)
    deger.setItemData(7, 230)
    deger.setItemData(8, 210)
    deger.setItemData(9, 230)
    deger.setItemData(10, 260)
    deger.setItemData(11, 295)
    deger.setItemData(12, 210)
    deger.setItemData(13, 260)
    deger.setItemData(14, 300)
    deger.setItemData(15, 325)
    deger.setItemData(16, 350)
    deger.setItemData(17, 240)
    deger.setItemData(18, 310)
    deger.setItemData(19, 370)
    deger.setItemData(20, 400)
    deger.setItemData(21, 430)
    deger.setItemData(22, 460)
    deger.setItemData(23, 230)
    deger.setItemData(24, 350)
    deger.setItemData(25, 370)
    deger.setItemData(26, 520)
    deger.setItemData(27, 360)
    deger.setItemData(28, 690)
    deger.setItemData(29, 400)
    deger.setItemData(30, 440)
    deger.setItemData(31, 740)
    deger.setItemData(32, 170)
    deger.setItemData(33, 180)
    deger.setItemData(34, 210)
    deger.setItemData(35, 240)
    deger.setItemData(36, 220)
    deger.setItemData(37, 240)
    deger.setItemData(38, 270)
    deger.setItemData(39, 310)
    deger.setItemData(40, 220)
    deger.setItemData(41, 270)
    deger.setItemData(42, 310)
    deger.setItemData(43, 335)
    deger.setItemData(44, 365)
    deger.setItemData(45, 250)
    deger.setItemData(46, 320)
    deger.setItemData(47, 385)
    deger.setItemData(48, 415)
    deger.setItemData(49, 445)
    deger.setItemData(50, 480)
    deger.setItemData(51, 360)
    deger.setItemData(52, 530)








    ui.agirlik.setText(str(ui.olcu.currentData()))

K_LISTELE()

def K_HESAPLA():

    kgdeger = ((int(ui.agirlik.text()) * ui.kgspn.value()) /100000000) * ui.uzunlukspn.value()
    ui.fiyat_sonuc.setText(str(kgdeger) + " TL")


def KAPAT():
    sys.exit(Uygulama.exec_())



#-----------------------ADET'DEN KG FİYATI------------------------#
#-----------------------------------------------------------------#

def A_TEMIZLE():
    ui.fiyat_sonuc_3.clear()
    ui.uzunlukspn_3.clear()
    ui.adet_fiyat.clear()

A_TEMIZLE()


def A_LISTELE():
    deger_2 = ui.olcu_3
    deger_2.setItemData(0, 120)
    deger_2.setItemData(1, 140)
    deger_2.setItemData(2, 130)
    deger_2.setItemData(3, 160)
    deger_2.setItemData(4, 155)
    deger_2.setItemData(5, 170)
    deger_2.setItemData(6, 200)
    deger_2.setItemData(7, 230)
    deger_2.setItemData(8, 210)
    deger_2.setItemData(9, 230)
    deger_2.setItemData(10, 260)
    deger_2.setItemData(11, 295)
    deger_2.setItemData(12, 210)
    deger_2.setItemData(13, 260)
    deger_2.setItemData(14, 300)
    deger_2.setItemData(15, 325)
    deger_2.setItemData(16, 350)
    deger_2.setItemData(17, 240)
    deger_2.setItemData(18, 310)
    deger_2.setItemData(19, 370)
    deger_2.setItemData(20, 400)
    deger_2.setItemData(21, 430)
    deger_2.setItemData(22, 460)
    deger_2.setItemData(23, 230)
    deger_2.setItemData(24, 350)
    deger_2.setItemData(25, 370)
    deger_2.setItemData(26, 520)
    deger_2.setItemData(27, 360)
    deger_2.setItemData(28, 690)
    deger_2.setItemData(29, 400)
    deger_2.setItemData(30, 440)
    deger_2.setItemData(31, 740)
    deger_2.setItemData(32, 170)
    deger_2.setItemData(33, 180)
    deger_2.setItemData(34, 210)
    deger_2.setItemData(35, 240)
    deger_2.setItemData(36, 220)
    deger_2.setItemData(37, 240)
    deger_2.setItemData(38, 270)
    deger_2.setItemData(39, 310)
    deger_2.setItemData(40, 220)
    deger_2.setItemData(41, 270)
    deger_2.setItemData(42, 310)
    deger_2.setItemData(43, 335)
    deger_2.setItemData(44, 365)
    deger_2.setItemData(45, 250)
    deger_2.setItemData(46, 320)
    deger_2.setItemData(47, 385)
    deger_2.setItemData(48, 415)
    deger_2.setItemData(49, 445)
    deger_2.setItemData(50, 480)
    deger_2.setItemData(51, 360)
    deger_2.setItemData(52, 530)

    ui.adet_agirlik.setText(str(ui.olcu_3.currentData()))

A_LISTELE()

#KG Fiyat = ((Adet Fiyatı * 1000) / Uzunluk) / Metre Ağırlığı
#Örnek = (5,0 * 1000 / 200) / 320

def A_HESAPLA():
    if  ui.uzunlukspn_3.value() == 0:
        ui.fiyat_sonuc_3.setText("Boş")

    elif ui.adet_fiyat.text() == "":
        ui.fiyat_sonuc_3.setText("Boş")

    else:
        adet_deger = ((float(ui.adet_fiyat.text()) * 100000) / ui.uzunlukspn_3.value()) / int(ui.adet_agirlik.text())

        adet_deger = round(adet_deger,3)

        ui.fiyat_sonuc_3.setText(str((adet_deger)) + " TL")





#-----------------------Buttons-------------------------#
#-------------------------------------------------------#

ui.btn_hesapla.clicked.connect(K_HESAPLA)
ui.btn_sifirla.clicked.connect(K_TEMIZLE)
ui.btn_cikis.clicked.connect(KAPAT)

ui.btn_cikis_3.clicked.connect(KAPAT)
ui.btn_sifirla_3.clicked.connect(A_TEMIZLE)
ui.btn_hesapla_3.clicked.connect(A_HESAPLA)

ui.olcu.currentTextChanged.connect(K_LISTELE)
ui.olcu_3.currentTextChanged.connect(A_LISTELE)





#-----------------------END-----------------------------#
#-------------------------------------------------------#

sys.exit(Uygulama.exec_())
