import json

# Lire un fichier:
with open("words.txt", "r") as file:
    lines = file.read().splitlines()
    print(lines)

# Ecrire dans un fichier:
with open("words.txt", "w") as file:
    newWords = ["Chocolat", "Vanille", "Fraise"]
    file.write('\n'.join(newWords))

# Comment ajouter un nouveau mot/une nouvelle ligne? 🤔
# Il suffit de:
#   1) Lire le fichier et le stocker dans une variable (liste)
#   2) Ajouter un mot dans la variable
#   3) Ecrire la variable dans le fichier

with open("words.txt", "r") as file:
    lines = file.read().splitlines()

lines.append("Pistache")

with open("words.txt", "w") as file:
    file.write('\n'.join(lines))

#######################################################

# Lire un fichier JSON
# C'est pareil, mais on va passer par une phase de transformation Chaine de caractère -> Types Pythons (dictionnaire, ...):
with open("tweets.json", "r") as file:
    contenu = file.read() # Ici, le contenu du fichier est une simple chaine de caractère
    tweets = json.loads(contenu) # On "désérialise" vers une variable
    print(tweets)

# Ecrire dans un fichier Python
# Idem, mais cette fois-ci, on va faire l'opération inverse:
with open("tweets.json", "w") as file:
    tweets = [
        {
            "auteur": "@Thibaud",
            "message": "Le projet est à rendre pour le 21/03/2021 à 23h59!"
        },
        {
            "auteur": "@Ynov",
            "message": "Vivement les vacances"
        }
    ]
    chaineDeCaractere = json.dumps(tweets, indent=2) # On "sérialise" vers une chaine de caractère
    file.write(chaineDeCaractere)

# Comment faire pour modifier un tweets?
# Vous l'aurez compris, on va:
#   1) Lire le fichier
#   2) Désérialiser le contenu
#   3) Modifier le contenu
#   4) Sérialiser le contenu
#   5) Ecrire dans le fichier

with open("tweets.json", "r") as file:
    tweets = json.loads(file.read()) # Note: On peut lire et désérialiser en une seule ligne

tweets[0]["auteur"] = "@Errorname_" # Ici on modifie l'auteur du premier Tweet

with open("tweets.json", "w") as file:
    file.write(json.dumps(tweets, indent=2)) # Note: On peut aussi sérialiser et écrire en une seule ligne

######################################################

# Comment faire "un tweet dans un tweet"?

# Un tweet ? => Un dictionnaire
unTweet = {
    "auteur": "@Jack",
    "message": "Yes"
}

# Des tweets ? => Une liste de dictionnaires
desTweets = [
    {
        "auteur": "@Jack",
        "message": "Yes"
    },
    {
        "auteur": "@Jane",
        "message": "Oui"
    }
]

# Un tweets qui "possède" des tweets en réponse ? => Un dictionnaire qui possède une liste de dictionnaires
unTweetsAvecDesTweets = {
    "auteur": "@Errorname_",
    "message": "Vivement les vacances",
    "reponses": [
        {
            "auteur": "@Jack",
            "message": "Yes"
        },
        {
            "auteur": "@Jane",
            "message": "Oui"
        }
    ]
}

# Et si je veux modifier le message du deuxième tweets en réponse au tweet?
unTweetsAvecDesTweets["reponses"][1]["message"] = "Oui, carrément."