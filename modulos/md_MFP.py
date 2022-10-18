from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from sympy import Symbol

from Backend.bk_funcoes import valAendB_log, valAendB_expre
from Backend.bk_metodoFalsaPosicao import MFPosicao
from template.tp_metMFP import Ui_MetFP
import math
import timeit
x = Symbol('x')
class metMFP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MetFP()
        self.ui.setupUi(self)

        self.ui.but_calc.clicked.connect(self.lerVal)
        self.ui.but_clear.clicked.connect(self.clear)

        self.ui.radioButton.toggled.connect(self.selectStatusManual)
        self.ui.radioButton_2.toggled.connect(self.selectStatusAutomatico)

    def selectStatusManual(self):
        self.ui.lineEdit_valA.setEnabled(True)
        self.ui.lineEdit_valB.setEnabled(True)
        # print("Manual")

    def selectStatusAutomatico(self):
        self.ui.lineEdit_valA.setEnabled(False)
        self.ui.lineEdit_valB.setEnabled(False)
        # print("Automatico")

    def lerVal(self):
        a = 0
        b = 0
        exprMPF = self.ui.inp_expr_MPF.text()
        tolMPF = self.ui.inp_tolMPF.text()
        itr = self.ui.inp_itr.text()

        fBMPF = lambda x: eval(exprMPF)

        if self.ui.radioButton.isChecked() == True:
            a = float(self.ui.lineEdit_valA.text())
            b = float(self.ui.lineEdit_valB.text())

        if self.ui.radioButton_2.isChecked() == True:
            if 'log' in exprMPF:
                val_log = valAendB_log(fBMPF)
                a = val_log[0]
                b = val_log[1]
            else:
                val_expre = valAendB_expre(fBMPF)
                a = val_expre[0]
                b = val_expre[1]

        start = timeit.default_timer()
        resultMatrizMPF = MFPosicao(fBMPF, float(a), float(b), float(tolMPF), float(itr))
        stop = timeit.default_timer()
        execution_time = stop - start

        self.resultMatriz = resultMatrizMPF[0]
        raizMPF = resultMatrizMPF[1]

        self.ui.labelResult.setText(
            "valor de A: " + str(round(a, 6)) + "\nvalor de B: " + str(round(b, 6)) + "\nO ponto é: " + str(
                float(round(raizMPF, 6))))
        self.ui.lblTempExib.setText(str(round(execution_time, 6)) + "s")

        for row in (self.resultMatriz):
            self.ui.tableWidget.insertRow(0)
        for col in (self.resultMatriz[0]):
            self.ui.tableWidget.insertColumn(0)
        for rowNr, rowValue in enumerate(self.resultMatriz):
            for itemNr, itemValue in enumerate(rowValue):
                print(rowNr, itemNr, self.resultMatriz[rowNr][itemNr])
                self.ui.tableWidget.setItem(rowNr, itemNr, QtWidgets.QTableWidgetItem(self.resultMatriz[rowNr][itemNr]))

    def clear(self):
        self.ui.inp_expr_MPF.clear()
        self.ui.inp_tolMPF.clear()
        self.ui.inp_itr.clear()

        self.ui.tableWidget.clear()
        self.ui.labelResult.clear()
        self.ui.lblTempExib.clear()