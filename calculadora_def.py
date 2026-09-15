

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b

def potencia(a, b):
    return a ** b




usuario = input("Olá, bem-vindo(a) à calculadora! Digite seu nome: ")
print(f"Olá, {usuario}! Vamos começar?")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
opr = input("Escolha um operador (+, -, *, / ou **): ")

resultado = None


if opr == "+":
    resultado = somar(n1, n2)
elif opr == "-":
    resultado = subtrair(n1, n2)
elif opr == "*":
    resultado = multiplicar(n1, n2)
elif opr == "/":
    resultado = dividir(n1, n2)
    if resultado is None:
        print("Erro: Não é possível dividir por zero!")
elif opr == "**":
    resultado = potencia(n1, n2)
else:
    print("Erro: Operador inválido!")


if resultado is not None:
    print(f"O resultado é: {resultado:.2f}")
