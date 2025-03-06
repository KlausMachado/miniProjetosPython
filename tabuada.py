#tabuada utilizando for
def tabuada():
    print('\nBem vindo a calculadora de tabuadas ')
    
    try:
        multiplicador = int(input('Qual é o multiplicador? '))
        multiplicandoInicio =	 int(input('Qual o primeiro multiplicando da tabuada? '))
        multiplicandoFinal =	 int(input('Qual o ultimo multiplicando da tabuada? ')) + 1

        for i in range(multiplicandoInicio, multiplicandoFinal):
            calculo = i * multiplicador
            print(calculo)
    
    except ValueError:
        print("\n⚠ Erro: Por favor, insira um número válido.")
        return

def main():
    while True:
        tabuada()
        
        continuar = input('\nDeseja calcular nova tabuada? (s/n) ')
        if continuar != 's':
            print('Até a proxima! ')
            break

main()