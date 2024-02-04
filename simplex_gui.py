from tkinter import *
from tkinter import ttk 
import numpy as np
from numpy.linalg import inv
from simplex import simplex

def obter_valores():
    num_variaveis = int(entrada_variaveis.get())
    num_restricoes = int(entrada_restricoes.get())
    rotulo_max = Label(janela, text=f"Selecione a função:")
    rotulo_max.grid(row=3, column=0, padx=5, pady=10)
    valores_combobox = ["Maximizar", "Minimizar"]  # Substitua com os valores desejados
    combobox = ttk.Combobox(janela, values=valores_combobox)
    combobox.grid(row=3, column=1, columnspan=num_variaveis, padx=5, pady=10)
    f.append(combobox)
    rotulo_objetivo = Label(janela, text=f"Função objetivo:")
    rotulo_objetivo.grid(row=4, column=0, padx=5, pady=10)
    
    # Criar a matriz na interface
    count = 1
    for i in range(num_variaveis):
        entrada_valor = Entry(janela, width=5)
        entrada_valor.grid(row=4, column=count, padx=5, pady=10)
        
        rotulo_variavel = Label(janela, text=f"X{i+1}")
        rotulo_variavel.grid(row=4, column=count+1, padx=5, pady=10)

        entradas_variaveis_objetivo.append(entrada_valor)
        count += 3

    rotulo_objetivo = Label(janela, text=f"Restrições:")
    rotulo_objetivo.grid(row=5, column=0, padx=5, pady=10)
    
    # Criar a matriz na interface para as restrições
    for r in range(num_restricoes):
        count = 1
        for i in range(num_variaveis):
            if i == num_variaveis - 1:
                string = ""
            else:
                string = " +"
            
            entrada_valor = Entry(janela, width=5)
            entrada_valor.grid(row=5+r, column=count, padx=0, pady=10)
            
            rotulo_variavel = Label(janela, text=f"X{i+1}" + string)
            rotulo_variavel.grid(row=5+r, column=count+1, padx=5, pady=10)

            entradas_variaveis_restricoes.append(entrada_valor)
            count += 3
        
        operadores_combobox = [">=", "<=", "="]  # Substitua com os valores desejados
        combobox2 = ttk.Combobox(janela, values=operadores_combobox, width=3)
        combobox2.grid(row=5+r, column=count, padx=10, pady=10)
        op.append(combobox2)
        
        entrada_valor2 = Entry(janela, width=5)
        entrada_valor2.grid(row=5+r, column=count+2, padx=5, pady=10)
        entradas_variaveis_b.append(entrada_valor2)


    for i in range(num_variaveis): 
        if i == num_variaveis - 1:
            string = ""
        else:
            string = ","       
        rotulo_variavel = Label(janela, text=f"X{i+1}" + string)
        rotulo_variavel.grid(row=5+r+1, column=i+1, padx=0, pady=10)

    rotulo_objetivo = Label(janela, text=f">= 0")
    rotulo_objetivo.grid(row=5+r+1, column=num_variaveis+1, padx=5, pady=10)

    botao_resolver = Button(janela, text="Resolver", command=gerarResultado)
    botao_resolver.grid(row=5+r+2, column=0, columnspan=2, pady=10)

def gerarResultado():
    # Coletar valores das entradas da função objetivo
    valores_objetivo = np.array([float(element.get()) for element in entradas_variaveis_objetivo])

    # Coletar valores das entradas das restrições
    valores_restricoes = [float(element.get()) for element in entradas_variaveis_restricoes]
    num_variaveis = len(valores_objetivo)
    num_restricoes = len(valores_restricoes) // num_variaveis

    # Criar matriz_A a partir das entradas das restrições
    matriz_A = np.array([valores_restricoes[i * num_variaveis: (i + 1) * num_variaveis] for i in range(num_restricoes)])

    # Coletar valores das entradas do vetor b
    vetor_b = np.array([float(element.get()) for element in entradas_variaveis_b])

    # # Imprimir as matrizes
    # print("Matriz A:")
    # print(matriz_A)

    # print("\nVetor b:")
    # print(vetor_b)

    # print("\nVetor c (Função Objetivo):")
    # print(valores_objetivo)
    o = [element.get() for element in op]
    simplex(f[0].get(), valores_objetivo, matriz_A, o, vetor_b, num_variaveis, num_restricoes)


# Criar a janela
janela = Tk()
janela.title("Entrada de Valores")

# Criar rótulos e entradas
rotulo_variaveis = Label(janela, text="Número de variáveis:")
rotulo_variaveis.grid(row=0, column=0, padx=10, pady=10)

entrada_variaveis = Entry(janela, width=5)
entrada_variaveis.grid(row=0, column=1, padx=10, pady=10)

rotulo_restricoes = Label(janela, text="Número de restrições:")
rotulo_restricoes.grid(row=1, column=0, padx=10, pady=10)

entrada_restricoes = Entry(janela, width=5)
entrada_restricoes.grid(row=1, column=1, padx=10, pady=10)

# Botão para obter os valores
botao_obter_valores = Button(janela, text="Gerar", command=obter_valores)
botao_obter_valores.grid(row=2, column=0, columnspan=2, pady=10)

# Lista para armazenar as entradas das variáveis
entradas_variaveis_objetivo = []
entradas_variaveis_restricoes = []
entradas_variaveis_b = []
f = []
op = []

# Iniciar a interface gráfica
janela.mainloop()
