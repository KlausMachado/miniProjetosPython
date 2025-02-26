def somaPares():
    print('\nBem-vindo à calculadora de números pares.')
    try:
        inicio = int(input('Em que número vamos iniciar a soma dos números pares? '))
        fim = int(input('Em que número vamos finalizar a soma? '))

        soma = 0  
        print('Número par encontrado:')
        for i in range(inicio, fim + 1):           
            if i % 2 == 0:
                print(i)
                soma += i  

        print(f'A soma dos números pares no intervalo de {inicio} a {fim} é: {soma}')
      
    except ValueError:
        print("\n⚠ Erro: Por favor, insira um número válido.")
        return 
       
    
def main():
    while True:
        somaPares()
        continuar = input('\nDeseja realizar novo cálculo? (s/n) ').lower().strip()
        if continuar != 's':
            print('Até a próxima!')
            break

main()