#calculadora de numero primo:
def verificandoNumeroPrimo():
    try:
        # Entrada de dados
        n = int(input("Qual número você deseja verificar? "))
        divisores = []
        
        print("\nAnalisando número ...")
        if n % 2 == 0:
            for i in range(1, n + 1):                
                if i % 2 == 0:
                    divisores.append(str(i))
                    divisores_str = ",".join(map(str, divisores))
                    
            print(f'O numero foi divisivel por: {divisores_str}')
            
        else :
            print('Esse é um numero primo')                                
                   

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

def main():
    while True:
        verificandoNumeroPrimo()
        continuar = input("\nDeseja calcular outro numero? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até logo!")
            break

main()