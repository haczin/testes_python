usuario = input("Olá, bem vindo(a) a minha calculadora, por favor digite seu nome: ")
print(f"Olá {usuario}, vamos começar?")

n1 = float(input("Por favor escolha um número: "))
n2 = float(input("Agora digite o segundo número: "))
opr = input("Use um operador matemático (+, -, *, / ou **): ")

# Usamos a variável resultado para guardar o valor da conta
resultado = None

if opr == "+":
    resultado = n1 + n2
elif opr == "-":
    resultado = n1 - n2 
elif opr == "*":
    resultado = n1 * n2 
elif opr == "/":
    
    if n2 == 0:
        print("Erro: Não é possível dividir por zero!")
    else:
        resultado = n1 / n2
elif opr == "**":
    resultado = n1 ** n2
else:
    print("Erro: Operador inválido!")


if resultado is not None:
    print(f"O resultado é de {resultado:.2f}")
