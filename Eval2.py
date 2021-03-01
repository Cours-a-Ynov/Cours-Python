a = float(input("Longueur a: "))
b = float(input("Longueur b: "))
c = float(input("Longueur c: "))

if a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b:
    print("rectangle")
else:
    print("pas rectangle")