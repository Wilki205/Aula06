nomes = ["","","","",""]
for x in range(len(nomes)):
    nomes[x]=input(f"digite o nome {x+1}: ")
print (nomes)
nome = input("Digite o nome que deseja buscar: ")
for i in range (len(nomes)):
    if nome == nomes[i]:
        print (f"nome {nome} encontrado na posição {i}!")
