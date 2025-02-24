import random

def jokenpo():    
    opcoes = ["PEDRA", "PAPEL", "TESOURA"]    
    print("\nVamos jogar Jokenpô! Escolha a sua opção:")
    
    # Exibindo opções numeradas
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao}")

    try:
        # Jogador escolhe a opção
        jogada = int(input("\nQual a sua jogada? (1, 2 ou 3): ")) - 1

        # Verifica se a jogada é válida
        if jogada not in [0, 1, 2]:
            print("\n❌ Escolha uma opção válida (1, 2 ou 3).")
            return

        # Jogada da máquina
        jogadaMaquina = random.randint(0, 2)
        escolhaMaquina = opcoes[jogadaMaquina]

        print(f"\nVocê escolheu: {opcoes[jogada]}")
        print(f"A máquina escolheu: {escolhaMaquina}")

        derrota = "Você perdeu! Mais sorte da próxima vez."
        vitoria = "Você venceu! PARABÉNS :)"
        empate = "Empate! Joguem novamente."

        # Verifica o resultado
        if jogada == jogadaMaquina:
            print(empate)
        elif (jogada == 0 and jogadaMaquina == 2) or \
             (jogada == 1 and jogadaMaquina == 0) or \
             (jogada == 2 and jogadaMaquina == 1):
            print(vitoria)
        else:
            print(derrota)

    except ValueError:
        print("\n⚠ Erro: Por favor, insira um número válido.")

def main():
    while True:
        jokenpo()
        
        # Pergunta se deseja jogar novamente
        continuar = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nAté a próxima!")
            break

main()