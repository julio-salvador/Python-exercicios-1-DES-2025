# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.
internet = int(input("Digite o consumo de internet"))
if internet > 100:
    print(f"O consumo da internet ({internet}) foi ultrapassado.")
else:
    print(f"O limite ({internet}) não foi ultrapassado.")

