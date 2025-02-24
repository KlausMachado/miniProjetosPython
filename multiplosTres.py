def calcular():
    print('\nCalculando multipos')
    try:
        inicio = int(input('Em qual numero inicar o calculo? '))
        fim = int(input('Em qual numero finalizamos o calculo? ')) + 1
        multiplo = int(input('Qual multiplo deseja calcular? '))
    except ValueError:
        print("\n⚠ Erro: Por favor, insira um número válido.")
        return
        
    somaMultiplos = 0
    for i in range(inicio, fim):
        
        #verificação multiplos
        if i % multiplo == 0:
            print('Os multiplos são:')
            print(i)
            somaMultiplos += i
            
    print(f'A soma dos multiplos de {multiplo}, no intervalo entre {inicio} e {fim - 1} é: {somaMultiplos}')
    
def main():
    while True:
        calcular()
        
        continuar = input('\nDeseja realizar novo calculo? (s/n) ').strip().lower()
        if continuar != 's':
            print('Até a proxima!')
            break

main()            
