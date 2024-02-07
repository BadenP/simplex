import numpy as np
from numpy.linalg import inv
from forma_padrao import conversor

def simplex(f,c,A,o,b,n,m):

    # Conversão para a norma padrão 
    c = conversor(f,c,A,o)[0]
    A = conversor(f,c,A,o)[1]
    print("Vetor c na forma padrão: ",c)
    print("Matriz A na forma padrão: ", A)

    base = []
    n_base = []

    for i in range (n):
        n_base.append(i)

    contador = 0
    for elemento in o:
        if elemento != "=":
            contador += 1

    for i in range(contador):
        base.append(i+n)

    print("Não base: ", n_base)
    print("Base: ", base)

    while True:
        matriz_base = A[:, base]
        print("Matriz da base:\n", matriz_base)
        try:
            inversa = inv(matriz_base)
            print("Matriz inversa da base:\n", inversa)
        except np.linalg.LinAlgError:
            print("A matriz não possui inversa.")
            return None,"A matriz da base não possui inversa."

        cbt = np.array(c)[base]
        cnt = np.array(c)[n_base]

        # Solução básica
        solucao_basica = inversa @ b
        print("Solução básica: ", solucao_basica)

        # Lambda
        lambdat =  cbt @ inversa 

        # cnj
        mult = (lambdat @ A[:, n_base])
        print("Lambda * anj: \n", mult)
        cnj = cnt - mult
        print("Cnt : ",cnt)
        print("Cbt : ",cbt)
        print("Lambda-t : ",lambdat)
        print("anj : ", A[:, n_base])

        # Cnk: elemento mínimo de cnj
        cnk = min(cnj)
        # índice do cnk
        k = np.argmin(cnj)
        indice_entra_base = n_base[k]
        print("Cnj : ", cnj)
        print("cnk: ", cnk)
        print("índice k : ", k)
        print("índice q entra na base: ", indice_entra_base)

        if cnk >= 0:
            soma = 0
            resultado_texto = ""
            resultado_texto += "Solução ótima encontrada:<br>"
            print("Solução ótima encontrada.")
            print(base)
            print(solucao_basica)

            for i in range(len(solucao_basica)):
                print(f"x{base[i]+1} =", round(solucao_basica[i], 2))
                resultado_texto += f"x{base[i]+1} = {round(solucao_basica[i], 2)}<br>"
                soma += cbt[i] * solucao_basica[i]

            for i in range(len(n_base)):
                resultado_texto += f"x{n_base[i]+1} = 0<br>"
                print(f"x{n_base[i]+1} = 0")

            if f == "Maximizar":
                soma = soma * -1

            resultado_texto += f"Z = {round(soma, 2)}<br>"
            print("Z = ", soma)
            return solucao_basica,resultado_texto
        else:
            y = inversa @ A[:, indice_entra_base]
            if all(y <= 0):
                print("Pare. O problema não tem solução, problema ilimitado.")
                resultado_texto = "O problema não tem solução, problema ilimitado."
                return solucao_basica,resultado_texto
            else:
                e = []
                for i in range(len(solucao_basica)):
                    if y[i] <= 0 :
                        elemento = float('inf')
                    else:
                        print("Xbi/Yi:")
                        print(solucao_basica)
                        print(y)
                        print(solucao_basica[i],"/",y[i])
                        elemento = solucao_basica[i] / y[i]

                    e.append(elemento)

                sai_base = min(e)
                print("Valor mínimo (Xbi/Yi): ", sai_base)
                indice = e.index(sai_base)
                print("Índice do valor mínimo que sai da base: ", indice)
                entra_nao_base = base[indice]
                print("Quem sai da base: ", entra_nao_base)
                n_base[k] = entra_nao_base
                print("Não base atualizada: ", [element + 1 for element in n_base]) 
                base[indice] = indice_entra_base
                print("Base atualizada: ", [element + 1 for element in base])


def teste1():
    n = 2
    m = 2

    # Matriz A
    A = np.array([
                [9, 1],
                [3, 1]])

    # Vetor c
    c = np.array([4, 1])

    # Vetor b
    b = np.array([18,12])
    o = ["<=","<="]
    simplex("Maximizar",c,A,o,b,n,m)[0] == np.array([1,9])


def teste2():
    n = 2
    m = 2

    # Matriz A
    A = np.array([
                [1, -1, 1, 0.0],
                [2, 1, 0, -1]])

    # Vetor c
    c = np.array([-2, -1, 0, 0])

    # Vetor b
    b = np.array([1,6])
    o = [">=",">="]
    simplex("Maximizar",c,A,o,b,n,m)


# Teste 1
def teste3():
    n = 2
    m = 4

    A = np.array([
        [2, 1],
        [3, 4],
        [1, 1],
        [1, -1]])
    
    c = np.array([8, 5])
    b = np.array([1200, 2400, 800, 450])
    o = ["<=", "<=", "<=", "<="]

    # Adicionando asserts
    simplex("Maximizar", c, A, o, b, n, m)

teste3()