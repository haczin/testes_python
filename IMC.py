print("Vamos calcular seu IMC")


peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))


imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Você está no peso normal")
elif 25.0 <= imc <= 29.9:
    print("Você está com sobrepeso")
else:
    print("Você está com obesidade")
