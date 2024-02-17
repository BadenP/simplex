import numpy as np
from numpy.linalg import inv
from forma_padrao import conversor

# Algoritmo do Simplex
def simplex(f,c,A,o,b,n,m):

    # Conversão para a norma padrão 
    c = conversor(f,c,A,o,b)[0]
    A = conversor(f,c,A,o,b)[1]
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

        # Índice do cnk
        k = np.argmin(cnj)
        # Definição de qual é o índice (que está em N) que vai entrar na base
        indice_entra_base = n_base[k]
        print("Cnj : ", cnj)
        print("cnk: ", cnk)
        print("índice k : ", k)
        print("índice que entra na base: ", indice_entra_base)

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

# Casos de teste, cada teste é um problema de PL  
                
def teste1():
    n = 2
    m = 2

    A = np.array([[9, 1],[3, 1]])

    c = np.array([4, 1])

    b = np.array([18,12])
    o = ["<=","<="]
    resultado = simplex("Maximizar", c, A, o, b, n, m)[0]
    resultado_arredondado = np.round(resultado, 2)
    esperado_arredondado = np.array([1,9])
    assert np.array_equal(resultado_arredondado, esperado_arredondado)

def teste2():
    n = 2
    m = 2

    A = np.array([[1, -1],[2, 1]])

    c = np.array([2,-1])
    b = np.array([1,6])
    o = ["<=",">="]
    resultado = simplex("Maximizar", c, A, o, b, n, m)[0]
    resultado_arredondado = np.round(resultado, 2)
    esperado_arredondado = np.array([1, -4])
    assert np.array_equal(resultado_arredondado, esperado_arredondado)
    assert simplex("Maximizar", c, A, o, b, n, m)[1] == "O problema não tem solução, problema ilimitado."

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

    resultado = simplex("Maximizar", c, A, o, b, n, m)[0]
    resultado_arredondado = np.round(resultado, 2)
    esperado_arredondado = np.array([240, 210, 80, 480])
    assert np.array_equal(resultado_arredondado, esperado_arredondado)

def teste4():
    n = 2
    m = 3

    A = np.array([
        [3, 2],
        [1, 0],
        [0, 2]])
    
    c = np.array([3,5])
    b = np.array([18,4,12])
    o = ["<=", "<=", "<="]
    resultado = simplex("Maximizar", c, A, o, b, n, m)[0]
    assert np.array_equal(resultado,np.array([2,2,6]))

def teste5():
    n = 2
    m = 3

    A = np.array([
        [1, 1],
        [1, -1],
        [-1, 1]])
    
    c = np.array([1,-2])
    b = np.array([6,4,4])
    o = ["<=", "<=", "<="]
    resultado = simplex("min", c, A, o, b, n, m)[0]
    resultado_arredondado = np.round(resultado, 2)
    esperado_arredondado = np.array([1,8,5])
    assert np.array_equal(resultado_arredondado,esperado_arredondado)

def teste6():
    n = 3
    m = 3

    A = np.array([
        [1, 1, 2],
        [1, 1, -1],
        [-1, 1, 1]])
    
    c = np.array([1,1,-4])
    b = np.array([9,2,4])
    o = ["<=", "<=", "<="]
    resultado = simplex("min", c, A, o, b, n, m)[0]
    resultado_arredondado = np.round(resultado, 2)
    esperado_arredondado = np.array([0.33,6,4.33])
    assert np.array_equal(resultado_arredondado,esperado_arredondado)

# Chamadas para testar os problemas 
teste1()
teste2()
teste3()
teste4()
teste5()
teste6()