import numpy as np

def conversor(funcao, funcao_objetivo, restricoes, operadores):

    if funcao == "Maximizar":
        funcao_objetivo = [-1 * elemento for elemento in funcao_objetivo]

    for i in range(len(operadores)):
        if operadores[i] == '>=':
            # Adiciona uma variável de folga na respectiva linha das restrições
            folga = np.zeros((len(restricoes),))
            folga[i] = -1
            restricoes = np.column_stack((restricoes, folga))
            # Adiciona 0 na função objetivo
            funcao_objetivo = np.append(funcao_objetivo, 0)
        elif operadores[i] == '<=':
            # Adiciona uma variável de folga na respectiva linha das restrições
            folga = np.zeros((len(restricoes),))
            folga[i] = 1
            restricoes = np.column_stack((restricoes, folga))
            # Adiciona 0 na função objetivo
            funcao_objetivo = np.append(funcao_objetivo, 0)

    return funcao_objetivo,restricoes

funcao = "min"

# Matriz A
restricoes = np.array([
        [1, 1],
        [-1, 2],
        [3, 1]
    ])

operadores = np.array(['<=', '>=','='])

# Vetor c
funcao_objetivo = np.array([2, 1])

# Vetor b
b = np.array([1, 6])

# funcao_objetivo, restricoes = conversor(funcao, funcao_objetivo, restricoes, operadores)
#print(conversor(funcao, funcao_objetivo, restricoes, operadores))
# print("Função Objetivo:", funcao_objetivo)
# print("Restrições:")
# print(restricoes)

def teste1():
    # Minimizar 2x + y
    funcao = "min"
    restricoes = np.array([
        [1, 1],
        [-1, 2],
        [3, 1]
    ])
    operadores = np.array(['<=', '>=', '='])
    funcao_objetivo = np.array([2, 1])
    resultado_fobj = [2,1,0,0]
    # Resultado esperado com as colunas de variáveis de folga
    resultado_restricoes = np.array([[ 1,  1,  1,  0],
                                    [-1,  2,  0, -1],
                                    [ 3,  1,  0,  0]])
    resultado_obtido = conversor(funcao, funcao_objetivo, restricoes, operadores)

    # Verifica se as matrizes são iguais
    assert np.array_equal(resultado_obtido[0], resultado_fobj)
    assert np.array_equal(resultado_obtido[1], resultado_restricoes)

def teste1():
    # Minimizar 2x + y
    funcao = "min"
    restricoes = np.array([
        [1, 1],
        [-1, 2],
        [3, 1]
    ])
    operadores = np.array(['<=', '>=', '='])
    funcao_objetivo = np.array([2, 1])
    resultado_fobj = [2,1,0,0]
    # Resultado esperado com as colunas de variáveis de folga
    resultado_restricoes = np.array([[ 1,  1,  1,  0],
                                    [-1,  2,  0, -1],
                                    [ 3,  1,  0,  0]])
    resultado_obtido = conversor(funcao, funcao_objetivo, restricoes, operadores)

    # Verifica se as matrizes são iguais
    assert np.array_equal(resultado_obtido[0], resultado_fobj)
    assert np.array_equal(resultado_obtido[1], resultado_restricoes)

def teste2():
    # Minimizar 2x + y + z 
    funcao = "max"
    restricoes = np.array([
        [1, 1, 1],
        [-1, 2, 0],
        [-1, 0, 1]
    ])
    operadores = np.array(['<=', '<=', '<='])
    funcao_objetivo = np.array([1, -1, 2])
    resultado_fobj = [-1,1,-2,0,0,0]
    # Resultado esperado com as colunas de variáveis de folga
    resultado_restricoes = np.array([[ 1,  1,  1,  1, 0, 0],
                                    [-1,  2,  0, 0, 1, 0],
                                    [-1,  0,  1,  0, 0, 1]])
    resultado_obtido = conversor(funcao, funcao_objetivo, restricoes, operadores)

    # Verifica se as matrizes são iguais
    assert np.array_equal(resultado_obtido[0], resultado_fobj)
    assert np.array_equal(resultado_obtido[1], resultado_restricoes)

def teste3():
    # Minimizar 2x + y
    funcao = "min"
    restricoes = np.array([
        [1, 1],
        [-1, 2],
        [3, 1]
    ])
    operadores = np.array(['<=', '>=', '='])
    funcao_objetivo = np.array([2, 1])
    resultado_fobj = [2,1,0,0]
    # Resultado esperado com as colunas de variáveis de folga
    resultado_restricoes = np.array([[ 1,  1,  1,  0],
                                    [-1,  2,  0, -1],
                                    [ 3,  1,  0,  0]])
    resultado_obtido = conversor(funcao, funcao_objetivo, restricoes, operadores)

    # Verifica se as matrizes são iguais
    assert np.array_equal(resultado_obtido[0], resultado_fobj)
    assert np.array_equal(resultado_obtido[1], resultado_restricoes)

def teste4():
    # Minimizar 2x + y
    funcao = "min"
    restricoes = np.array([
        [1, 1],
        [-1, 2],
        [3, 1]
    ])
    operadores = np.array(['<=', '>=', '='])
    funcao_objetivo = np.array([2, 1])
    resultado_fobj = [2,1,0,0]
    # Resultado esperado com as colunas de variáveis de folga
    resultado_restricoes = np.array([[ 1,  1,  1,  0],
                                    [-1,  2,  0, -1],
                                    [ 3,  1,  0,  0]])
    resultado_obtido = conversor(funcao, funcao_objetivo, restricoes, operadores)

    # Verifica se as matrizes são iguais
    assert np.array_equal(resultado_obtido[0], resultado_fobj)
    assert np.array_equal(resultado_obtido[1], resultado_restricoes)
