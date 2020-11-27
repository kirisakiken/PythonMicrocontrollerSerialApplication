# @author : Bezmican Zehir | LinkedIn: bezmicanzehir | IG: @bayonuc
# This file converts .ui to .py
from PyQt5 import uic

with open('my_py.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('my_ui.ui', fout)
