'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
'''
def main():
    while True:
        print('\nBem-vindo ao Comparador Númerico! Vamos começar')                      
        try:
            n1 = int(input('Digite um número inteiro: '))
            n2 = int(input('Digite um segundo número inteiro: '))                                  
        except ValueError:
            print('Por favor, insira valores numéricos válidos.')
            continue    
        print('\nRealizando comparação:')
        if n1 == n2:
            print('Não existe valor maior, os dois são iguais.')
        elif n1 > n2:
            print('O primeiro valor é maior.')
        elif n1 < n2:
            print('O segundo valor é maior.')       
        
        repetir = input('\nDeseja realizar nova comparação? (s/n) ').strip().lower()
        if repetir != 's':
            print('Até a próxima!')
            break      

main()
