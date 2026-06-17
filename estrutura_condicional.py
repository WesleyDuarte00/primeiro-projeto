# Casar ou comprar uma bicicleta ?

print("Casar ou comprar uma bicicleta ?")

resposta = input("Você está gordo ? s/n")

if resposta == "s":
    quer_emagrecer = input("Você quer emagrecer ?")
    if quer_emagrecer == "s":
        print("compre uma bicicleta")
    else:
        print("Então case")
else:
    quer_engordar = input("Você quer engordar ? s/n")
    if quer_engordar == "s":
        print("Então case!")
    else:
        print("Compre uma bicicleta!")



