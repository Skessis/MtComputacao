from PyQt5.QtWidgets import  QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import sys, os

from Backend.bk_funcoes import valAendB_log, valAendB_expre
from Backend.bk_metodoBissecao import bissecao
from template.tp_metBissecao import Ui_MetBissecao
import math
import timeit

class metBissecao(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MetBissecao()
        self.ui.setupUi(self)

        self.ui.but_calc.clicked.connect(self.lerVal)
        self.ui.but_clear.clicked.connect(self.clear)

        self.ui.radioButton.toggled.connect(self.selectStatusManual)
        self.ui.radioButton_2.toggled.connect(self.selectStatusAutomatico)

    def selectStatusManual(self):
        self.ui.lineEdit_valA.setEnabled(True)
        self.ui.lineEdit_valA_2.setEnabled(True)
        #print("Manual")

    def selectStatusAutomatico(self):        
        self.ui.lineEdit_valA.setEnabled(False)
        self.ui.lineEdit_valA_2.setEnabled(False)
        #print("Automatico")

    def lerVal (self):
        a = 0
        b = 0
        exprBiss = self.ui.inp_expr_Biss.text()
        tolBiss = self.ui.inp_tolBiss.text()

        fBissecao = lambda x: eval(exprBiss)
        
        if self.ui.radioButton.isChecked() == True:
            a = float(self.ui.lineEdit_valA.text())
            b = float(self.ui.lineEdit_valA_2.text())
        
        if self.ui.radioButton_2.isChecked() == True:
            if 'log' in exprBiss:
                val_log = valAendB_log(fBissecao)
                a = val_log[0]
                b = val_log[1]
            else:
                val_expre = valAendB_expre(fBissecao)
                a = val_expre[0]
                b = val_expre[1]

        start = timeit.default_timer()
        resultBissecao = bissecao(fBissecao, float(a), float(b), float(tolBiss))
        stop = timeit.default_timer()
        execution_time = stop - start

        self.resultMatriz = resultBissecao[0]
        raizBissecao = resultBissecao[1]
        k = resultBissecao[2]

        self.ui.labelResult.setText("\nO ponto é: "+ str(float(round(raizBissecao, 6))))
        self.ui.lblTempExib.setText(str(round(execution_time, 4)) + "s")

        for row in (self.resultMatriz):
            self.ui.tableWidget.insertRow(0)
        for col in (self.resultMatriz[0]):
            self.ui.tableWidget.insertColumn(0)
        for rowNr, rowValue in enumerate(self.resultMatriz):
            for itemNr, itemValue in enumerate(rowValue):
                print(rowNr, itemNr, self.resultMatriz[rowNr][itemNr])
                self.ui.tableWidget.setItem(rowNr, itemNr, QtWidgets.QTableWidgetItem(self.resultMatriz[rowNr][itemNr]))


    def clear(self):
        self.ui.inp_expr_Biss.setText("")
        self.ui.inp_tolBiss.setText("")
        self.ui.tableWidget.clear()
        self.ui.labelResult.setText("")
