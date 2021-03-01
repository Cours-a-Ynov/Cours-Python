name = int(input('Nom (perso 1) : '))
x = int(input('Point de vie (perso 1) : '))
y = int(input('Point dattack (perso 1) : '))
z = int(input('Point de defense(perso 1) : '))
name2 = int(input('Nom (perso 2) : '))
x2 = int(input('Point de vie (perso 2) : '))
y2 = int(input('Point dattack (perso 2) : '))
z2 = int(input('Point de defense (perso 2) : '))

class Character:
    def __init__(self, name, pv, attaque, defense):
        self.name = name
        self.pv = pv
        self.attaque = attaque
        self.defense = defense

    def is_alive(self):
        if (self.pv > 0):
            return True
        else:
            return False

    def attack(self, c2):
        degats = self.attaque - c2.defense
        if (degats >=0):
            c2.pv = c2.pv - degats

c1 = (name, x, y, z)
c2 = (name2, x2, y2, z2)

print(name.isalive())

name.attck(name2)
name2.attck(name)

print(f"{name.name}: {name.pv}PV / {name2.name}: {name2.pv}PV")