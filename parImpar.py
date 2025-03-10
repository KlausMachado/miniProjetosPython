'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será 
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas 
que ele conquistou no final do jogo'''
import random

def parImpar():
    contadorUsuario = contadorMaquina = 0 
    while True:
        try:
            opcaoUsuario = input("\nEscolha par ou impar (P/I): ").upper().strip()
            if opcaoUsuario == 'P':
                maquina = 'I'            
            elif opcaoUsuario == 'I':
                maquina = 'P'
            else:
                print("O valor digitado não é valido")
                continue    
            
               
            numeroUsuario = int(input("Faça sua jogada: "))
            numeroMaquina = random.randint(0, 10)
            print("----------------------------------------")
            soma = numeroUsuario + numeroMaquina
            print(soma)
            if soma % 2 == 0 and opcaoUsuario == 'P':
                print("\nVocê venceu! A soma dos números é par. ")
                contadorUsuario += 1
                print(f"Agora você tem {contadorUsuario} vitorias")
            elif soma % 2 != 0 and opcaoUsuario == 'I':
                print("\nVocê venceu! A soma dos números é impar. ")
                contadorUsuario += 1
                print(f"Agora você tem {contadorUsuario} vitorias")
            else:
                print("\n Não foi dessa vez! Vitória da maquina.")
                contadorMaquina += 1    
                
        except ValueError: 
            print("Insira valores validos")
        print("--------------------------------------------")    
        continuar = input("Deseja jogar novamente? (s/n) ").lower().strip()
        if continuar != 's':
            print(f"Placar final: Você ({contadorUsuario}) x Maquina ({contadorMaquina})")
            print("Até a proxima!")
            break 
                
parImpar()