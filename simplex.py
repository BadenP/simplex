import numpy as np
from numpy.linalg import inv
from forma_padrao import conversor
# n = 2
# m = 2

# # Matriz A
# A = np.array([
#               [1, -1, 1, 0.0],
#               [2, 1, 0, -1]])

# # Vetor c
# c = np.array([-2, -1, 0, 0])

# # Vetor b
# b = np.array([1,6])

# def simplex(A,c,b,n,m):
#     base = []
#     n_base = []

#     for i in range (n):
#         n_base.append(i)

#     for i in range(m):
#         base.append(i+n)

#     print("nao base = ", n_base)
#     print("base = ", base)

#     controle = True
#     iteracao = 0
#     while controle:
#         iteracao += 1
#         base_matrix = A[:, base]
#         print("Base:\n", base_matrix)
#         inversa = inv(base_matrix)
#         print("inversa:\n", inversa)
#         cbt = c[base]
#         cnt = c[n_base]

#         # Solução básica
#         solucao_basica = inversa @ b

#         # Lambda
#         lambdat =  cbt @ inversa 

#         # cnj
#         cnj = cnt - (lambdat @ A[:, n_base])
#         print("cnt : ",cnt)
#         print("cbt : ",cbt)
#         print("lambdat : ",lambdat)
#         print("anj : ",A[:, n_base])

#         # Cnk
#         cnk = min(cnj)
#         k = np.argmin(cnj)
#         print("cnj : ", cnj)
#         print("k : ", k)
#         print("cnk: ", cnk)

#         if cnk >= 0:
#             print("Solução ótima encontrada.")
#             print("Solução:", solucao_basica)
#             break  # Exit the loop if optimal solution is reached
#         else:
#             y = inversa @ A[:, k]
#             if any(y < 0):
#                 print("Pare. Soluções ilimitadas")
#                 break 
#             else:
#                 e = []
#                 for i in range(len(solucao_basica)):
#                     if y[i] == 0:
#                         elemento = float('inf')
#                     else:
#                         elemento = solucao_basica[i] / y[i]

#                     e.append(elemento)

#                 sai_base = min(e)
#                 print("sai_base:", sai_base)

#                 indice = e.index(sai_base)
#                 print("indice =", indice)
#                 entra_nao_base = base[indice]
#                 print("entra na nao_base = ", entra_nao_base)
#                 n_base[k] = entra_nao_base
#                 print("nao base =", [element + 1 for element in n_base])
                
#                 base[indice] = k
#                 print("base atualizada: ", [element + 1 for element in base])



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

    controle = True
    iteracao = 0
    while controle:
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
            print("Solução ótima encontrada.")
            print("Solução:", solucao_basica)
            break  # Exit the loop if optimal solution is reached
        else:
            y = inversa @ A[:, k]
            if any(y < 0):
                print("Pare. Soluções ilimitadas.")
                break 
            else:
                e = []
                for i in range(len(solucao_basica)):
                    if y[i] == 0:
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
