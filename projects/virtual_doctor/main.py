"""Projet Docteur Virtuel incorporant le calcul de l'IMC: Indice de Masse Corporel"""
from ast import Return
import os

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
                    print("Saisie Incorrecte (saisir 1 ou 2)")
                    continue
                else:
                    break
            except Exception as e:
                print("Saisie Incorrecte :", e)

        while True:
            try:
                taille = input("\nVeuillez votre taille (en cm) : ")
                taille = float(taille)
                if (taille <= 0):
                    print("La taille ne peut pas être inférieure ou égale à 0")
                    continue
                else:
                    break
            except Exception as e:
                print("Saisie Incorrecte :", e)

        while True:
            try:
                poids = input("\nVeuillez votre poids (en Kg) : ")
                poids = float(poids)
                if (poids <= 0):
                    print("Le poids ne peut pas être inférieur ou égal à 0")
                    continue
                else:
                    break
            except Exception as e:
                print("Saisie Incorrecte :", e)

        print("\nINFORMATIONS SAISIES")
        print(f"* SEXE : {SEX[sexe]}")
        print(f"* TAILLE : {taille/100}m")
        print(f"* POIDS : {poids}Kg")

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


def main() -> None:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "linux":
        os.system("clear")

    print("\n\t\t---------------------------------")
    print("\t\t|     Projet Docteur Virtuel\t|")
    print("\t\t---------------------------------")

    sexe, taille, poids = getUserInfo()
    poids_ideal = computePoidsIdeal(taille, sexe)
    bmi = computeBMI(taille, poids)
    qualification = getQualification(bmi)
    print("\n\n\tRESULTATS DE L'ANALYSE")
    print(f"\t* Votre poids idéal est : {poids_ideal}Kg")
    print("\t* Votre Indice de Masse Corporel (IMC) est :", bmi)
    print("\t* APPRECIATION :", QUALIFICATIONS[qualification], "\n")


if __name__ == "__main__":
    main()
