adn = input("ADN: ")
tab = list(adn)
marqueurs = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}
for i in range(len(tab)):
    tab[i] = marqueurs[tab[i]]

# Ou:
for i in range(len(tab)):
    if tab[i] == 'A':
        tab[i] = 'T'
    elif tab[i] == 'T':
        tab[i] = 'A'
    elif tab[i] == 'C':
        tab[i] = 'G'
    elif tab[i] == 'G':
        tab[i] = 'C'
b = "".join(tab)
print(b)
