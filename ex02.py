nomes = ["", "", "", "", ""]

for x in range(len(nomes)):
    nomes[x] = input(f"Digite o nome {x+1}: ")

print(nomes)

nome = input("Digite o nome que deseja buscar: ")
encontrado = 0  

for i in range(len(nomes)):
    if nome == nomes[i]:
        print(f"Nome '{nome}' encontrado na posição {i}!")
        encontrado = 1

if encontrado == 0:
    print("Nome não existe.")
