from datetime import datetime

def main():
    while True:
        print('\nBem-vindo ao Verificador de Alistamento Militar Brasileiro!')
        try:
            anoNascimento = int(input('Em que ano você nasceu? '))
            print('\nQual o seu gênero?')
            print('1 - Mulher')
            print('2 - Pessoa não binária')
            print('3 - Homem')
            escolha = input('Sua opção: ').strip()
        except ValueError:
            print('Por favor, insira valores numéricos válidos.')
            continue

        # Cálculo da idade correta
        agora = datetime.now()
        idade = agora.year - anoNascimento

        # Verificação de alistamento para homens (obrigatório no Brasil)
        if escolha == '3':
            print(f'\nVocê tem {idade} anos.')
            if idade < 18:
                anos_faltantes = 18 - idade
                print(f'Ainda faltam {anos_faltantes} ano(s) para o seu alistamento.')
                print(f'Seu alistamento será em {anoNascimento + 18}.')
            elif idade == 18:
                print('É a hora exata de se alistar! Procure a junta militar mais próxima.')
            else:
                anos_passados = idade - 18
                print(f'Você já deveria ter se alistado há {anos_passados} ano(s).')
                print(f'O seu alistamento deveria ter ocorrido em {anoNascimento + 18}.')

        # Para mulheres e pessoas não binárias (alistamento opcional)
        elif escolha == '1' or escolha == '2':
            print('\nO alistamento militar NÃO é obrigatório para o seu gênero.')
            if idade >= 18:
                print('Caso tenha interesse, você pode se alistar de forma voluntária.')
            elif idade < 18:
                print(f'Caso tenha interesse, no ano {anoNascimento + 18} você poderá se alistar de forma voluntária.')    

        else:
            print('Opção inválida. Tente novamente.')
            continue

        # Perguntar se o usuário deseja repetir
        repetir = input('\nDeseja realizar uma nova verificação? (s/n) ').strip().lower()
        if repetir != 's':
            print('Até a próxima!')
            break

main()