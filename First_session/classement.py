"""
  un algo qui permet de faire le classement selon la tranche d'âge de l'utilisateur
"""

age = int(input("Veuillez entrer votre âge : "))
if age < 0:
  print("Erreur de sasir, veuillez revoir !")
else:
  if age < 8:
    print("C'est un poussin")
  elif age < 14:
    print("C'est un benjamin")
  else:
    print("C'est un cadet")