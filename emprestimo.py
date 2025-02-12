def main():
    while True:
        print('\nBem-vindo ao Simulador de Empréstimos!')
        nome = input('Primeiro, me diga o seu nome: ')
        print(f'Olá {nome}, vamos começar a simulação:')
        
        # Tratamento de erros para entradas inválidas
        try:
            valorCasa = float(input('Qual o valor do imóvel que deseja financiar? (ex: 50000.00) '))
            salarioComprador = float(input('Qual a sua média salarial? (ex: R$4000.00) '))
            tempoQuitar = float(input('Em quantos anos você pretende quitar o financiamento? (ex: 1,5 = um ano e meio)'))
        except ValueError:
            print('Por favor, insira valores numéricos válidos.')
            continue
        
        # Cálculo de juros simples
        taxaJurosAnual = 5  # 5% ao ano
        totalComJuros = valorCasa * (1 + (taxaJurosAnual / 100) * tempoQuitar)
        valorParcela = totalComJuros / (tempoQuitar * 12)
        porcentagemParcela = (valorParcela / salarioComprador) * 100
        
        # Verificação da aprovação do empréstimo
        if porcentagemParcela <= 30:            
            print(f'\nEmpréstimo APROVADO! Sua parcela será de R${valorParcela:.2f} por mês.')
        else:
            print(f'\nEmpréstimo NEGADO! A parcela de R${valorParcela:.2f} excede 30% do seu salário.')
        
        # Verificar se o usuário deseja fazer uma nova simulação
        continuar = input('\nDeseja realizar uma nova simulação? (s/n) ').lower().strip()
        if continuar != 's':
            print('Espero ter ajudado! Até logo.')
            break

main()