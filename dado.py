import random
input("Pressione o enter para lançar o dado")

resultado = random.randint(1,14)
print (f"O dado rolou : {resultado}" );
if resultado > 12:
    print("Já ta mais sortudo que o Leclerc")
elif resultado < 11:
    print("Agora ta sortudo igual o Alonso")




