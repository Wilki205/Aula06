user = [""]*3
for i in range (3):
    user[i] = input("Digite um nome para user: ")
print("Normal:")
for nome in user:
    print(nome)
print("Inverso:")
for j in range(2, -1, -1):
    print(user[j])