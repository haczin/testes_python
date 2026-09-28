import random 

print("Vamos jogar pedra, papel ou tesoura")

jogador_vence = 0
computador_vence = 0 


while jogador_vence < 2 and computador_vence < 2:

    escolhas = ["pedra", "papel", "tesoura"]
    escolha_Jogador = input("\nEscolha pedra, papel ou tesoura: ").lower()

    
    if escolha_Jogador not in escolhas:
        print("Opção inválida! Escolha apenas pedra, papel ou tesoura.")
        continue

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
        jogador_vence += 1  
        print("Você venceu esta rodada!")
    elif vencedor == "Computador":
        computador_vence += 1  
        print("O Computador venceu esta rodada!")
    else: 
        print("Empate nesta rodada!")

    
    print(f"Score atual - Jogador: {jogador_vence}, Computador: {computador_vence}")


print("\n--- FIM DO JOGO ---")
if jogador_vence > computador_vence:
    print("Parabéns! Você venceu o jogo!!!")
else:
    print("O Computador venceu o jogo!")
