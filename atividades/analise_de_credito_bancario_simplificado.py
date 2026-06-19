salario_bruto = float(input("Digite o salário bruto:"))
valor_da_parcela = float(input("Digite o valor da parcela:"))

if valor_da_parcela <= salario_bruto *0.30:
    print("Aprovado")
else:
    print("Reprovado")