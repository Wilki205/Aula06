n = [0]*10

for i in range(10):
    n[i] = int(input("Digite um número:"))

print("\nNúmeros pares:")
for numero in n:
    if numero % 2 == 0:
        print(numero)
maior = n[0]
menor = n[0]
for i in range(1, 10):
    if n[i] < menor:
        menor = n[i]
    if n[i] > maior:
        maior = n[i]

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")

soma = 0
for i in range(10):
    soma += n[i]
media = soma / 10

maioresQueMedia = 0
for i in range(10):
    if n[i] > media:
        maioresQueMedia += 1

print(f"\nMédia dos valores: {media:.2f}")
print(f"Quantidade de valores maiores que a média: {maioresQueMedia}")
