# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.

curso01 = int(input("Digite quantas avaliações o curso 1 teve: "))
curso02 = int(input("Digite quantas avaliações o curso 2 teve: "))

if curso01 == curso02:
    print("Empate nas avaliações.")
elif curso01 > curso02:
    print("O curso 01 é maior.")
else:
    print("O curso 02 é maior.")


