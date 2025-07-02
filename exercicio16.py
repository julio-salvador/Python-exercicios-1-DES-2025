salario = float(input("Informe seu salário atual: "))
reajuste = 0
salario_reajustado = salario

if salario <= 2000:
    reajuste = salario * 0.15
elif salario <= 5000:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05
    salario_reajustado = salario + reajuste

    print("Reajuste aplicado: R$", round(reajuste, 2))
    print("Novo salário: R$", round(salario_reajustado, 2))