user = [""]*1
senha = [0]*1

for i in range (len(user)):
    user[i] = input("Usuario: ")
    senha[i] = int(input("senha: "))
login = input("User: ")
password = int(input("Password: "))

for i in range (len(user)):
    if user[i] == login and senha [i] == password:
        login = True
        print ("Login efetuado com sucesso!")
        break
else:
    print("acesso negado!")
