notas = [0,0,0,0,0]
soma = 0
cont = 0

for i in range (len(notas)):
    notas [i] = float(input("DIGITE NOTA: "))
for j in range (len(notas)):
    soma += notas [j]
    media = soma/(len(notas))
for k in range(len(notas)):
    if notas [k] > media:
        cont = cont + 1
print(f"media das notas: {media:.1f}")
print(f"{cont} aluno(s) ficaram acima da media.")