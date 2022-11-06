#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:40:05 2022

@author: kaangenis
"""

#-----------------------Kütüphane-----------------------#
#-------------------------------------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaSayfaDeneme import *

#-----------------------Uygulama------------------------#
#-------------------------------------------------------#

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()



#-----------------------VeriTabani----------------------#
#-------------------------------------------------------#

import sqlite3
global curs
global conn
conn = sqlite3.connect('projedb.db')
curs = conn.cursor()
sorguCreTblSpor = ("CREATE TABLE IF NOT EXISTS Sporcu_Liste(                  \
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,             \
                   TcNo TEXT NOT NULL UNIQUE,                                 \
                   SporcuAdi TEXT NOT NULL,                                   \
                   SporcuSoyadi TEXT NOT NULL,                                \
                   KulupAdi TEXT NOT NULL,                                    \
                   Brans TEXT NOT NULL,                                       \
                   Cinsiyet TEXT NOT NULL,                                    \
                   DogumTarihi TEXT NOT NULL,                                 \
                   MedeniHal TEXT NOT NULL,                                   \
                   Kilo TEXT NOT NULL,                                        \
                   Boy TEXT NOT NULL)")
    
curs.execute(sorguCreTblSpor)
conn.commit()


#-----------------------Kaydetme------------------------#
#-------------------------------------------------------#

def EKLE():
    _lneTCK = ui.line_TCK.text()
    _lneSporcuAdi = ui.line_Name.text()
    _lneSporcuSoyadi = ui.line_Surname.text()
    _cmbSporKulubu = ui.cmbx_Club.currentText()
    _lwBrans = ui.listWidget_2.currentItem().text()
    _cmbCinsiyet = ui.cmbx_Gender.currentText()
    _cwDTarihi = ui.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
    
    if ui.chckbx_IsMaried.isChecked():
        _medeniHal = "Evli"
    else:
        _medeniHal = "Bekar"
        
    _spnKilo = ui.spbx_Kg.value()
    _spnBoy = ui.spbx_Height.value()
    

    curs.execute("INSERT INTO Sporcu_Liste \
                        (TcNo, SporcuAdi, SporcuSoyadi, KulupAdi, Brans, Cinsiyet, DogumTarihi, MedeniHal, Kilo, Boy) \
                        VALUES (?,?,?,?,?,?,?,?,?,?)", 
                        (_lneTCK, _lneSporcuAdi, _lneSporcuSoyadi, _cmbSporKulubu, _lwBrans, _cmbCinsiyet, _cwDTarihi, _medeniHal, _spnKilo, _spnBoy))
    conn.commit()
    
    LISTELE()
    
#-----------------------Listele-------------------------#
#-------------------------------------------------------#

def LISTELE():
    ui.tblw_Bilgiler.clear()
    ui.tblw_Bilgiler.setHorizontalHeaderLabels(('NO:', 'TCKN: ', 'Sporcu Adı: ', 'Sporcu Soyadı: ', 'Kulüp Adı: ', 'Branş: ', 'Cinsiyet: ', 'Doğum Tarihi', 'Medeni Hal: ', 'Kilo: ', 'Boy: '))
    ui.tblw_Bilgiler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM Sporcu_Liste")
    
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tblw_Bilgiler.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))


LISTELE()


        
#-----------------------ÇIKIŞ------------------------------#
#----------------------------------------------------------#
        


#-----------------------Signal-Slot------------------------#
#----------------------------------------------------------#
ui.button_Ekle.clicked.connect(EKLE)
ui.button_Liste.clicked.connect(LISTELE)





sys.exit(Uygulama.exec_())


