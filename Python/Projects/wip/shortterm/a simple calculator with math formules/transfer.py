from PyQt5 import uic

with open('Arayuz_1_1.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('hesapui.ui', fout)