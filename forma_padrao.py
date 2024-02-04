def conversor(funcao_objetivo, restricoes):

    num_vb = len(funcao_objetivo)
    
    c = funcao_objetivo
    
    folga = [0] * len(restricoes)
    
    A = []
    b = []
    
    for i, restricao in enumerate(restricoes):
        coeficientes, rhs, tipo_operador = restricao
        
        A.append(coeficientes + folga)
        b.append(rhs)
        
        if tipo_operador == '<=':
            c += [0] * (len(restricoes) - 1)
            c[num_vb + i] = -1  
    
    return c, A, b

funcao_objetivo = [2, -3]  
restricoes = [
    ([1, 2], 5, '<='),    
    ([-1, 1], 3, '='),   
    ([0, 1], 4, '>='),   
]

c_padrao, A_padrao, b_padrao = conversor(funcao_objetivo, restricoes)

print("Forma padrão:")
print("Maximize", c_padrao, "sujeito a:")
for i in range(len(A_padrao)):
    print(A_padrao[i], " = ", b_padrao[i])


    import re
