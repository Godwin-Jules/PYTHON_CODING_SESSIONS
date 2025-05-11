"""
  * Demander à l'utilisateur de rentrer un nombre positif entre 1 et 7
  * Faire la vérification de ce nombre et ...
"""

# try:
#   entree = int(input("une valeur entre 1 et 7"))
#   if entree > 0 and entree <=7:
#     # continue
#     print()
#   else:
# except

# try:
#   entree = input("une valeur entre 1 et 7")
#   try:
#     entree = int(entree)
#   except:
#     print("Ta saisie est une chaîne de caractères")
#   if entree > 0 and entree <=7:
#     # continue
#     print()
#   else:

# except:

# Validation of data entries
while True:
  entree = input("une valeur entre 1 et 7 : ")
  try:
    entree = int(entree)
  except ValueError as error:
    print("Veuillez entrer un chiffre")
    print(error)
    continue
  except Exception:
    print()
    continue
  except:
    print("Je ne connais pas cette erreur")
    continue
  if entree > 0 and entree <=7:
    break
  else:
    print("Veuillez reprendre et entrez un chiffre entre 1 et 7")



