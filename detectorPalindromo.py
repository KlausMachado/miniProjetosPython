#detector de palindromo
import time

def inverterStr(str):
    return ''.join(reversed(str)) #reversed coloca a string de tras para frente

def verificadorPalindromo():
    try:
        # Entrada de dados
        frase = str(input('\nQual a palavra ou frase que deve ser analisada? ')).replace(" ", "").lower()
        fraseInvertida = inverterStr(frase)
        print('\n... analisando frase ...')
        time.sleep(1)
        
        if frase == fraseInvertida :
            print('\nEssa frase é um palindromo!')
            print(f'Sua frase: {frase}')
            print(f'Frase invertida: {fraseInvertida}')
        else:
            print('\nNão é um palindromo!')   
            print(f'Sua frase: {frase}')
            print(f'Frase invertida: {fraseInvertida}')

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

def main():
    while True:
        verificadorPalindromo()
        
        continuar = input("\nDeseja verificar uma nova frase? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até logo!")
            break

main() 