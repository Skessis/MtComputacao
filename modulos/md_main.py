from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import sys, os

from template.tem_main import Ui_MainWindow
from modulos.md_newtRaph import newtRaphWindow
from modulos.md_metBis import metBissecao
from modulos.md_MFP import metMFP
from modulos.md_MetPF import metMPF


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bnt_next.clicked.connect(self.next)

    def next(self):
        index = self.ui.comboSelectItem.currentText()

        if str(index) == "Método Newton Raphson":
            self.telaNewt = newtRaphWindow()
            self.telaNewt.show()
        if str(index) == "Método Bisseção":
            self.telaBiss = metBissecao()
            self.telaBiss.show()
        if str(index) == "Método Posição Falsa":
            self.telaMFP = metMFP()
            self.telaMFP.show()
        if str(index) == "Método Iterativo Linear":
            self.telaMPF = metMPF()
            self.telaMPF.show()
