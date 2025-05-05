n = [0]*3
for i in range (3):
    n[i] = int(input("Digite um numero: "))
a = int(input("Digite mais um numero: "))

contador = 0
for j in range (3):
    if n[j] == a:
        contador +=1
print(f"O número {a} aparece {contador} vez(es) no vetor.")