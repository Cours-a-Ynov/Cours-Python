mot = "BANANE"
list_word = list(mot)
hidden_word = "_" * len(mot)
list_hidden_word = list(hidden_word)
print(f"Mot à trouver: {hidden_word}")
test_number = 0
while test_number < 6:
    if mot == ''.join(list_hidden_word):
        print("Gagné")
        break
    letter = input("Entrer une lettre: ")
    isgood = False
    for j in range(len(mot)):
        if letter == mot[j]:
            list_hidden_word[j] = letter
            isgood = True
    if isgood == False:
        print("Faux!")
        test_number += 1
    print(f"Voici le mot à présent: {''.join(list_hidden_word)}")
else:
    print("Perdu... :(")
