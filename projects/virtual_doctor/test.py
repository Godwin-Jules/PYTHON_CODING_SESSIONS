import json

from matplotlib.pyplot import step


# Ecrtiture dans un fichier : Manipulation classique d'un fichier
fichier = open("projects/virtual_doctor/reading.txt", "w", encoding="utf-8")

donne = "Tout ce que je veux, je peux l'écrire dedans"
fichier.write(donne)

fichier.close()


# Lecture d'un fichier : Manipulation classique d'un fichier
with open("projects/virtual_doctor/reading.txt", "+w", encoding="utf-8") as fichier:
    donne = "Tout ce que je veux, je peux le mettre dans mon fichier txt"
    fichier.write(donne)


# Ecriture dans un fichier JSON
with open("projects/virtual_doctor/testing.json", "w") as testing:
    data = {
        "name": "UNKNOWN",
        "surname": "JSON",
        "âge": 27
    }
    # testing.write(str(data))
    json.dump(data, testing, indent=2)


# Lecture d'un fichier JSON
with open("projects/virtual_doctor/testing.json", "r") as testing:
    data = json.load(testing)
    print("\n", data, "\n", sep="")
    for el in data:
        print("*", el, ":", data[el])
