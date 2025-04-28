notas = [0,0,0,0,0]
soma = 0
cont = 0
for x in range (len(notas)):
    notas [x] = float(input("Digite nota: "))
for y in range (len(notas)):
    soma += notas [y]
media = soma/(len(notas))
for z in range(len(notas)):
    if notas [z] > media:
        cont = cont +1
print(f"Média das notas: {media:.2f}")
print(f"{cont} aluno(s) ficaram acima da média.")