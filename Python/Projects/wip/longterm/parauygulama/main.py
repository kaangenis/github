#-----------------------Kütüphane-----------------------#
#-------------------------------------------------------#

import sys
from PyQt5 import QtWidgets
from Sifre1_0 import *
from PyQt5.QtWidgets import *
from Anasayfa1_0 import *


#-----------------------Uygulama------------------------#
#-------------------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()



#-----------------------Fonksiyonlar------------------------#
#-----------------------------------------------------------#


dict_1 = {

    "username1": "kaangenis",
    "password1": "12345678",
    "username2": "ramazanduran",
    "password2": "87654321",
    "username3": "tunakarakose",
    "password3": "31313131"

}

hidden_answers = {

    "kaangenis": "patateskofte",
    "ramazanduran": "gitargitar",
    "tunakarakose": "birabira"


}

def LINK():
    check_1 = ui.line_nickname.text()
    check_2 = ui.line_password.text()
    if (check_1 == dict_1["username1"] and check_2 == dict_1["password1"]) or (check_1 == dict_1["username2"] and check_2 == dict_1["password2"]) or (check_1 == dict_1["username3"] and check_2 == dict_1["password3"]):
        ui.line_check.setText("Giriş İşlemi Başarılı")
    else:
        ui.line_check.setText("Giriş İşlemi Başarısız")


def PASSWORDCHANGE():
    print("Zort")


def INFOCHECK():
    print("zort1")





#-----------------------Buttons-----------------------------#
#-----------------------------------------------------------#
ui.btn_giris.clicked.connect(LINK)
ui.btn_sifresifirla.clicked.connect(PASSWORDCHANGE)


#-----------------------END-----------------------------#
#-------------------------------------------------------#

sys.exit(Uygulama.exec_())