A = float(input("Digite o comprimento da reta A: "))
B = float(input("Digite o comprimento da reta B: "))
C = float(input("Digite o comprimento da reta C: "))

# Verifica se forma um triângulo
if A + B > C and A + C > B and B + C > A:
    print("As retas podem formar um triângulo!")

    # Classificação do triângulo
    if A == B == C:
        print("Tipo: Triângulo Equilátero")
    elif A == B or A == C or B == C:
        print("Tipo: Triângulo Isósceles")
    else:
        print("Tipo: Triângulo Escaleno")
else:
    print("As retas não podem formar um triângulo")







