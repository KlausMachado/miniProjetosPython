def escrevendo(n):
    numeros = {
        0: "Zero",
        1: "Um",
        2: "Dois",
        3: "Três",
        4: "Quatro",
        5: "Cinco",
        6: "Seis",
        7: "Sete",
        8: "Oito",
        9: "Nove",
        10: "Dez",
        11: "Onze",
        12: "Doze",
        13: "Treze",
        14: "Catorze",
        15: "Quinze",
        16: "Dezesseis",
        17: "Dezessete",
        18: "Dezoito",
        19: "Dezenove",
        20: "Vinte"
    }
    return print(numeros[n])
    

def main():
    while True:
        try:
            escolha = int(input("\nEscolha um número inteiro de 0 a 20: (-1 para sair) "))
            if escolha == -1:
                print("Até a proxima!")
                break 
            elif escolha < 0 or escolha > 20:
                print("\nO numero deve estar no intervalo entre 0 e 20!")
                continue
               
            escrevendo(escolha)
            
        except ValueError:
            print("Digite um número valido!")
            continue
            
        continuar = input("Deseja escolher outro número? (s/n) ").strip().upper()
        if continuar != "S":
            print("\nAté a proxima!")
            break

main()