import numpy as np

# Função que converte um problema para a forma padrão
def conversor(funcao, funcao_objetivo, restricoes, operadores, b):

    if funcao == "Maximizar":
        funcao_objetivo = [-1 * elemento for elemento in funcao_objetivo]

    for i in range(len(b)):
        if b[i] < 0:
            restricoes[i] *= -1
            b[i] *= -1
            if operadores[i] == ">=":
                operadores[i] = "<="
            elif operadores[i] == "<=":
                operadores[i] = ">="

    for i in range(len(operadores)):
        if operadores[i] == '>=':
            folga = np.zeros((len(restricoes),))
            folga[i] = -1
            restricoes = np.column_stack((restricoes, folga))
            funcao_objetivo = np.append(funcao_objetivo, 0)
        elif operadores[i] == '<=':
            folga = np.zeros((len(restricoes),))
            folga[i] = 1
            restricoes = np.column_stack((restricoes, folga))
            funcao_objetivo = np.append(funcao_objetivo, 0)
         

    return funcao_objetivo,restricoes

# Casos de teste, cada teste é um problema de PL

def teste1():
    n = 2
    m = 2

    A = np.array([[9, 1],[3, 1]])

    c = np.array([4, 1])

    b = np.array([18,12])
    o = ["<=","<="]
    resultado_restricoes = conversor("Maximizar", c, A, o, b)[1]
    resultado_fobj = conversor("Maximizar", c, A, o, b)[0]
    resultado_esperado_restricoes = np.array([[9, 1, 1, 0],[3,1,0,1]])
    resultado_esperado_fobj = np.array([-4,-1,0,0])
    assert np.array_equal(resultado_esperado_restricoes, resultado_restricoes)
    assert np.array_equal(resultado_esperado_fobj, resultado_fobj) 

def teste2():
    n = 2
    m = 2

    A = np.array([[1, -1],
                  [2, 1]])

    c = np.array([2,-1])
    b = np.array([1,6])
    o = ["<=",">="]
    resultado_restricoes = conversor("Maximizar", c, A, o, b)[1]
    resultado_fobj = conversor("Maximizar", c, A, o, b)[0]
    resultado_esperado_restricoes = np.array([[1,-1,1,0],[2,1,0,-1]])
    resultado_esperado_fobj = np.array([-2,1,0,0])
    assert np.array_equal(resultado_esperado_restricoes, resultado_restricoes)
    assert np.array_equal(resultado_esperado_fobj, resultado_fobj) 
    
def teste3():
    n = 2
    m = 4

    A = np.array([[2, 1],
                  [3, 4],
                  [1, 1],
                  [1, -1]])
    
    c = np.array([8, 5])
    b = np.array([1200, 2400, 800, 450])
    o = ["<=", "<=", "<=", "<="]
    resultado_restricoes = conversor("Maximizar", c, A, o, b)[1]
    resultado_fobj = conversor("Maximizar", c, A, o, b)[0]
    resultado_esperado_restricoes = np.array([[2,1,1,0,0,0],[3,4,0,1,0,0],[1,1,0,0,1,0],[1,-1,0,0,0,1]])
    resultado_esperado_fobj = np.array([-8,-5,0,0,0,0])
    assert np.array_equal(resultado_esperado_restricoes, resultado_restricoes)
    assert np.array_equal(resultado_esperado_fobj, resultado_fobj) 
    

def teste4():
    n = 2
    m = 3

    A = np.array([[3, 2],
                  [1, 0],
                  [0, 2]])
    
    c = np.array([3,5])
    b = np.array([18,4,12])
    o = ["<=", "<=", "<="]
    resultado_restricoes = conversor("Maximizar", c, A, o, b)[1]
    resultado_fobj = conversor("Maximizar", c, A, o, b)[0]
    resultado_esperado_restricoes = np.array([[3,2,1,0,0],[1,0,0,1,0],[0,2,0,0,1]])
    resultado_esperado_fobj = np.array([-3,-5,0,0,0])
    assert np.array_equal(resultado_esperado_restricoes, resultado_restricoes)
    assert np.array_equal(resultado_esperado_fobj, resultado_fobj) 

def teste5():
    n = 2
    m = 3

    A = np.array([[1, 1],
                  [1, -1],
                  [-1, 1]])
    
    c = np.array([1,-2])
    b = np.array([6,4,4])
    o = ["<=", "<=", "<="]
    resultado_restricoes = conversor("Min", c, A, o, b)[1]
    resultado_fobj = conversor("Min", c, A, o, b)[0]
    resultado_esperado_restricoes = np.array([[1,1,1,0,0],[1,-1,0,1,0],[-1,1,0,0,1]])
    resultado_esperado_fobj = np.array([1,-2,0,0,0])
    assert np.array_equal(resultado_esperado_restricoes, resultado_restricoes)
    assert np.array_equal(resultado_esperado_fobj, resultado_fobj) 

def teste6():
    n = 3
    m = 3

    A = np.array([[1, 1, 2],
                  [1, 1, -1],
                  [-1, 1, 1]])
    
    c = np.array([1,1,-4])
    b = np.array([9,2,4])
    o = ["<=", "<=", "<="]
    resultado_restricoes = conversor("Min", c, A, o, b)[1]
    resultado_fobj = conversor("Min", c, A, o, b)[0]
    resultado_esperado_restricoes = np.array([[1,1,2,1,0,0],[1,1,-1,0,1,0],[-1,1,1,0,0,1]])
    resultado_esperado_fobj = np.array([1,1,-4,0,0,0])
    assert np.array_equal(resultado_esperado_restricoes, resultado_restricoes)
    assert np.array_equal(resultado_esperado_fobj, resultado_fobj) 

# Chamadas para testar os problemas 
teste1()
teste2()
teste3()
teste4()
teste5()
teste6()