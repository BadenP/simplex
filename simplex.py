import numpy as np
from numpy.linalg import inv
from forma_padrao import conversor

def simplex(f,c,A,o,b,n,m):
    c = conversor(f,c,A,o)[0]
    A = conversor(f,c,A,o)[1]
    print(c)
    print(A)

    base = []
    n_base = []

    for i in range (n):
        n_base.append(i)

    for i in range(m):
        base.append(i+n)

    print("nao base = ", n_base)
    print("base = ", base)

    iteracao = 0
    while True:
        iteracao += 1
        base_matrix = A[:, base]
        print("Base:\n", base_matrix)
        inversa = inv(base_matrix)
        print("inversa:\n", inversa)
        cbt = np.array(c)[base]
        cnt = np.array(c)[n_base]

        # Solução básica
        solucao_basica = inversa @ b

        # Lambda
        lambdat =  cbt @ inversa 

        # cnj
        cnj = cnt - (lambdat @ A[:, n_base])
        print("cnt : ",cnt)
        print("cbt : ",cbt)
        print("lambdat : ",lambdat)
        print("anj : ",A[:, n_base])

        # Cnk
        cnk = min(cnj)
        k = np.argmin(cnj)
        print("cnj : ", cnj)
        print("k : ", k)
        print("cnk: ", cnk)

        if cnk >= 0:
            soma = 0
            resultado_texto = ""
            resultado_texto += "Solução ótima encontrada:<br>"
            print("Solução ótima encontrada.")
            for i in range(len(solucao_basica)):
                print(f"x{base[i]+1} =", round(solucao_basica[i]))
                resultado_texto += f"x{base[i]+1} = {round(solucao_basica[i], 1)}<br>"
                soma += cbt[i] * solucao_basica[i]

            for i in range(len(n_base)):
                resultado_texto += f"x{n_base[i]+1} = 0<br>"

            if f == "Maximizar":
                soma = soma * -1

            resultado_texto += f"Z = {round(soma, 1)}<br>"
            print("Z = ", soma)
            return solucao_basica,resultado_texto
        else:
            y = inversa @ A[:, k]
            if all(y <= 0):
                print("Pare. O problema não tem solução.")
                resultado_texto = "O problema não tem solução."
                return solucao_basica,resultado_texto
            else:
                e = []
                for i in range(len(solucao_basica)):
                    if y[i] <= 0 :
                        elemento = float('inf')
                    else:
                        elemento = solucao_basica[i] / y[i]

                    e.append(elemento)

                sai_base = min(e)
                print("sai_base:", sai_base)

                indice = e.index(sai_base)
                print("indice =", indice)
                entra_nao_base = base[indice]
                print("entra na nao_base = ", entra_nao_base)
                n_base[k] = entra_nao_base
                print("nao base =", [element + 1 for element in n_base])
                
                base[indice] = k
                print("base atualizada: ", [element + 1 for element in base])


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

teste1()

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
    m = 2

    A = np.array([
        [1, -1],
        [2, 1]])
    
    c = np.array([2, -1])
    b = np.array([1, 6])
    o = ["<=", ">="]

    # Adicionando asserts
    assert simplex("Maximizar", c, A, o, b, n, m) == False