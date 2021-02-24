from random import randint
nombre = randint(1,100)
vies = 6
while vies > 0:
    essai = int(input("Nombre entre 1 et 100: "))
    if essai == nombre:
        print(f"Félicitation! Le nombre était bien {nombre}")
        break
    elif essai < nombre:
        print("C'est plus!")
    elif essai > nombre:
        print("C'est moins!")
    vies-=1
else:
    print(f"Retente une prochaine fois!")