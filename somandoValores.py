def main():
    soma_total = 0  # Variável para acumular a soma
    lista = []
    while True:
        try:
            n = int(input("Digite um número para somar (ou 0 para sair): "))
            if n == 0:
                print(f"A soma total dos números {lista} é:\n{soma_total}")
                print("Programa encerrado.")
                break
            soma_total += n  #soma total
            lista.append(n)


            print(f"Soma parcial: {soma_total}")
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()