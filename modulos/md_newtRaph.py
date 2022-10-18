from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableView, QWidget, QTableWidgetItem
from template.tp_metNewRaph import  Ui_metNewRaph
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout

#from Backend.bk_funcoes import calculaDerivada
from Backend.bk_metodoNewtonRaphson_V2 import newton

import math 
import time
import timeit

import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

class newtRaphWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_metNewRaph()
        self.ui.setupUi(self)

        self.ui.but_calc.clicked.connect(self.calcMetNewt)
        self.ui.but_clear.clicked.connect(self.clear)
        

    def calcMetNewt(self):
        expr = self.ui.inp_expr.text()
        x0 = self.ui.inp_x0.text()
        erro = self.ui.inp_erro.text()
        iter = self.ui.inp_itera.text()
        f = lambda x: eval(expr)


        start = timeit.default_timer()
        resultado = newton(f, float(x0),float(erro), int(iter))
        stop = timeit.default_timer()
        execution_time = stop - start



        self.resultMatriz = resultado[0]
        resultRaiz = resultado[1]
        k = resultado[2]

        self.ui.labelResult.setText("\nO ponto é: " + str(round(resultRaiz, 6)))
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
        self.ui.inp_expr.clear()
        self.ui.inp_erro.clear()
        self.ui.inp_x0.clear()
        self.ui.inp_itera.clear()

        self.ui.tableWidget.clear()
        self.ui.labelResult.clear()
        self.ui.lblTempExib.clear()

