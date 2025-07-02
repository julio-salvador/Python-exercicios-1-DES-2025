ano = int(input("Digite o ano desejado: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("Ano bissexto confirmado.")
else:
    print("Este não é um ano bissexto.")