#calculadora de progressão aritimetica:
def calcular_pa():
    try:
        a1 = float(input("Digite o primeiro termo da PA (a₁): "))
        r = float(input("Digite a razão da PA (r): "))
        n = int(input("Quantos termos da PA você deseja calcular? "))

        
        if n <= 0:
            print("O número de termos deve ser maior que zero.")
            return
       
        print("\nTermos da Progressão Aritmética:")
        soma = 0  
        for i in range(1, n + 1):
            an = a1 + (i - 1) * r             
            print(f"Termo {i}: {an}")
            soma += an  

       
        print(f"\nA soma dos {n} primeiros termos da PA é: {soma}")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

def main():
    while True:
        calcular_pa()
        continuar = input("\nDeseja calcular outra PA? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até logo!")
            break

main()