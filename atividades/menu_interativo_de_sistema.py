while True:
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        print("Encerrando o programa...")
        break

    if opcao >= 1 and opcao <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado:", num1 + num2)

        elif opcao == 2:
            print("Resultado:", num1 - num2)

        elif opcao == 3:
            print("Resultado:", num1 * num2)

        elif opcao == 4:
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Erro: divisão por zero!")




    else:
        print("Opção inválida!")