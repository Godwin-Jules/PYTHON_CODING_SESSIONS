# REGLES ISSUES DES CONVENTIONS DE CODAGE
"""
  CONVENTIONS
    * NOMMAGE
      Il faut que les variables, les constantes et les fonctions soient représentatives :
        + Ecriture CamelCase (nomCompletEtudiant, nomCompletProf)       ->  Variables, fonctions, constantes, others
        + Ecriture PascalCase (NomCompletEtudiant, NomCompletProf)      ->  Classes
        + Ecriture SnakeCase (nom_complet_Etudiant, nom_complet_prof)   ->  variables, fonctions, constantes, others
        + Ecriture KebabCase (nom-complet-etudiant, nom-complet-prof)   ->  Non accepté en python

    * STRING (CHAINES DE CARACTERES)
      \n : nouvelle ligne
      \t : tabulation
      \r : retour chariot
      \b : retour en arrière
      \f : nouvelle page

    * NOTATION DES NOMBRES
      Depuis la version 3.10, il est possible d'écrire les nombres complexes ou difficile à lire à l'aide du séparateur "_" pour faciliter la lisibilité du code => Ex: 10_000_000

    * LES TYPES DE DONNES (VARIABLES)
          type primitif   type objet associé     place en mémoire    fourchette de valeurs
      ->  boolean         boolean                 1octet              True(1) | False(0)
      ->  char            Character               2octets             unicode : 65536 caractères disponibles
      ->  string          String                  4octets             Autant de caractères que possible
      ->  int             Integer                 4octets             -2 147 483 648 à 2 147 483 647
      ->  float           Float                   4octets             1.4 * 10^(-45) à 3.4 * 10^18
      ->  double          Double                  8octets             4.9 * 10^(-324) à 1.7 * 10^308

    * OPERATEURS
      ->  Addition              =>    +
      ->  Soustraction          =>    -
      ->  Multiplication        =>    *
      ->  Division              =>    /
      ->  Division entière      =>    //
      ->  Modulo                =>    %
      ->  Exponantiation        =>    **
"""

"""
# LES STRINGS - FORMATAGE
print("FORMATAGE DES CHAINES DE CARACTERES")
nom = "Doe"
prenom = "Jane"
age = 34

nom_complet = prenom + " " + nom
# print(prenom + " " + nom)
# print("*-------------------------------------*")
# print(nom_complet)


#   FORMATAGE AVEC L'OPERATEUR D'ADDITION DIT LA CONCATENATION
# print("Bonjour, je m'appelle", prenom, nom, "et j'ai", age, "ans")
# print("Bonjour, je m'appelle " + prenom + " " + nom + " et j'ai " + str(age) + " ans")


#LE FORMATAGE AVEC LE SYMBOLE DU POURCENTAGE
# print("Bonjour, je m'appelle %s %s et j'ai %f ans" % (prenom, nom, age))
# print("Vous avez été identifié : %s %s et vous avez %i ans !" % ("YASSINTHE", "Godwin", 17))


#   FORMATAGE AVEC LA FONCTION FORMAT - ARGUMENTS ORDONNES
chaine = "Bonjour, je m'appelle {} {} et j'ai {} ans!".format(age, nom, prenom)


#   FORMATAGE AVEC LA FONCTION FORMAT - ARGUMENTS NON ORDONNES : 
chaine_1 = "Bonjour, je m'appelle {2} {1} et j'ai {0} ans!".format(age, nom, prenom) # UTILISATION DES INDEX
chaine_2 = "Bonjour, je m'appelle {PRENOM} {NOM} et j'ai {AGE} ans!".format(AGE = age, NOM = nom, PRENOM = prenom) # AUTRE FORME
chaine_3 = "Bonjour, je m'appelle {p} {n} et j'ai {a} ans!".format(a = age, n = nom, p = prenom) # AUTRE FORME

# print("0 ---------------------------")
# print(chaine)
# print("1 ------------------------------*")
# print(chaine_1)
# print("2 ---------------------------------**")
# print(chaine_2)
# print("3 -------------------------------------***")
# print(chaine_3)


#   FORMATAGE EN UTILISANT LA FONCTION F_STRINGS
# print(f"Bonjour, je m'appelle {prenom} {nom} et j'ai {age} ans")
"""


"""
#   LES LISTES
print("\nLES LISTES")
list_01 = ["Float", "Integer", "Strings", "Double", "Boolean"]
MixedList = ["Togo", "Benin", "Bourkina-Faso", ["Accra","Hô", "Lagos", "Lomé"]]

print(len(MixedList))   # Connaître la longueur d'une liste
print(len(list_01))     # Connaître la longueur d'une liste

MixedList.append("Jr d") # Ajouter un élément à la fin d'une liste
print(MixedList)

# AFFICHER LES ELEMENTS D'UNE LISTE
print("--------------------------")
fList = ["Victor", "Gbanzo", "Gedeon", "Michel", "Josue", "David", "Victoire", "Rene", "Caleb"]
for friend in fList:
    print(friend)

print("--------------------------")

friend = 0
while friend < len(fList):
    print(fList[friend])
    friend +=1

# AFFICHAGE GRÂCE AUX INDEX CROISSANTS
print("--------------------------")
print(fList[0])
print(fList[1])
print(fList[2])
print(fList[3])

# AFFICHAGE GRÂCE AUX INDEX DECROISSANTS
print("--------------------------")
print(fList[-1])
print(fList[-2])
print(fList[-3])
print(fList[-4])
"""

"""
print("\nLES LISTES : APPROFONDISSEMENT")
ListPresentation = ["YASSINTHE", "Dieu donné K . Jules", "00228 99 88 77 66", "Etudiant en 2ème année", "UL - EPL - GL"]
print(ListPresentation)

# LES DIFFERENTES FONCTIONS UTILISEES DANS LES LISTES
#In     =>      faire une recherche ou une vérification
print("YASSINTHE" in ListPresentation)
print("name" in ListPresentation)
print("-*-*-*-*-*-*-*-*-*-*-*-*-")

#Copy   =>      copier tous les éléments d'une liste
ListCopy = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #[range(0, 11)]
print(ListCopy)
ListCopy = ListPresentation.copy()
print(ListCopy)
print("-*-*-*-*-*-*-*-*-*-*-*-*-")

#Pop    =>      supprimer un élément d'une liste à une position donnée
ListCopy.pop(0)
print(ListCopy)
print("-*-*-*-*-*-*-*-*-*-*-*-*-")

#Clear  =>      supprimer tous les éléments d'une liste donnée
print(ListCopy.clear())
print(ListCopy)
ListCopy = ["Greeting", "Hello World"]
print(ListCopy)
print("-*-*-*-*-*-*-*-*-*-*-*-*-")


# CONBINAISON DE DEUX OU PLUSIEURS LISTES
print("Combinaison de deux listes")
NewList = [*ListCopy, *ListPresentation]    # Permet de remplir une nouvelle liste avec le contenu des deux listes
print(NewList)


# LES LISTES COMPREHENSION
fruits = ['Banana', 'Apple', 'Lime']
loud_fruit = [elt.upper() for elt in fruits]
low_fruit = [fruit.lower() for fruit in fruits]
sort_fruit = fruits.sort()
print(sort_fruit)
print(fruits)
print(loud_fruit)
print(low_fruit)
print(list(enumerate(fruits)))
print("------------------------")
x = list(enumerate(["Joy", "Peace", "Happiness"]))
print(x)

# Une autre notion à connaître lorsqu'on manipule les variables: id (il permet de renvoyer à l'écran l'adresse à laquelle est stockée une variable)
print(id(x))
print(id(fruits))
print(id(enumerate(fruits)))    #   etc, etc, etc ...
# Pour toute valeur comprise entre -5 et 256, python les enregistre nativement dans la mémoire vive : c'est ce qu'on appelle le système de cache !
# Donc pour toute valeur dans cette marge, toutes les variables possèdent la même addresse en mémoire. Prenons un exemple
a = 500
print(id(a)) 
b = 500
print(id(b))
print(id(a)==id(b)
"""

"""
#   LES DICTIONNAIRES
print("\nLES DICTIONNAIRES")
dictionary = dict({"earth" : 40075, "Saturn" : 378675, "Jupiter" : 439263})
print(dictionary)

# AUTRE MANIERE DE DECLARER UNE LISTE ET DE LA REMPLIR
t0 = {}
t0[0] = 0
t0[1] = 1
t0[2] = 2
print(t0)
"""

"""
#   LES DICTIONNAIRES - APPROFONDISSEMENT

print("LES DICTIONNAIRES - APPROFONDISSEMENT")

Repertoire = {
    "nom" : "YASSINTHE",
    "prenom" : "Dieu donné",
    "age" : 19,
    "niveau_universitaire" : "2ème année",
    "numero_de_telephone" : "00228 99 88 77 66",
    "langage_de_programmation_favoris" : "Python",
    "couleur_favorie" : "Blanche",
    "est_majeur" : True,
    "bizarre" : "non"
}

print(Repertoire)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# RECUPERER LA LISTE DES VALEURS DES CLES DU DICTIONNAIRE (repertoire.values())
for i in Repertoire.values():
    print(i)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# RECUPERER LA LISTE DES CLES DU DICTIONNAIRES (repertoire.keys())
for j in Repertoire.keys():
    print(j)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# RECUPERER LES TUPLES (KEY, VALUE) DES ELEMENTS DU DICTIONNAIRES (repertoire.items())
for i,j in Repertoire.items():
    print(i,j)


# LES FONCTIONS UTILISEES SUR LES DICTIONNAIRES

#In     =>      Faire une recherche ou une vérification
print("nom" in Repertoire)       # Même chose que celui d'en bas
print("nom" in Repertoire.keys())    # Même chose que celui qui en haut
print("Dieu donné" in Repertoire.values())
print("-*-*-*-*-*-*-*-*-*-*-*-*-")

#Copy   =>      copier tous les éléments d'une dictionnaire
NewRepertoire = Repertoire.copy()
print(f"NewRepertoire : {NewRepertoire}") # ceci ou
print("----------------------------------------------------------")
print("NewRepertoire " + str(NewRepertoire)) # cela
print("-*-*-*-*-*-*-*-*-*-*-*-*-")

#Get    =>      récupérer la valeur d'une clé dans un dictionnaire
print(Repertoire.get("nom"))
print(Repertoire.get("name"))
print("-*-*-*-*-*-*-*-*-*-*-*-*-")

#Pop    =>      supprimer un élément (le dernier élément) dans un dictionnaire
NewRepertoire.pop("numero_de_telephone ")
print(NewRepertoire)
print("-*-*-*-*-*-*-*-*-*-*-*-*-")

#Clear  =>      supprimer tous les éléments contenus dans un dictionnaire
print(NewRepertoire.clear())
print(NewRepertoire)
print("-*-*-*-*-*-*-*-*-*-*-*-*-\n")

#Update =>      faire une fusion de deux dictionnaire
otherRepertoire = {"Nom_de_famille" : "JeNeSaisPlus"}
NewRepertoire = {"Qui_suis_je_au_juste" : "une créature de Dieu"}
otherRepertoire.update(NewRepertoire)
print(otherRepertoire)
print("---***---***---***---***---***---\n")
otherRepertoire.update(Repertoire)
print(otherRepertoire)
print("-*-*-*-*-*-*-*-*-*-*-*-*-")
"""

"""
# LES TUPLES : SES ELEMENTS NE SONT PAS CHANGEABLES OU MODIFIABLES, PEUVENT ÊTRE UTILISES DANS UN DICTIONNAIRE
print("Les Tuples")
tuple = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")
print(tuple)
print("La longueur totale de notre tuple est : " + str(len(tuple)))

# UTILISATION DANS UN DICTIONNAIRE
Localisation = {
    (41.4521, 81.2514) : "Coordonnées de ma maison",
    (20.8241, 121.2105) : "Coordonnées d'une autre maison"
}
print(Localisation)
# AUTRE FORME D'AFFICHAGE
for month in tuple:
    print(month)
print("-----------------------------------------")
z = 0
while z < len(tuple):
    print(tuple[z])
    z+=1

# LES FONCTIONS UTILISEES DANS LES TUPLES
# Count & Index
print(tuple.count("Janvier"))   # afficher le nombre de fois que la chaîne de caractère "Janvier" se trouve dans le tuple
print(tuple.index("Avril"))     # afficher l'index ou la position de la chaîne de caractère "Avril"
"""

"""
from collections import namedtuple

print("Les tuples")
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
Greeting = "Morning",
weekend = "Saturday", "Sunday"

print(week)
print(Greeting)
print(weekend)

print(type(week))
print(type(Greeting))
print(type(weekend))

week_days = namedtuple("Week_days", ["Days", "Weekend_days"])
exemple = week_days(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["Saturday", "Sunday"]) # Erroné a revoir
print(exemple.Days)
print(exemple.Weekend_days)
"""

"""
from collections import namedtuple

# Créer un namedtuple pour stocker les jours de la semaine
Day = namedtuple("Day", ["name", "abbreviation"])

# Créer des objets Day pour chaque jour de la semaine
monday = Day("Monday", "Mon")
tuesday = Day("Tuesday", "Tue")
wednesday = Day("Wednesday", "Wed")
thursday = Day("Thursday", "Thu")
friday = Day("Friday", "Fri")
saturday = Day("Saturday", "Sat")
sunday = Day("Sunday", "Sun")

# Afficher les jours de la semaine
print("Les jours de la semaine sont au nombre de sept qui sont :\n")
print(monday.name)
print(tuesday.name)
print(wednesday.name)
print(thursday.name)
print(friday.name)
print(saturday.name)
print(sunday.name)
"""

"""
#Sets
set = {44, 52, 90944}
gathering = {55, 88, 66, 77, 92440}

print(66 in set)
print(55 in set)
print("------------------")
print(55 in gathering)
print(92440 in gathering)

for nmuber in set:
    print(set)
"""

"""
# MAP IN PYTHON

store = [
    ('shirt', 20.00),
    ('pants', 25.00),
    ('jacket', 50.00),
    ('socks', 10.00),
    ('shoes', 35.00)
]

to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], data[1] / 0.82)

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store_euros))
print('prices in euros')
for store in store_euros:
    print(store)
print('prices in dollars')
for store in store_euros:
    print(store)
"""

"""
# LES FONCTIONS
def my_name():
    print("Je suis YASSINTHE Dieu donné K. Jules")
my_name()

def carre(number):
    return number * number
# number = int(input("Votre nombre "))
resultat = carre(5)
print(resultat)

def nom(name):
    return f"Mon nom est {name} !"
RESULTAT = nom("YASSINTHE DIEU DONNE K. JULES")
print(RESULTAT)

def sum(*args): # fonction permettant de calculer la somme de deux ou plusieurs nombres
    result = 0
    for num in args:
        result += num
    return result
print(sum(20,55,6188,20,11,355,55))
print(sum(2,5.226,66,0.9565))

# FONCTION FIBONACCI
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
"""

"""
# LES DECORATEURS

def greeting(param):
    def wrapper():
        print("Bonjour, je suis Dieu donné, content de ...")
        param()
        print("Euuhh.. pourquoi tu m'as interrompu ?")
    return wrapper

def interruption():
    print("Ehh je suis Marc !")

hello = greeting(interruption)
hello()

print("-----------------********************-------------------")

def presentation(args):
    def wrapper():
        print("Je suis un supercalculateur humain !\nLaissez-moi vous faire ma présentation : Je m'appelle ...")
        args()
        print("Ne vois-tu pas que je suis en train de me présenter ?\nIl fallait être un peu plsu poli non !?")
    return wrapper

@presentation
def interrupt():
    print("Où je porrais trouver le cafétariat dans ce coin, Monsieur?")

present = presentation(interrupt)
present()

print("------------Autre forme d'affichage du décorateur------------")
interrupt()
"""

"""
a, b, c = 10, 25, 62#, 58
print(a, b, c)

# Opération d'affectation
a,b,c = c,a,b
print(a,b,c)

#   LES NOMBRES COMPLEXES
a = 6 + 7j
b = 7j + 5

print(a)
print(b)
print(type(a), type(b))

c = float("54.66")
print(c)
print(type(c))

d = float(54.66)
print(d)
print(type(d))
print(bool(None))
"""
