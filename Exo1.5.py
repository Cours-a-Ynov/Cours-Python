price = input('Object price? ')
given = input('Money given? ')
# Calculer la différence entre le prix de l'objet, et l'argent donné
delta = int(given) - int(price)
# Si le delta est négatif, alors on a pas donné assez d'argent
if delta < 0:
    print(f'Not enough money given: {delta}')
else:
    # Si le delta est supérieur à 500 (càd: si il faut rendre au moins 500€)
    if delta > 500:
        # Alors il faudra rendre au moins 1 billet de 500€. Combien ?
        # On va utiliser l'opérateur de division entière (//)
        # Exemple: 1200 // 500 = 2 (il faut donc rendre 2 billet de 500)
        print(f'500€ x {delta // 500}')
        # Après avoir donné les billets de 500, combien reste-t'il d'argent à rendre ?
        # On va utiliser l'opérateur modulo (%) (= le reste de la division entière!)
        # Exemple: 1200 // 500 = 200 (il reste 200€ à rendre)
        delta %= 500
    # On recommence avec les billets de 200
    if delta > 200:
        print(f'200€ x {delta // 200}')
        delta %= 200

    # Puis 100
    if delta > 100:
        print(f'100€ x {delta // 100}')
        delta %= 100

    # Etc...
    if delta > 50:
        print(f'50€ x {delta // 50}')
        delta %= 50
    if delta > 20:
        print(f'20€ x {delta // 20}')
        delta %= 20
    if delta > 10:
        print(f'10€ x {delta // 10}')
        delta %= 10
    if delta > 5:
        print(f'5€ x {delta // 5}')
        delta %= 5
    if delta > 2:
        print(f'2€ x {delta // 2}')
        delta %= 2
    if delta > 1:
        print(f'1€ x {delta // 1}')
        delta %= 1
    print('Done!')