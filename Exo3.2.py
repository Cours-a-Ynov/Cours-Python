word = input("Entrez un mot: ")
with open("words.txt", "r+") as file:
    #if word in file.read().splitlines():
    #    print("Word found")
    #else:
    #    file.write(f"\n{word}")
    for line in file:
        if line == word+"\n":
            print("Word found in file")
            break
    else:
        file.write(f"{word}\n")