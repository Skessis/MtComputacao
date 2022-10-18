from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from sympy import Symbol

from Backend.bk_funcoes import valAendB_log, valAendB_expre
from Backend.bk_metodoPontoFixo import metPFixo
from template.tp_metMPF import Ui_MainWindow
import math
import timeit
x = Symbol('x')

class metMPF(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.but_calc.clicked.connect(self.lerVal)
        self.ui.but_clear.clicked.connect(self.clear)

    def lerVal(self):
        expr = self.ui.inp_expr_MPF.text()
        exprIt = self.ui.inp_exprItera_MPF.text()
        x0 = self.ui.inp_x0.text()
        e = self.ui.inp_e.text()
        N = self.ui.inp_N.text()

        fx = lambda x: eval(expr)
        wx = lambda x: eval(exprIt)

        start = timeit.default_timer()
        result = metPFixo(fx, wx, float(x0), float(e), int(N))
        stop = timeit.default_timer()
        execution_time = stop - start

        if result != 0:
            self.resultMatriz = result[0]
            self.ui.labelResult.setText("Raiz: "+str(float(round(result[1], 6))))
            self.ui.lblTempExib.setText(str(round(execution_time, 6)) + "s")

            print(str(float(round(result[1], 6))))
            print(self.resultMatriz)

            for row in (self.resultMatriz):
                self.ui.tableWidget.insertRow(0)
            for col in (self.resultMatriz[0]):
                self.ui.tableWidget.insertColumn(0)
            for rowNr, rowValue in enumerate(self.resultMatriz):
                for itemNr, itemValue in enumerate(rowValue):
                    print(rowNr, itemNr, self.resultMatriz[rowNr][itemNr])
                    self.ui.tableWidget.setItem(rowNr, itemNr, QtWidgets.QTableWidgetItem(self.resultMatriz[rowNr][itemNr]))
        else:
            self.ui.labelResult.setText("Não convergente.")

    def clear(self):
        self.ui.inp_expr_MPF.clear()
        self.ui.inp_x0.clear()
        self.ui.inp_e.clear()
        self.ui.inp_N.clear()
        self.ui.tableWidget.clear()
        self.ui.labelResult.clear()