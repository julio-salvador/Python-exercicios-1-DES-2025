valor = float(input("Informe o total da compra: "))
valor_final = valor

if valor > 500:
    valor_final = valor - (valor * 0.10)
elif valor > 300:
   valor_final = valor - (valor * 0.05)
print("Total com desconto: R$", round(valor_final, 2))