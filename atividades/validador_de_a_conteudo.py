ano_nasc = float(input("Digite ano de nascimento:"))
idade = 2026 - ano_nasc
if idade > 16:
    print("acesso liberado:")
else:
    print("acesso bloqueado:")