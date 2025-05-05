def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

print("Calculadora simples")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
operacao = input("Escolha (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", somar(a, b))
elif operacao == "-":
    print("Resultado:", subtrair(a, b))
elif operacao == "*":
    print("Resultado:", multiplicar(a, b))
elif operacao == "/":
    print("Resultado:", dividir(a, b))
else:
    print("Operação inválida")
