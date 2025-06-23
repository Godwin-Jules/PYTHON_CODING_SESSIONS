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

    print("\n\n\tAFFICHAGE DES INFORMATIONS UTILISATEUR\n")
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


def updateUser(user: dict[str, str | int | float]) -> bool:
    print("\n\tMISE A JOUR DES DONNEES UTILISATEUR\n")
    print("Voici vos données actuelles dans notre base de données", sep="")
    showUserInfos(user)
    print("\nVeuillez remplir seulement le champ des informations à modifier\n")

    id: int = user.get("id")  # type:ignore
    nom = validateName(input("Votre nom : "), user.get(
        "surname")).upper()  # type:ignore

    prenoms = validateName(input("Votre (Vos) prénom(s) : "),
                           user.get("names")).title()  # type:ignore

    try:
        age: int = int(input("Votre âge : "))
        if age < 0:
            print("L'âge est toujours supérieur ou égal à 0")
            age = user.get("age")  # type:ignore
    except:
        age = user.get("age")  # type:ignore

    profession = validateName(input("Votre profession : "), user.get(
        "profession")).upper()  # type:ignore

    email = validateName(input("Votre adresse email : "),
                         user.get("email"), True).lower()  # type:ignore

    country = validateName(input("Votre pays d'origine : "),
                           user.get("country")).title()  # type:ignore

    location = validateName(input("Votre lieu de résidence : "), user.get(
        "location")).title()  # type:ignore

    try:
        print("\n\t[1] - Masculin")
        print("\t[2] - Féminin")
        sexe = int(input("Votre sexe (1 ou 2) : "))
        if (sexe not in [1, 2]):
            sexe: int = user.get("sex")  # type:ignore
    except:
        sexe: int = user.get("sex")  # type:ignore

    try:
        taille = float(input("Veuillez votre taille (en cm) : "))
        if (taille <= 0):
            taille: float = user.get("height")  # type:ignore
    except:
        taille: float = user.get("height")  # type:ignore

    try:
        poids = float(input("Veuillez votre poids (en Kg) : "))
        if (poids <= 0):
            poids: float = user.get("weight")  # type:ignore
    except:
        poids: float = user.get("weight")  # type:ignore

    bmi: float = computeBMI(taille, poids)

    print("\nÊtes-vous sûr de modifier ces informations ?")

    if input("(o/O) pour modifier, *any pour continuer : ") not in ["o", "O"]:
        return False
    else:
        user["surname"] = nom
        user["names"] = prenoms
        user["age"] = age
        user["profession"] = profession
        user["email"] = email
        user["country"] = country
        user["location"] = location
        user["sex"] = sexe
        user["height"] = taille
        user["weight"] = poids
        user["ideal_weight"] = computePoidsIdeal(taille, sexe)
        user["BMI"] = bmi
        user["qualification"] = getQualification(bmi)

        users: list[dict] = getJsonFileContent("users.json")  # type:ignore
        index = 0
        for idx, el in enumerate(users):
            if el.get("id") == id:
                index = idx
                break
        users[index] = user
        response = updateJsonFileContent("users.json", users)
        if response:
            print("\n\tModification enregistrée avec succès !")
            showUserInfos(users[index])
            return True
        else:
            print("\nModification non enregistrée")
            return False


def deleteUser(user: dict[str, str | int | float]) -> bool:
    id: int = user.get("id")  # type:ignore
    print("\nÊtes-vous sûr de supprimer votre compte ainsi que toutes vos données peresonnelles ?")

    if input("(o/O) pour supprimer, *any pour continuer : ") not in ["o", "O"]:
        print("Suppression du compte utilisateur annulée")
        return False
    else:
        users: list = getJsonFileContent("users.json")  # type:ignore
        index = 0
        for idx, el in enumerate(users):
            if el.get("id") == id:
                index = idx
                break
        users.pop(index)
        response = updateJsonFileContent("users.json", users)
        if response:
            showUserInfos(user)
            print("\nSuppression de votre compte effectuée avec succès")
            return True
        else:
            print("Erreur lors de la suppression du compte utilisateur")
            return False


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
            break

    while True:

        print("\n\tQuelle opération voulez-vous effectuer sur cette plateforme ?")
        print("\nVeuillez faire un choix parmi le menu ci-après")

        print("[1] - Consulter ses informations médicales")
        print("[2] - Consulter toutes ses informations personnelles")
        print("[3] - Modifier ses informations personnelles")
        print("[4] - Se déconnecter")
        print("[5] - Supprimer votre compte")

        while True:
            try:
                user_choice = int(input("\nQuel est votre choix : "))
                if user_choice < 1 and user_choice > 4:
                    print("\nChoix incorrect, faire un choix entre [1] et [4]")
                break
            except Exception as e:
                print("\n\tSaisie incorrecte :", e)
                continue

        if user_choice == 1:
            showUserInfo(user)
        elif user_choice == 2:
            showUserInfos(user)
        elif user_choice == 3:
            response = updateUser(user)
            if response:
                print("Mise à jour effectuée avec succès")
            else:
                print(
                    "\nLa mise à jour de vos données personnelles s'est terminée avec échec, veuillez reprendre")
        elif user_choice == 4:
            print(
                "\n\n\t---------- MERCI DE VOTRE VISITE SUR LA PLATEFORME \"VIRTUAL DOCTOR\" ----------\n")
            break
        elif user_choice == 5:
            response = deleteUser(user)
            if response:
                print("\nVotre compte a été supprimé\n\tVeuillez vous connecter !")
                break
            else:
                print("\nErreur lors de la suppression du compte utilisateur")


if __name__ == "__main__":
    main()
