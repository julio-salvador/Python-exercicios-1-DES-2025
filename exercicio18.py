nota1 = float(input("Nota da primeira prova: "))
peso1 = float(input("Peso da primeira nota: "))

nota2 = float(input("Nota da segunda prova: "))
peso2 = float(input("Peso da segunda nota: "))

media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

print("Média ponderada final:", round(media_ponderada, 2))