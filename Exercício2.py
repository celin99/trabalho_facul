import random
import matplotlib.pyplot as plt

class GraficoEquacaoLinear:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def gerar_vetor_x(self, tamanho):
        vetor_x = []
        for _ in range(tamanho):
            vetor_x.append(random.uniform(-10, 10))  # Gerando números aleatórios entre -10 e 10
        return vetor_x

    def calcular_y(self, x):
        return self.a * x + self.b * x - self.c

    def criar_grafico(self, vetor_x):
        vetor_y = [self.calcular_y(x) for x in vetor_x]

        plt.scatter(vetor_x, vetor_y, c='blue', label='Pontos')  # Configuração do gráfico de pontos
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.title('Gráfico da Equação Linear')
        plt.legend()
        plt.show()

# Valores para a, b e c (baseado nos três primeiros números do RU)
a = 3
b = 6
c = 2

# Criando uma instância da classe GraficoEquacaoLinear
grafico = GraficoEquacaoLinear(a, b, c)

# Gerando vetor de x
tamanho_vetor = 10
vetor_x = grafico.gerar_vetor_x(tamanho_vetor)

# Criando o gráfico
grafico.criar_grafico(vetor_x)
