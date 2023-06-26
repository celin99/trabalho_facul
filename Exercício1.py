import math

class Calculadora:
    def __init__(self):
        pass

    def mostrar_menu(self):
        print("")
        print("Escolha a operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Expoente (^)")
        print("6. Resto (%)")
        print("7. Raiz quadrada da soma dos dois números (sqrt(Num1 + Num2))")
        print("0. Sair")

    def executar_calculadora(self):
        while True:
            self.mostrar_menu()
            escolha = int(input("Digite o número da operação desejada: "))
            
            if escolha == 0:
                print("Encerrando a calculadora...")
                break

            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))

            if escolha == 1:
                resultado = self.somar(num1, num2)
                print("Resultado da soma:", resultado)
            elif escolha == 2:
                resultado = self.subtrair(num1, num2)
                print("Resultado da subtração:", resultado)
            elif escolha == 3:
                resultado = self.multiplicar(num1, num2)
                print("Resultado da multiplicação:", resultado)
            elif escolha == 4:
                resultado = self.dividir(num1, num2)
                print("Resultado da divisão:", resultado)
            elif escolha == 5:
                resultado = self.expoente(num1, num2)
                print("Resultado do expoente:", resultado)
            elif escolha == 6:
                resultado = self.resto(num1, num2)
                print("Resultado do resto:", resultado)
            elif escolha == 7:
                resultado = self.raiz_quadrada_soma(num1, num2)
                print("Resultado da raiz quadrada da soma:", resultado)
            else:
                print("Opção inválida. Tente novamente.")

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Erro: divisão por zero não é permitida.")
            return None

    def expoente(self, a, b):
        return a ** b

    def resto(self, a, b):
        return a % b

    def raiz_quadrada_soma(self, a, b):
        return math.sqrt(a + b)

calculadora = Calculadora()

calculadora.executar_calculadora()