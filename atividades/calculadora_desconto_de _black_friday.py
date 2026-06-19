# Entrada de dados do usuário
usuario = input("Digite o nome de usuário: ")
token = int(input("Digite a chave de segurança (token inteiro): "))

# Verificação de segurança usando o operador lógico 'and'
if usuario == "admin" and token == 9988:
    print("Acesso concedido. Bem-vindo!")
else:
    print("Dados de acesso inválidos")