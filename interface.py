import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from simplex import simplex

class SimplexSolver(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        hlayout = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        self.label_variables = QLabel('Número de variáveis:')
        self.entry_variables = QLineEdit()
        hlayout.addWidget(self.label_variables)
        hlayout.addWidget(self.entry_variables)
    
        self.label_constraints = QLabel('Número de restrições:')
        self.entry_constraints = QLineEdit()
        hlayout2.addWidget(self.label_constraints)
        hlayout2.addWidget(self.entry_constraints)

        self.button_generate = QPushButton('Gerar')
        self.button_generate.clicked.connect(self.create_dynamic_input_widgets)

        self.dynamic_input_layout = QGridLayout()

        layout.addLayout(hlayout)
        layout.addLayout(hlayout2)
        layout.addWidget(self.button_generate)
        layout.addLayout(self.dynamic_input_layout)

        self.setLayout(layout)
        self.setWindowTitle('Entrada de Valores')
        self.show()
    
    def clear_dynamic_input_widgets(self):
        # num_variaveis = self.entry_variables.text()
        # num_restricoes = self.entry_constraints.text()

        # while self.layout().count():
        #     item = self.layout().takeAt(0)
        #     widget = item.widget()
        #     if widget is not None:
        #         widget.deleteLater()

        for i in reversed(range(self.dynamic_input_layout.count())):
            widget = self.dynamic_input_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # self.label_variables = QLabel('Número de variáveis:')
        # self.entry_variables = QLineEdit()
        # self.entry_variables.setText(num_variaveis)
    
        # self.label_constraints = QLabel('Número de restrições:')
        # self.entry_constraints = QLineEdit()
        # self.entry_constraints.setText(num_restricoes)

        # self.button_generate = QPushButton('Gerar')
        # self.button_generate.clicked.connect(self.create_dynamic_input_widgets)

        # self.dynamic_input_layout = QGridLayout()

        # self.layout().addWidget(self.label_variables)
        # self.layout().addWidget(self.entry_variables)
        # self.layout().addWidget(self.label_constraints)
        # self.layout().addWidget(self.entry_constraints)
        # self.layout().addWidget(self.button_generate)
        # self.layout().addLayout(self.dynamic_input_layout)

    def create_dynamic_input_widgets(self):
        self.clear_dynamic_input_widgets()
        num_variaveis = int(self.entry_variables.text())
        num_restricoes = int(self.entry_constraints.text())

        self.dynamic_input_layout.addWidget(QLabel("Selecione a função:"), 0, 0)
        combobox = QComboBox()
        combobox.addItems(["Maximizar", "Minimizar"])
        self.dynamic_input_layout.addWidget(combobox, 0, 1, 1, num_variaveis)
        self.dynamic_input_layout.addWidget(QLabel("Função objetivo:"), 1, 0)

        entradas_objetivo = []
        for i in range(num_variaveis):
            if i != num_variaveis - 1:
                string = "+"
            else:
                string = ""
            entrada = QLineEdit()
            self.dynamic_input_layout.addWidget(entrada, 1, 2 * i + 1)
            self.dynamic_input_layout.addWidget(QLabel(f"X{i+1}" + string), 1, 2 * i + 2)
            entradas_objetivo.append(entrada)

        self.dynamic_input_layout.addWidget(QLabel("Restrições:"), 2, 0)

        entradas_restricoes = []
        entradas_b = []
        op = []
        for r in range(num_restricoes):
            for i in range(num_variaveis):
                if i != num_variaveis - 1:
                    string = "+"
                else:
                    string = ""
                entrada = QLineEdit()
                self.dynamic_input_layout.addWidget(entrada, 2+r, 2 * i + 1)
                self.dynamic_input_layout.addWidget(QLabel(f"X{i+1}" + string), 2+r, 2 * i + 2)
                entradas_restricoes.append(entrada)

            combobox2 = QComboBox()
            combobox2.addItems([">=", "<=", "="])
            self.dynamic_input_layout.addWidget(combobox2, 2 + r, 2 * i + 3)
            op.append(combobox2)

            entrada_b = QLineEdit()
            self.dynamic_input_layout.addWidget(entrada_b, 2 + r, 2 * i + 4)
            entradas_b.append(entrada_b)

        resolver_button = QPushButton("Resolver")
        resolver_button.clicked.connect(lambda: self.resolve_problem())
        self.dynamic_input_layout.addWidget(resolver_button, 3 + num_restricoes, 0, 1, 2)
        self.f_combobox = combobox
        self.entradas_objetivo = entradas_objetivo
        self.entradas_restricoes = entradas_restricoes
        self.entradas_b = entradas_b
        self.f_combobox = combobox
        self.op = op


    def resolve_problem(self):
        num_variaveis = int(self.entry_variables.text())
        num_restricoes = int(self.entry_constraints.text())
        # Coletar valores das entradas da função objetivo
        valores_objetivo = [float(entrada.text()) for entrada in self.entradas_objetivo]

        # Coletar valores das entradas das restrições
        valores_restricoes = [float(entrada.text()) for entrada in self.entradas_restricoes]

        # Criar matriz_A a partir das entradas das restrições
        matriz_A = [valores_restricoes[i * num_variaveis: (i + 1) * num_variaveis] for i in range(num_restricoes)]

        # Coletar valores das entradas do vetor b
        vetor_b = [float(entrada.text()) for entrada in self.entradas_b]

        # Coletar operadores
        operadores = [combo.currentText() for combo in self.op]

        # Coletar função de maximização ou minimização
        objetivo = self.f_combobox.currentText()

        # Chamar a função simplex com os valores coletados
        # Você pode substituir o chamado abaixo pela sua lógica de resolução real
        print("Numero de variaveis:", num_variaveis)
        print("Numero de restricoes:", num_restricoes)
        print("Função Objetivo:", objetivo)
        print("Vetor C (Função Objetivo):", valores_objetivo)
        print("Matriz A:", matriz_A)
        print("Operadores:", operadores)
        print("Vetor b:", vetor_b)
        resultado = simplex(objetivo, valores_objetivo, matriz_A, operadores, vetor_b, num_variaveis, num_restricoes)[1]
        
        # Criar um QLabel para exibir o resultado como HTML
        resultado_widget = QLabel()
        #resultado_widget.setTextFormat(Qt.RichText)
        self.dynamic_input_layout.addWidget(resultado_widget, 4 + num_restricoes, 0, 1, 2)

        # Construir o texto do resultado
        resultado_texto = "<html><b>Solução:</b><br>"
        resultado_texto += resultado
        resultado_texto += "</html>"

        # Definir o texto no QLabel
        resultado_widget.setText(resultado_texto)


# Lista para armazenar as entradas das variáveis
entradas_variaveis_objetivo = []
entradas_variaveis_restricoes = []
entradas_variaveis_b = []
maximizar_ou_minimizar = []
operadores = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplexSolver()
    sys.exit(app.exec_())
