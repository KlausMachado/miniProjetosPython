from datetime import datetime

def ageComparator():
    try:
        # Entrada de dados
        years = input('\nQual os anos de nascimento deseja comparar? \nSepare os anos por , (ex: 2000, 1990) ').split(',')
        current_year = datetime.now().year
        ages_calculated = []                
        
        for year in years:
            years_list = int(year.strip())            
            ages_calculated.append(current_year - years_list)
        if len(ages_calculated) <= 1:
            print('Digite pelomenos dois anos.')
            return
        max_age = max(ages_calculated)
        min_age = min(ages_calculated)
            
        print(f'A maior idade entre todas é: {max_age}')
        print(f'A menir idade entre todas é: {min_age}')
            
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

def main():
    while True:
        ageComparator()
        continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até logo!")
            break

main()