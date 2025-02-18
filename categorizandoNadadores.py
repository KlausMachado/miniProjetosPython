from datetime import datetime

def main():
    while True:
        print('\nBem-vindo ao portão da Confederação Nacional de Natação!')
        print('Vamos encontrar a categoria ideal para você competir. Vamos começar:')
        
        try:
            anoNascimento = int(input('Em que ano você nasceu? '))
            print('\nQual o seu gênero?')
            print('1 - Mulher')
            print('2 - Pessoa não binária')
            print('3 - Homem')
            escolha = input('Sua opção: ').strip()

            # Definindo categoria para NB
            if escolha == '2':
                escolha = input('Você se sentiria confortavel em copetir nas categorias feminino(1) ou masculino(3)? ').strip()         
        except ValueError:
            print('Por favor, insira valores numéricos válidos.')
            continue

        # Cálculo da idade correta
        agora = datetime.now()
        idade = agora.year - anoNascimento

        textoFinalAdultos = 'Para se inscrever, entre em contato conosco pelo telefone (00)0000000.'
        textoFinalMenores = 'Para se inscrever, basta seus responsáveis entrarem em contato com a gente.'

        # Verificação das categorias
        if idade <= 9:
            if escolha == '1':
                print('Você pode competir na categoria MIRIM feminina (até 9 anos).')
            elif escolha == '3':
                print('Você pode competir na categoria MIRIM masculina (até 9 anos).')
            print(textoFinalMenores)  # Agora a mensagem será exibida corretamente

        elif idade <= 14:
            if escolha == '1':
                print('Você pode competir na categoria INFANTIL feminina (até 14 anos).')
            elif escolha == '3': 
                print('Você pode competir na categoria INFANTIL masculina (até 14 anos).')   
            print(textoFinalMenores)

        elif idade <= 25:
            if escolha == '1':
                print('Você pode competir na categoria SENIOR feminina.')
            elif escolha == '3':    
                print('Você pode competir na categoria SENIOR masculina.')
            print(textoFinalAdultos) 

        elif idade > 25:
            if escolha == '1':
                print('Você pode competir na categoria MASTER feminina.')
            elif escolha == '3':
                print('Você pode competir na categoria MASTER masculina.')    
            print(textoFinalAdultos) 

        else:
            print('Opção inválida. Tente novamente.')
            continue

        # Perguntar se o usuário deseja repetir
        repetir = input('\nDeseja realizar uma nova verificação? (s/n) ').strip().lower()
        if repetir != 's':
            print('Até a próxima!')
            break

main()