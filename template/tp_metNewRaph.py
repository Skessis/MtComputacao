# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_metNewtRaph2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_metNewRaph(object):
    def setupUi(self, metNewRaph):
        metNewRaph.setObjectName("metNewRaph")
        metNewRaph.resize(797, 654)
        metNewRaph.setMinimumSize(QtCore.QSize(797, 654))
        metNewRaph.setMaximumSize(QtCore.QSize(797, 654))
        metNewRaph.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.centralwidget = QtWidgets.QWidget(metNewRaph)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 65, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.inp_expr = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_expr.setGeometry(QtCore.QRect(112, 90, 551, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_expr.setFont(font)
        self.inp_expr.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_expr.setInputMask("")
        self.inp_expr.setText("")
        self.inp_expr.setObjectName("inp_expr")
        self.but_calc = QtWidgets.QPushButton(self.centralwidget)
        self.but_calc.setGeometry(QtCore.QRect(420, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.but_calc.setFont(font)
        self.but_calc.setStyleSheet("color: rgb(255, 255, 255);")
        self.but_calc.setObjectName("but_calc")
        self.but_clear = QtWidgets.QPushButton(self.centralwidget)
        self.but_clear.setGeometry(QtCore.QRect(240, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.but_clear.setFont(font)
        self.but_clear.setStyleSheet("color: rgb(255, 255, 255);")
        self.but_clear.setObjectName("but_clear")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 310, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(10, 540, 761, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelResult.setFont(font)
        self.labelResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelResult.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(38, 38, 38);")
        self.labelResult.setText("")
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 340, 761, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(38, 38, 38);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 130, 281, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.inp_x0 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_x0.setFont(font)
        self.inp_x0.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_x0.setObjectName("inp_x0")
        self.gridLayout.addWidget(self.inp_x0, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.inp_itera = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_itera.setFont(font)
        self.inp_itera.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_itera.setObjectName("inp_itera")
        self.gridLayout.addWidget(self.inp_itera, 2, 1, 1, 1)
        self.inp_erro = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inp_erro.setFont(font)
        self.inp_erro.setStyleSheet("color: rgb(255, 255, 255);")
        self.inp_erro.setText("")
        self.inp_erro.setObjectName("inp_erro")
        self.gridLayout.addWidget(self.inp_erro, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(620, 600, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lblTempExib = QtWidgets.QLabel(self.centralwidget)
        self.lblTempExib.setGeometry(QtCore.QRect(690, 600, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTempExib.setFont(font)
        self.lblTempExib.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblTempExib.setText("")
        self.lblTempExib.setObjectName("lblTempExib")
        metNewRaph.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(metNewRaph)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menubar.setObjectName("menubar")
        metNewRaph.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(metNewRaph)
        self.statusbar.setObjectName("statusbar")
        metNewRaph.setStatusBar(self.statusbar)

        self.retranslateUi(metNewRaph)
        QtCore.QMetaObject.connectSlotsByName(metNewRaph)

    def retranslateUi(self, metNewRaph):
        _translate = QtCore.QCoreApplication.translate
        metNewRaph.setWindowTitle(_translate("metNewRaph", "Método Newton Raphson"))
        self.label.setText(_translate("metNewRaph", "Método Newton Raphson"))
        self.label_2.setText(_translate("metNewRaph", "Equação:"))
        self.inp_expr.setPlaceholderText(_translate("metNewRaph", "Ex.: 2*x**2 + x + 1 | x + log10(x)"))
        self.but_calc.setText(_translate("metNewRaph", "Calcular"))
        self.but_clear.setText(_translate("metNewRaph", "Limpar"))
        self.label_6.setText(_translate("metNewRaph", "Resultado:"))
        self.label_3.setText(_translate("metNewRaph", "x0:"))
        self.label_5.setText(_translate("metNewRaph", "Iterações:"))
        self.inp_x0.setPlaceholderText(_translate("metNewRaph", "Ex.: 0.5 | 1"))
        self.label_4.setText(_translate("metNewRaph", "Erro:"))
        self.inp_itera.setPlaceholderText(_translate("metNewRaph", "Ex.: 1 | 10 | 100"))
        self.inp_erro.setPlaceholderText(_translate("metNewRaph", "Ex.: 0.001 | 10**-3"))
        self.label_7.setText(_translate("metNewRaph", "Execução:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    metNewRaph = QtWidgets.QMainWindow()
    ui = Ui_metNewRaph()
    ui.setupUi(metNewRaph)
    metNewRaph.show()
    sys.exit(app.exec_())
