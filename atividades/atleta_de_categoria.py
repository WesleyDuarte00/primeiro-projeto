idade= int(input("Digite a idade do atleta:"))

if idade <=9:
    print("Cartegoria Mirim")
elif idade <=14:
     print("Cartegoria Infantil")
elif idade <=19:
     print("Cartegoria Junior")
elif idade <=25:
     print("Cartegoria Senior")
else:
     print("Cartegoria Master")
