import math

traco = "-------------"

def notasCinquenta(valor):
    return math.floor(valor / 50)

def notasVinte(valor):
    return math.floor(valor / 20)

def notasDez(valor):
    return math.floor(valor / 10)

def notasCinco(valor):
    return math.floor(valor / 5)

def notasDois(valor):
    return math.floor(valor / 2)

def calcularNotas(valor):
    notas = {
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0
    }
    
    valorRestante = valor
    
    # Calcula a quantidade de notas de 50
    notas[50] = notasCinquenta(valorRestante)
    valorRestante -= notas[50] * 50
    
    # Calcula a quantidade de notas de 20
    notas[20] = notasVinte(valorRestante)
    valorRestante -= notas[20] * 20
    
    # Calcula a quantidade de notas de 10
    notas[10] = notasDez(valorRestante)
    valorRestante -= notas[10] * 10
    
    # Verifica se o valor restante pode ser zerado com notas de 2
    if valorRestante % 2 == 0:
        notas[2] = notasDois(valorRestante)
        valorRestante -= notas[2] * 2
    else:
        # Se não, tenta usar notas de 5 primeiro
        notas[5] = notasCinco(valorRestante)
        valorRestante -= notas[5] * 5
        
        # Depois, usa notas de 2 para o restante
        notas[2] = notasDois(valorRestante)
        valorRestante -= notas[2] * 2
    
    return notas, valorRestante

def simuladorCaixaEletronico():
    while True:
        try:
            print("\nBem-vindo ao caixa eletrônico!")
            valor = int(input("Qual o valor do saque? R$"))
            
            if valor <= 0:
                print("Valor inválido. O valor deve ser maior que 0.")
                continue
            
            notas, valorRestante = calcularNotas(valor)
            
            print("\nNotas a serem sacadas:")
            print(traco)
            print(f"Notas de 50: {notas[50]}")
            print(f"Notas de 20: {notas[20]}")
            print(f"Notas de 10: {notas[10]}")
            print(f"Notas de 5: {notas[5]}")
            print(f"Notas de 2: {notas[2]}")
            print(traco)
            print(f"Valor restante: {valorRestante}")
            
            if valorRestante > 0:
                print("Não foi possível sacar o valor completo com as notas disponíveis.")
            
            novo_saque = input("\nDeseja realizar outro saque? (s/n): ").strip().lower()
            if novo_saque != 's':
                print("Obrigado por usar o caixa eletrônico. Até mais!")
                break
                
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    simuladorCaixaEletronico()