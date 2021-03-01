valeur = float(input("Distance: "))
type = input("K or L: ")

if type == "K":
    valeur = valeur/4.828
    print(valeur)
elif type == "L":
    valeur = valeur*4.828
    print(valeur)
else:
    print("Please select a correct type (K or L)")