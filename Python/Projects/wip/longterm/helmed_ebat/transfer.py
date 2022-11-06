from PyQt5 import uic

with open('Arayuz_1_3.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('arayuz.ui', fout)