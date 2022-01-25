from math import *
from sympy import *

def newton(f, x0, epsilon, maxIter):
    if abs(f(x0)) <= epsilon:
        return x0
    k=0
    matrizResult = []
    matrizResult.append(['K', 'X0', 'F(x0)', "F'(x0)", 'Er'])
    while k <= maxIter:
        df = flin(f, x0, 0.0000001)
        x1 = x0-f(x0) / df
        dr = abs(x1 - x0)
        matrizResult.append([str(k), str(round(x0, 6)), str(round(f(x0), 6)), str(round(df, 6)), str(round(dr, 6))])
        if abs(f(x0)) <= epsilon:
            return (matrizResult, x0, k)
        x0 = x1
        k += 1
    print("ERRO> Número Máximo de iterações atingido")
    return (matrizResult, x1, k)

def flin (f, x, h):
    a = x+h
    b = x-h
    fderiv = (f(a) - f(b))/(2.0*h)
    return fderiv