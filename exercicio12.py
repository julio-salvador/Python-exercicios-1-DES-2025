senha = input("Crie sua senha: ")

if senha[7:8] != "":
    print("Senha aceita com sucesso.")
else:
   print("Sua senha está muito curta.")