def verifica_triangulo():
    print("\nDigite os comprimentos das três retas:")
    print("Substitua a (,) por (.) se necessário.")
    
    try:
        # Entrada dos comprimentos
        r1 = float(input("Primeira reta: "))
        r2 = float(input("Segunda reta: "))
        r3 = float(input("Terceira reta: "))
        
        # Verifica a condição de existência de um triângulo
        if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
            print("\nAs retas podem formar um triângulo!")

            # Classificação do triângulo
            if r1 == r2 == r3:
                print("➡ Esse é um triângulo **EQUILÁTERO**, pois todos os lados são iguais.")
            elif (r1 == r2) or (r1 == r3) or (r2 == r3):
                print("➡ Esse é um triângulo **ISÓSCELES**, pois dois lados são iguais.")
            else:
                print("➡ Esse é um triângulo **ESCALENO**, pois todos os lados são diferentes.")
        else:
            print("\n❌ As retas NÃO podem formar um triângulo.")
    
    except ValueError:
        print("\n⚠ Erro: Por favor, insira um número válido.")

def main():
    while True:
        verifica_triangulo()
        
        # Verifica se o usuário deseja continuar
        continuar = input("\nDeseja verificar outro triângulo? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nAté a próxima!")
            break

main()