import math

def metPFixo(f, g, x0, e, N):
    print('\n\nMétodo da Iterativo Linear')
    iteracao = 1
    flag = 1
    condition = True
    aux = 0.0
    erro = 1
    listResult = []
    listResult.append(['k', 'x1', 'f(x1)', 'Er'])
    while erro > e:
        x1 = g(x0)
        erro = abs(abs(aux) - abs(f(x1)))
        listResult.append([str(iteracao), str(float(round(x1, 6))), str(float(round(f(x1), 6))), str(float(round(erro, 6)))])
        print('Iteração - %d, x1 = %0.6f, f(x1) = %0.6f' % (iteracao, x1, f(x1)))

        aux = f(x1)
        x0 = x1
        iteracao = iteracao + 1
        if iteracao > N:
            flag = 0
            break
        condition = abs(f(x1)) > e
    if flag == 1:
        print('\nA raíz da equação é: %0.8f' % x1)
        return listResult, x1
    else:
        return 0
        print('\nNão convergente.')