from PyQt5 import uic

with open('logo.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('test.qrc', fout)