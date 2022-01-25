from bk_metodoNewtonRaphson_V2 import newton
from bk_metodoBissecao import bissecao
from bk_metodoPontoFixo import metPFixo
from bk_metodoFalsaPosicao import MFPosicao
from bk_funcoes import *
import ast
from math import *
from sympy import Symbol
# from numpy import *
# from testes.testMatriz import newton
x = Symbol('x')
opcao = input(
    "## MENU ## \n 1 - Metodo Newton-Raphson \n 2 - Metodo Bisseção \n 3 - M.P.Falsa \n 4 - M. P. Fixo\n --> Escolha a opção desejada: ")

if int(opcao) == 1:
    expr = input("Digite a Equação: ")  # "2*x - sin(x) + 4"
    x0 = input("Digite o valor inicial: ")
    tamErro = input("tamanho de erro: ")
    maxInter = input("Digite o máximo de iterações: ")

    fx = str(calculaDerivada(expr))
    f = lambda x: eval(expr)
    df = lambda x: eval(fx)

    resultado = newton(f, df, float(x0), float(tamErro), int(maxInter))
    resultMatriz = resultado[0]
    resultRaiz = resultado[1]
    k = resultado[2]
    for l in range(k):
        for c in range(k):
            print(f'[{resultMatriz[l][c]}]', end='')
        print()
    print("Raiz: " + str(resultRaiz))

elif int(opcao) == 2:
    a = 0
    b = 1
    exprBissecao = input("Digite a Equação: ")
    tolBissecao = input("Digite a tolerancia: ")
    maxInterBissecao = input("Digite o máximo de iterações: ")
    # fBissecao = lambda x: exprBissecao
    exprBiss = lambda x: eval(exprBissecao)
    # test = valAendB(exprBiss)
    # a = test[0]
    # b = test[1]
    print("a:{} b:{}".format(a, b))
    raizBissecao = bissecao(exprBiss, 0.3, 0.4, float(tolBissecao), int(maxInterBissecao))
    print("\n Raiz: {} \n".format(raizBissecao))
elif int(opcao) == 3:
    expr = "x**3 - 9*x + 3"
    f = lambda x: eval(expr)
    print(expr)
    a = 0
    b = 1
    tol = 1e-4
    resultMPF = MPFalsa(f, float(a), float(b), float(tol))
    print(resultMPF)
elif int(opcao) == 4:
    x0 = float(input("Entre com o numero real x0: "))
    e = float(input("Entre com o numero real e: "))
    fx = lambda x: exp(-x ** 2 + 1) + sin(x ** 2) - x
    wx = lambda x: ((exp(-x ** 2 + 1) + sin(x ** 2) - x) + 2 * x) / 2
    result = metPFixo(fx, wx, x0, e)
    print("A raiz é: {} \nO numero de iterações foram: {}".format(result[0], result[1]))