# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_metMPontoFixo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 605)
        MainWindow.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(20, 480, 611, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelResult.setFont(font)
        self.labelResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelResult.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 38, 38);")
        self.labelResult.setText("")
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.but_calc = QtWidgets.QPushButton(self.centralwidget)
        self.but_calc.setGeometry(QtCore.QRect(350, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.but_calc.setFont(font)
        self.but_calc.setStyleSheet("color: rgb(255, 255, 255);")
        self.but_calc.setObjectName("but_calc")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 300, 611, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(38, 38, 38);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 270, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.but_clear = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear.setGeometry(QtCore.QRect(170, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.but_clear.setFont(font)
        self.but_clear.setStyleSheet("color: rgb(255, 255, 255);")
        self.but_clear.setObjectName("but_clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 550, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lblTempExib = QtWidgets.QLabel(self.centralwidget)
        self.lblTempExib.setGeometry(QtCore.QRect(550, 550, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTempExib.setFont(font)
        self.lblTempExib.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblTempExib.setText("")
        self.lblTempExib.setObjectName("lblTempExib")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 150, 111, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.inp_N = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_N.setGeometry(QtCore.QRect(440, 150, 167, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_N.setFont(font)
        self.inp_N.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_N.setObjectName("inp_N")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(21, 180, 36, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.inp_x0 = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_x0.setGeometry(QtCore.QRect(123, 145, 167, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_x0.setFont(font)
        self.inp_x0.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_x0.setObjectName("inp_x0")
        self.inp_exprItera_MPF = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_exprItera_MPF.setGeometry(QtCore.QRect(154, 110, 461, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_exprItera_MPF.setFont(font)
        self.inp_exprItera_MPF.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_exprItera_MPF.setInputMask("")
        self.inp_exprItera_MPF.setText("")
        self.inp_exprItera_MPF.setObjectName("inp_exprItera_MPF")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(21, 145, 23, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(21, 110, 127, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.inp_expr_MPF = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_expr_MPF.setGeometry(QtCore.QRect(92, 75, 521, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_expr_MPF.setFont(font)
        self.inp_expr_MPF.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_expr_MPF.setInputMask("")
        self.inp_expr_MPF.setText("")
        self.inp_expr_MPF.setObjectName("inp_expr_MPF")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 75, 65, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.inp_e = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_e.setGeometry(QtCore.QRect(123, 180, 167, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_e.setFont(font)
        self.inp_e.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_e.setText("")
        self.inp_e.setObjectName("inp_e")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but_calc.setText(_translate("MainWindow", "Calcular"))
        self.label_6.setText(_translate("MainWindow", "Resultado:"))
        self.but_clear.setText(_translate("MainWindow", "Limpar"))
        self.label.setText(_translate("MainWindow", "Método Iterativo Linear"))
        self.label_7.setText(_translate("MainWindow", "Execução:"))
        self.label_8.setText(_translate("MainWindow", "Max. Iterações:"))
        self.inp_N.setPlaceholderText(_translate("MainWindow", "Ex.: 100 | 1000"))
        self.label_4.setText(_translate("MainWindow", "Erro:"))
        self.inp_x0.setPlaceholderText(_translate("MainWindow", "Ex.: 0.5 | 1"))
        self.inp_exprItera_MPF.setPlaceholderText(_translate("MainWindow", "Ex.: 2*x**2 + x + 1 | x + log10(x)"))
        self.label_3.setText(_translate("MainWindow", "x0:"))
        self.label_5.setText(_translate("MainWindow", "Equação Iteração:"))
        self.inp_expr_MPF.setPlaceholderText(_translate("MainWindow", "Ex.: 2*x**2 + x + 1 | x + log10(x)"))
        self.label_2.setText(_translate("MainWindow", "Equação:"))
        self.inp_e.setPlaceholderText(_translate("MainWindow", "Ex.: 0.001 | 10**-3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
