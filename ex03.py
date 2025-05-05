nomes = ["", "", "", "", ""]

for i in range(len(nomes)):
    nomes[i] = input(f"Digite um nome {i+1}: ")

for nome in nomes:
    print(nome)

nome = input("Digite um nome para buscar: ")
encontrado = 0

for j in range(len(nomes)):
    if nome == nomes[j]:
        print(f"Nome '{nome}' encontrado na posição {j}!")
        encontrado += 1

if encontrado == 0:
    print("Nome não encontrado!")
