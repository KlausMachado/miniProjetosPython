def formaPagamento():
    print("\nVocê está no gerenciador de Pagamentos")
       
    try:
        valorCompra = float(input("Para continuar insira o valor total das suas compras: "))
        print('Qual a forma de pagamento?')
        print('1 - à vista dinheiro/cheque: 10% de desconto')
        print('2 - à vista no cartão: 5% de desconto')
        print('3 - em até 2x no cartão: preço formal')
        print('4 - 3x ou mais no cartão: 20% de juros')
        escolha = input('Escolha uma opção: ').strip()
        if escolha == '4':
            parcelas = int(input('Em quantas parcelas deseja dividir sua compra? .'))
        
        # Verifica forma de pagamento
        if escolha == '1':
            desconto = valorCompra * 10 / 100
            valorFinal = float(valorCompra - desconto)
            print(f"\nO valor final da sua compra é de R${valorFinal :.2f}")
        elif escolha == '2':
            desconto = valorCompra * 5 / 100
            valorFinal = float(valorCompra - desconto)
            print(f"\nO valor final da sua compra é de R${valorFinal :.2f}")
        elif escolha == '3':
            valorParcela = valorCompra / 2
            print(f'\nO valor de cada parcela será de R${valorParcela}')
        elif escolha == '4':                        
            juros = valorCompra * 20 / 100
            valorFinal = float(valorCompra + juros) / parcelas
            print(f'\nO valor de cada parcela será de {valorFinal :.2f}. Totalizando {valorFinal * parcelas :.2f}')
            
                 
    except ValueError:
        print("\n⚠ Erro: Por favor, insira um número válido.")

def main():
    while True:
        formaPagamento()
        
        # Verifica se o usuário deseja continuar
        continuar = input("\nDeseja verificar outro triângulo? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nAté a próxima!")
            break

main()

