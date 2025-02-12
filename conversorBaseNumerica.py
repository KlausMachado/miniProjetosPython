def main():
    while True:
        print('\nBem-vindo ao Conversor de Base Numérica! Vamos começar')                      
        try:
            numero = int(input('Digite um número inteiro: '))
            print('Escolha a base para conversão:')
            print('\n1 - Binário')
            print('2 - Octal')
            print('3 - Hexadecimal')
            escolha = input('\nSua opção: ')
        except ValueError:
            print('Por favor, insira valores numéricos válidos.')
            continue    
        
        if escolha == '1':
            print(f'O número {numero} em binário é {bin(numero)[2:]}')
        elif escolha == '2':
            print(f'O número {numero} em octal é {oct(numero)[2:]}')
        elif escolha == '3':
            print(f'O número {numero} em hexadecimal é {hex(numero)[2:].upper()}')
        else:
            print('Opção inválida. Tente novamente.')
        
        repetir = input('Deseja realizar nova conversão? (s/n) ').strip().lower()
        if repetir != 's':
            print('Até a próxima!')
            break      

main()