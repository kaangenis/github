from PyQt5 import uic

with open('Sifre1_0.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('sifre_arayuz.ui', fout)