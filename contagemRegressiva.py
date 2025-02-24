import time

def contagem():
    try:
        inicio = int(input("Quantos segundos deseja iniciar a contagem regressiva? "))
        print("Contagem regressiva iniciada:")    
        for i in range(inicio, 0, -1):  # Contagem de 5 a 1
            print(i)
            time.sleep(1)  # Espera 1 segundo
        print("\033[91mFogo!\033[0m")

    except ValueError:
        print("\n⚠ Erro: Por favor, insira um número válido.")

def main():
    while True:
        print("Bem vindo a contagem regressiva!")
        contagem()
        
        continuar = input("\nDeseja relizar nova contagem? (s/n) ").strip().lower()
        if continuar != 's':
            print("Espero ter ajudado! Até logo!")
            break 
main()