hauteur = int(input("Taille: "))

for i in range(hauteur):
    espaces = hauteur - i - 1
    print(" "*espaces + "x"*(i*2+1))