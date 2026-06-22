# Leitura do valor total das compras
valor_original = float(input("Digite o valor total da compra (R$): "))

# Estrutura condicional para definir o percentual de desconto
if valor_original <= 100.00:
    percentual_desconto = 0
elif valor_original <= 300.00:
    percentual_desconto = 5
elif valor_original <= 500.00:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# Cálculos
valor_desconto = valor_original * (percentual_desconto / 100)
total_a_pagar = valor_original - valor_desconto

# Exibição dos resultados (formatados com 2 casas decimais)
print(f"\n--- Resumo da Compra ---")
print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto aplicado: {percentual_desconto}% (R$ {valor_desconto:.2f})")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")