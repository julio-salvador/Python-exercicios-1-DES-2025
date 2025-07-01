# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)

meta1 = int(input("Digite a média da meta 1: "))
meta2 = int(input("Digite a média da meta 2: "))
meta3 = int(input("Digite a média da meta 3: "))
indice = meta1 + meta2 + meta3 / 3

if indice >=7:
    print("muito bem, vocẽ foi aprovado.")
elif indice >=5 <7:
    print("Vocẽ está fazendo o treinamento no treinamento.")
else:
    print("Uma pena, mas vocẽ não foi aprovado.")