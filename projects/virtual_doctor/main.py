"""Projet Docteur Virtuel incorporant le calcul de l'IMC: Indice de Masse Corporel"""

import os
import json

ROOT_PATH = r"D:\PROJECTS\ORIGINALS\PYTHON_CODING_SESSIONS\projects\virtual_doctor\database"

SEX: dict[int, str] = {
    1: "Masculin",
    2: "Féminin"
}

# QUALITIES: dict[int, str] = {
#     1: "IMC € ]*, 18.5[",
#     2: "IMC € [18.5, 25[",
#     3: "IMC € [25, 30[",
#     4: "IMC € [30, 35[",
#     5: "IMC € [35, 40[",
#     6: "IMC € [40, *[",
# }

QUALITIES: dict[int, str] = {
    1: "** < IMC < 18.5",
    2: "18.5 < IMC < 25",
    3: "25 < IMC < 30",
    4: "30 < IMC < 35",
    5: "35 < IMC < 40",
    6: "40 < IMC < **",
}

QUALIFICATIONS: dict[int, str] = {
    1: "Maigreur, Sous-poids",
    2: "Corpulence normale",
    3: "Surpoids",
    4: "Obésité (modérée)",
    5: "Obésité sévère",
    6: "Obésité morbide ou massive"
}


def connexion(clear: bool) -> dict[str, str | int | float]:
    if clear:
        if os.name == "nt":
            os.system("cls")
        elif os.name == "linux":
            os.system("clear")

        print("\n\t\t---------------------------------")
        print("\t\t|     Projet Docteur Virtuel\t|")
        print("\t\t---------------------------------")

        print("\n\tBienvenue sur notre plateforme de consultation medicale virtuelle")

    while True:
        print("\nVeuillez vous connecter à la plateforme")
        print("[1] - Se connecter")
        print("[2] - S'inscrire")

        try:
            user_choice: int = int(input("Veuillez faire un choix : "))
            if user_choice == 1:
                users: list = getJsonFileContent("users.json")  # type:ignore
                if len(users) == 0:
                    print("\n\t(0) utilisateur enregistré dans la base de données")
                    print("\tVeuillez créer un compte")
                    return {}
                else:
                    print(
                        f"\n\t\tListe de tous les utilisateurs enregistrés dans la base de données : ({len(users)})\n")
                    for index, user in enumerate(users):
                        print(
                            f"\t{index + 1} - {user["surname"]} {user["names"]}")

                    while True:
                        try:
                            print(
                                "\nSaisir le numéro correspondant à votre identité")
                            choice = int(input("Veuillez faire un choix : "))
                            if choice < 1:
                                continue
                            user = users[choice - 1]
                            return user
                        except Exception as e:
                            print("Saisie incorrecte, veuillez reprendre.", e, "\n")
            elif user_choice == 2:
                user: dict[str, str | int | float] = createUser()
                print(
                    "\nVeuillez compléter votre inscription en fournissant certaines informations supplémentaires")
                sex, taille, poids = getUserInfo()
                bmi = computeBMI(taille, poids)
                user["sex"] = sex
                user["height"] = taille
                user["weight"] = poids
                user["ideal_weight"] = computePoidsIdeal(taille, sex)
                user["BMI"] = bmi
                user["qualification"] = getQualification(bmi)
                addUser(user)
                return user
            else:
                print("Veuillez faire un choix entre [1] et [2]")
                continue
        except:
            print("Saisie incorrecte, veuillez réessayer !")
            continue


def createUser() -> dict:
    print("\n\tCREATION D'UN NOUVEAU COMPTE UTILISATEUR\n")
    id: int = 0
    nom: str = input("Votre nom : ")
    prenoms: str = input("Votre (Vos) prénom(s) : ")
    while True:
        try:
            age: int = int(input("Votre âge : "))
            if age < 0:
                print("L'âge est toujours supérieur ou égal à 0")
                continue
            else:
                break
        except Exception as error:
            print("Saisie incorrecte :", error)

    profession: str = input("Votre profession : ")
    email: str = input("Votre adresse email : ")
    country: str = input("Votre pays d'origine : ")
    location: str = input("Votre lieu de résidence : ")

    nom = validateName(nom, "unknown").upper()
    prenoms = validateName(prenoms, "guest").title()
    profession = validateName(profession, "unknown").upper()
    email = validateName(email, "unknown", True).lower()
    country = validateName(country, "Unknown").title()
    location = validateName(location, "Unknown").title()

    last_id: dict = getJsonFileContent("id_increment.json")  # type:ignore
    id = last_id["increment"] + 1
    last_id["increment"] += 1
    updateJsonFileContent("id_increment.json", last_id)

    user: dict[str, str | int] = {
        "id": id,
        "surname": nom,
        "names": prenoms,
        "age": age,
        "profession": profession,
        "email": email,
        "country": country,
        "location": location,
    }
    print("\n\tVotre compte a été créé avec succès")
    return user


def validateName(name: str, default: str, email: bool = False) -> str:
    if len(name) < 3:
        return default
    else:
        if email:
            return name
        elif (name.strip().isalpha() |
              name.replace("-", "").isalpha() |
              name.replace(" ", "").replace("-", "").isalpha()):
            return name
        else:
            return default


def addUser(user: dict) -> None:
    users: list = getJsonFileContent("users.json")  # type:ignore
    users.append(user)
    response = updateJsonFileContent("users.json", users)
    if response:
        print("Utilisateur enregistré avec succès dans la base de données")
    else:
        print("Erreur lors de l'enregistrement de l'utilisateur")


def getJsonFileContent(relative_path: str) -> dict | list | None:
    try:
        with open(f"{ROOT_PATH}\\{relative_path}", "r") as jsonFile:
            content: dict | list = json.load(jsonFile)
            return content
    except Exception as e:
        print("Erreur lors de la lecture du fichier :", e)
        return None


def updateJsonFileContent(relative_path: str, content: list | dict) -> bool:
    try:
        with open(f"{ROOT_PATH}\\{relative_path}", "w") as jsonFile:
            json.dump(content, jsonFile, indent=4)
            return True
    except Exception as e:
        print("Erreur lors de l'écriture dans le ficher :", e)
        return False


def getUserInfo() -> tuple[int, float, float]:
    while True:
        while True:
            try:
                print("\nVeuillez choisir votre sexe !")
                print("\t[1] - Masculin")
                print("\t[2] - Féminin")
                sexe = input("Votre choix (1 ou 2) : ")
                sexe = int(sexe)
                if (sexe not in [1, 2]):
                    print("Saisie Incorrecte (saisir 1 ou 2)\n")
                    continue
                else:
                    break
            except Exception as e:
                print("Saisie Incorrecte :", e, "\n")

        while True:
            try:
                taille = input("Veuillez votre taille (en cm) : ")
                taille = float(taille)
                if (taille <= 0):
                    print("La taille ne peut pas être inférieure ou égale à 0\n")
                    continue
                else:
                    break
            except Exception as e:
                print("Saisie Incorrecte :", e, "\n")

        while True:
            try:
                poids = input("Veuillez votre poids (en Kg) : ")
                poids = float(poids)
                if (poids <= 0):
                    print("Le poids ne peut pas être inférieur ou égal à 0\n")
                    continue
                else:
                    break
            except Exception as e:
                print("Saisie Incorrecte :", e, "\n")

        print("\nINFORMATIONS SAISIES")
        print(f"* {"SEXE":8s} :   {SEX[sexe]}")
        print(f"* {"TAILLE":8s} :   {taille/100}m")
        print(f"* {"POIDS":8s} :   {poids}Kg")

        print("\nVous voulez continuer ou modifier les informations ?")
        valid = input("(o/O) pour modifier, *any pour continuer : ")
        if valid not in ["o", "O"]:
            break

    return sexe, taille, poids


def computePoidsIdeal(taille: float, sex: int) -> float:
    return taille - 100 - (taille - 150)/4 if sex == 1 else taille - 100 - (taille - 120)/4


def computeBMI(taille: float, poids: float) -> float:
    return round(poids/((taille * 0.01) ** 2), 2)


def getQualification(bmi: float) -> int:
    if 0 < bmi < 18.5:
        return 1
    elif 18.5 <= bmi < 25:
        return 2
    elif 25 < bmi < 30:
        return 3
    elif 30 < bmi < 35:
        return 4
    elif 35 < bmi < 40:
        return 5
    elif bmi > 40:
        return 6
    else:
        return 0


def showUserInfos(user: dict[str, str | int | float]) -> None:
    qualification: int = user.get("qualification", 0)  # type:ignore

    print("\n\n\tAFFICHAGE DES INFORMATIONS UTILISATEUR")
    print(f"\t* {"Nom":30s} : {user.get("surname")}")
    print(f"\t* {"Prénom(s)":30s} : {user.get("names")}")
    print(f"\t* {"Sexe":30s} : {SEX[user.get("sex")]}")   # type:ignore
    print(f"\t* {"Âge":30s} : {user.get("age")}")
    print(f"\t* {"Adresse email":30s} : {user.get("email")}")
    print(f"\t* {"Profession":30s} : {user.get("profession")}")
    print(f"\t* {"Pays":30s} : {user.get("country")}")
    print(f"\t* {"Quartier":30s} : {user.get("location")}")

    print(f"\t* {"Taille":30s} : {user.get("height") / 100}m")    # type:ignore
    print(f"\t* {"Poids":30s} : {user.get("weight")}Kg")
    print(f"\t* {"Poids Idéal":30s} : {user.get("ideal_weight")}Kg")
    print(f"\t* {"IMC (Indce de Masse Corporel)":30s} : {user.get("BMI")}")

    print(f"\t* {"APPRECIATION":30s} : {QUALIFICATIONS[qualification]}\n")


def showUserInfo(user: dict[str, str | int | float]) -> None:
    qualification: int = user.get("qualification", 0)   # type:ignore

    print("\n\n\tRESULTATS DE L'ANALYSE")
    print(f"\t* Votre poids idéal est : {user.get("ideal_weight", 0)}Kg")
    print("\t* Votre Indice de Masse Corporel (IMC) est :", user.get("BMI", 0))
    print(f"\t* APPRECIATION : {QUALIFICATIONS[qualification]}\n")


def updateUser():
    ...


def deleteUser():
    ...


def main() -> None:

    # Récupération des données utilisateur grâce au processus de connexion à la plateforme "Virtual Doctor"
    clear = True
    while True:
        user: dict[str, str | int | float] = connexion(clear)
        if len(user) == 0:
            print("\nVeuillez vous connecter à la plateforme avant de continuer\n")
            clear = False
            continue
        else:
            showUserInfo(user)
            showUserInfos(user)
            break


if __name__ == "__main__":
    main()
