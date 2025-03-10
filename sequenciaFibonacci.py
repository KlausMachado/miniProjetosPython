'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os 
N primeiros elementos de uma Sequência de Fibonacci'''

def sequenciaFibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequencia = [0, 1]
    contador = 2
    
    while contador < n:       
        proximo_termo = sequencia[-1] + sequencia[-2] #soma dos dois ultimos termos do array
        print(f"soma: {sequencia[-1]} + {sequencia[-2]} = {proximo_termo}")
        sequencia.append(proximo_termo)
        contador += 1

    return sequencia

def main():
    while True:
        try:
            n = int(input("Quantos termos da sequencia de Fibonacci você quer gerar? "))
            if n < 0:
                print("Erro: O número de termos deve ser um inteiro maior que 0")
                continue
            break
        except ValueError:
            print("Erro: Por favor, insira um número inteiro valido")

    print(f"Sequência de Fibonacci com {n} termos: {sequenciaFibonacci(n)}")

if __name__ == "__main__":
    main()