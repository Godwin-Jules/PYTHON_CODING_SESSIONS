dictionnaire = {
    "firstname": "Joe",
    "name": "Doe"
}
lst = ["Doe", "Joe"]

firstname = "Joe"
name = "Doe"


def greet(name, firstname):
    print(
        f"Bonjour {firstname} {name} ! J'espère que vous allez bien aujourd'hui.")


print("EXPLOITATION DES DONNEES D'UN DICTIONNAIRE DANS UNE FONCTION")
print("*** Utilisation normale 1 ****")
greet("Doe", "Joe")
print("*** Utilisation normale 2 ****")
greet(name, firstname)
print("*** Utilisation normale 3 ****")
greet(firstname=firstname, name=name)
print("*** Utilisation du dictionnaire ****")
greet(**dictionnaire)
print("*** Utilisation d'une liste ****")
greet(*lst)

all_trials = {
    "facile": {
        1: [23, 43, 54],
        2: [23, 67, 34, 67, 34]
    },
    "intermediaire": "",
    "difficile": ""
}

# RESUME
liste = []
dictionnaire = {"key": "value"}

dcd = {
    0: {
        "name": "Doe",
        "firstname": "Joe",
        "age": 24,
        "parents": {
            "mere": {
                "nom": "ADAMA",
                "prenom": "Afi",
                "profession": "Présidente"
            },
            "pere": {
                "nom": "KPODAR",
                "prenom": "Koffi",
                "profession": "Président"
            }
        }
    },
    1: {
        "name": "Doe",
        "firstname": "Joe",
        "age": 24,
        "parents": {
            "mere": {
                "nom": "ADAMA",
                "prenom": "Afi",
                "profession": "Présidente"
            },
            "pere": {
                "nom": "KPODAR",
                "prenom": "Koffi",
                "profession": "Président"
            }
        }
    },
    "saluer": greet
}

set = {}
salutation = dcd["saluer"]
print(salutation)

# student_grades = {}

# math_grades = student_grades.get("Alice", {})
# math_grades["math"] = 90
# print(math_grades)
# print(student_grades)

# english_grades = student_grades.setdefault("Alice", {})
# print(english_grades)
# print(student_grades)

# english_grades["english"] = 85
# english_grades["french"] = 75
# print(english_grades)
# print(student_grades)

numbers = [1, 3, 5, 7, 9]
find = 4

for num in numbers:
    if num == find:
        print(f"Found {find} in the list.")
else:
    print(f"{find} was not found in the list.")


def danser():
    """
    jsdfghujoiuytrfcgvhj,k

    :param args: onjn
    :return: ouhj
    https://www.sphinx-doc.org/en/master/tutorial/describing-code.html
    """
    ...


def mutable_immutable():
    """
    MUTABLE: can change
        - list
        - set
        - dict
        - any other thing from library
    IMMUTABLE: cannot change
        - str
        - int
        - float
        - bool
        - bytes
        - tuple
        """
    ...
