class Matriz:
    def __init__(self):
        self.matriz = []
        
    def inserindoValores(self):
        for c in range(3):
            linha = []
            for i in range(3):
                while True:
                    try:
                        n = int(input(f"Digite um numero inteiro para a posição {c+1}.{i+1}:"))
                        linha.append(n)
                        break
                    except ValueError:
                        print("Adicione um numero valido.")
            self.matriz.append(linha)
            
    def exibirMatriz(self):
        print("-" *30)
        print("Matriz: \n")
        for linha in self.matriz:
            print(f"| {' | '.join(map(str, linha))} |")
        print("-" *30)    
            
    def analisandoMatriz(self):
        print("Realizando analise...")
        numeros = [num for linha in self.matriz for num in linha] 
        n = sum(numeros)
        print(f"A soma dos valores da matriz é: {n}")
        print("-" *30)
        print("Somando linhas:")
        indexLinha = int(input("Qual linha você quer comparar? (1, 2, 3): ")) - 1
        print(f"O maio número da linha é: {max(self.matriz[indexLinha])}")
        print("-" *30)
        print("Somando colunas:")
        indexColuna = int(input("Qual coluna você que somar? (1, 2, 3): ")) - 1
        coluna = []
        for linha in self.matriz:
            coluna.append(linha[indexColuna])
        print(f"A soma da coluna é: {sum(coluna)}")
        print("-" *30)

        
            

def main():
    while True:
        print("matriz:")
        matriz = Matriz()
        matriz.inserindoValores()
        matriz.exibirMatriz()
        matriz.analisandoMatriz()

        continuar = input("\nDesejá recomeçar? (s/n) ").lower()
        if continuar != "s":
            print("Até a proxima!")
            break
        else:
            print("...Reiniciando prorama...")
            continue   
    
if __name__ == "__main__":    
    main()
