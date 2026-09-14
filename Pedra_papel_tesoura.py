import random 

print("Vamos jogar pedra, papel ou tesoura")


escolhas = ["pedra", "papel", "tesoura"]

escolha_Jogador = input("Escolha pedra, papel ou tesoura: ").lower()

escolha_computador = random.choice(escolhas)

print(f"Escolha do computador: {escolha_computador.capitalize()}")

if (escolha_Jogador == "pedra" and escolha_computador == "tesoura") or \
   (escolha_Jogador == "tesoura" and escolha_computador == "papel") or \
   (escolha_Jogador == "papel" and escolha_computador == "pedra"):
    vencedor = "Jogador"

elif escolha_Jogador == escolha_computador:
    vencedor = "Empate"
else:
    vencedor = "Computador"

if vencedor == "Jogador":
    print("Você venceu!")
elif vencedor == "Computador":
    print("O Computador venceu!")
else: 
    print("Empate!")
