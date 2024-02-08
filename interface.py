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

        self.label_variaveis = QLabel('Número de variáveis:')
        self.entrada_variaveis = QLineEdit()
        hlayout.addWidget(self.label_variaveis)
        hlayout.addWidget(self.entrada_variaveis)
    
        self.label_restricoes = QLabel('Número de restrições:')
        self.entrada_restricoes = QLineEdit()
        hlayout2.addWidget(self.label_restricoes)
        hlayout2.addWidget(self.entrada_restricoes)

        self.btn_gerar = QPushButton('Gerar')
        self.btn_gerar.clicked.connect(self.cria_grid)

        self.layout_grid = QGridLayout()

        layout.addLayout(hlayout)
        layout.addLayout(hlayout2)
        layout.addWidget(self.btn_gerar)
        layout.addLayout(self.layout_grid)

        self.setLayout(layout)
        self.setWindowTitle('Simplex')
        self.show()
    
    def limpa_grid(self):
        for i in reversed(range(self.layout_grid.count())):
            widget = self.layout_grid.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def cria_grid(self):
        self.limpa_grid()
        num_variaveis = int(self.entrada_variaveis.text())
        num_restricoes = int(self.entrada_restricoes.text())

        self.layout_grid.addWidget(QLabel("Selecione a função:"), 0, 0)
        combobox = QComboBox()
        combobox.addItems(["Maximizar", "Minimizar"])
        self.layout_grid.addWidget(combobox, 0, 1, 1, num_variaveis)
        self.layout_grid.addWidget(QLabel("Função objetivo:"), 1, 0)

        entradas_objetivo = []
        for i in range(num_variaveis):
            if i != num_variaveis - 1:
                string = "+"
            else:
                string = ""
            entrada = QLineEdit()
            self.layout_grid.addWidget(entrada, 1, 2 * i + 1)
            self.layout_grid.addWidget(QLabel(f"X{i+1}" + string), 1, 2 * i + 2)
            entradas_objetivo.append(entrada)

        self.layout_grid.addWidget(QLabel("Restrições:"), 2, 0)

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
                self.layout_grid.addWidget(entrada, 2+r, 2 * i + 1)
                self.layout_grid.addWidget(QLabel(f"X{i+1}" + string), 2+r, 2 * i + 2)
                entradas_restricoes.append(entrada)

            combobox2 = QComboBox()
            combobox2.addItems([">=", "<=", "="])
            self.layout_grid.addWidget(combobox2, 2 + r, 2 * i + 3)
            op.append(combobox2)

            entrada_b = QLineEdit()
            self.layout_grid.addWidget(entrada_b, 2 + r, 2 * i + 4)
            entradas_b.append(entrada_b)
        
        for i in range(num_variaveis):
            if i != num_variaveis - 1:
                string = ","
            else:
                string = ""
            self.layout_grid.addWidget(QLabel(f"X{i+1}" + string), 3+r, 2+i)

        self.layout_grid.addWidget(QLabel(">= 0"), 3+r, 3+i)
        resolver_button = QPushButton("Resolver")
        resolver_button.clicked.connect(lambda: self.resolver())
        self.layout_grid.addWidget(resolver_button, 5 + num_restricoes, num_restricoes, 1, 2)
        self.f_combobox = combobox
        self.entradas_objetivo = entradas_objetivo
        self.entradas_restricoes = entradas_restricoes
        self.entradas_b = entradas_b
        self.op = op

    def resolver(self):
        num_variaveis = int(self.entrada_variaveis.text())
        num_restricoes = int(self.entrada_restricoes.text())

        valores_objetivo = []
        for entrada in self.entradas_objetivo:
            if entrada.text()=='':
                valores_objetivo.append(0)
            else:
                valores_objetivo.append(float(entrada.text()))

        valores_restricoes = []
        for entrada in self.entradas_restricoes:
            if entrada.text()=='':
                valores_restricoes.append(0)
            else:
                valores_restricoes.append(float(entrada.text()))

        matriz_A = [valores_restricoes[i * num_variaveis: (i + 1) * num_variaveis] for i in range(num_restricoes)]

        vetor_b = []
        for entrada in self.entradas_b:
            if entrada.text()=='':
                vetor_b.append(0)
            else:
                vetor_b.append(float(entrada.text()))

        operadores = [combo.currentText() for combo in self.op]
        objetivo = self.f_combobox.currentText()

        print("Numero de variaveis:", num_variaveis)
        print("Numero de restricoes:", num_restricoes)
        print("Função objetivo:", objetivo)
        print("Função objetivo:", valores_objetivo)
        print("Matriz A:", matriz_A)
        print("Operadores:", operadores)
        print("Vetor b:", vetor_b)
        resultado = simplex(objetivo, valores_objetivo, matriz_A, operadores, vetor_b, num_variaveis, num_restricoes)[1]
        
        resultado_widget = QLabel()
        self.layout_grid.addWidget(resultado_widget, 4 + num_restricoes, 0, 1, 2)
        resultado_texto = "<html><b>Solução:</b><br>"
        resultado_texto += resultado
        resultado_texto += "</html>"
        resultado_widget.setText(resultado_texto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplexSolver()
    sys.exit(app.exec_())
