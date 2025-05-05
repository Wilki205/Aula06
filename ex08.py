N = int(input("Digite um valor: "))
A = []
B = []

for i in range (N):
    A.append(int(input(f"A[{i}]: ")))
for j in range (N):
    B.append(int(input(f"B[{j}]: ")))

soma = [A[i] + B[j] for k in range (N)]

print(soma)