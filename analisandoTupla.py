# Recebe os números como strings e converte para inteiros
n = (int(input("Digite um número: ")), int(input("Digite outro número: ")), 
     int(input("Digite outro número: ")), int(input("Digite outro número: ")))

par = 0
repetidos = {}

for c in n:
    if c % 2 == 0:
        par += 1    
    # Contagem de repetições
    if c in repetidos:
        repetidos[c] += 1
    else:
        repetidos[c] = 1

# Exibe a contagem de repetições
for numero, quantidade in repetidos.items():
    if quantidade > 1:
        print(f"O número {numero} se repete {quantidade} vezes")
print(f"Número par encontrado: {c}. Total de pares: {par}")
