"""
  Algo qui permet de vérifier le signe du produit de deux nombres
"""

a = float(input("Saisir la première valeur : "))
b = float(input("Saisir la deuxième valeur : "))
produit = a * b

if produit > 0:
  print("Le produit de ces deux nombres est positif")
else :
  print("Le produit de ces deux nombres est négatif")