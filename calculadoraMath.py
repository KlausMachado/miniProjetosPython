import math

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Não é possível calcular a raiz quadrada de um número negativo."
    raizX = math.sqrt(x)
    return f"A raiz quadrada de {x} é {raizX:.2f}"

def arredondar_valores(x):
    arredondandoXCima = math.ceil(x)
    arredondandoXBaixo = math.floor(x)
    return (f"Arredondando o valor para cima: {arredondandoXCima}, "
            f"para baixo: {arredondandoXBaixo}")

def logaritmo_natural(x):
    if x <= 0:
        return "Erro: Logaritmos naturais requerem valores positivos."
    logaritimoX = math.log(x)
    return f"O logaritmo de {x} é {logaritimoX:.2f}"

def calcular_hipotenusa(x, y):
    hipotenusa = math.hypot(x, y)
    return f"A hipotenusa de {x} e {y} é {hipotenusa:.2f}"

def seno_cosseno_tangente(x):
    senX = math.sin(x)
    cosX = math.cos(x)
    tanX = math.tan(x)
    return (f"O seno de {x} é {senX:.2f}, o cosseno é {cosX:.2f} "
            f"e a tangente é {tanX:.2f}")

def calcular_fatorial(x):
    if x < 0 or not x.is_integer():
        return "Erro: Fatorial requer valores inteiros não negativos."
    fatorialX = math.factorial(int(x))
    return f"O fatorial de {x} é {fatorialX}."

def calcular_progressao(a1, r, n):
    if n <= 0:
        return "Erro: O número de termos deve ser maior que zero."
    
    termos = []
    soma = 0
    for i in range(1, n + 1):
        an = a1 + (i - 1) * r
        termos.append(f"Termo {i}: {an}")
        soma += an
    termo_geral_pa = a1 + (n - 1) * r
    resultado = "\n".join(termos)
    resultado += f"\nA soma dos {n} primeiros termos da PA é: {soma}"
    return resultado, f"O {n}º termo da PA é: {termo_geral_pa}"

def main():
    while True:
        print("\nEscolha uma operação:")
        print("1: Raiz quadrada")
        print("2: Arredondando valores")
        print("3: Logaritmo natural")
        print("4: Hipotenusa")
        print("5: Seno, cosseno e tangente")
        print("6: Fatorial")
        print("7: Progressão aritmética")
        print("8: Sair")
        
        operacao = input("Qual operação gostaria de realizar? (1-8): ")

        if operacao == "8":
            print("Até a próxima!")
            break
            
        if operacao not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Erro: Operação inválida. Tente novamente.")
            continue

        print(f"\nObs: Para operações que não podem ser realizadas com números flutuantes, os valores serão arredondados.")
        
        try:
            if operacao == "7":
                a1 = float(input("Digite o primeiro termo (a1): "))  # Primeiro termo
                r = float(input("Digite a razão (r): "))             # Razão da PA
                n = int(input("Digite o número de termos (n): "))    # Número de termos
                resultado, termo_geral_pa = calcular_progressao(a1, r, n)
                print(resultado)
                print(termo_geral_pa)
            else:
                x = float(input("Digite o valor de x: "))
                if operacao == "4":
                    y = float(input("Digite o valor de y: "))  # Segundo valor para a hipotenusa
                    resultado = calcular_hipotenusa(x, y)
                elif operacao == "1":
                    resultado = raiz_quadrada(x)
                elif operacao == "2":
                    resultado = arredondar_valores(x)
                elif operacao == "3":
                    resultado = logaritmo_natural(x)
                elif operacao == "5":
                    resultado = seno_cosseno_tangente(x)
                elif operacao == "6":
                    resultado = calcular_fatorial(x)

                print(resultado)
        except ValueError:
            print("Erro: Por favor, insira números válidos.")
        
        continuar = input("\nGostaria de calcular outro número? (s/n): ").lower()
        if continuar != "s":
            print("Até a próxima!")
            break
    
main()