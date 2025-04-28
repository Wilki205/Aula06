A = [0]*3
M = [0]*3
for i in range (3):
    A[i] = int(input("Digite um numero: "))
X = int(input("Digite novo valor: "))
for i in range(3):
    M[i] = A[i] * X
print (M)