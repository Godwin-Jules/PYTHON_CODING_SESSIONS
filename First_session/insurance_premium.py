"""
  Algo qui calcule les primes d'assurance
"""

base = 2_000_000

print("Veuillez choisir le risque approprié")
print("[1] - Tierce Collision")
print("[2] - Tout risque")
risque = int(input("Votre choix : "))

print("\nVeuillez choisir la puissance appropriée")
print("[1] - 2 à 5CV")
print("[2] - 6 à 8CV")
print("[3] - 9CV et plus")
puissance = int(input("Votre choix : "))

print("\nVeuillez choisir l'utilisation appropriée")
print("[1] - Promenade")
print("[2] - Trajet")
print("[3] - Affaire")
utilisation = int(input("Votre choix : "))

if risque == 1:
  r_value = 1
else:
  r_value = 1.5

if puissance == 1:
  p_value = 1
elif puissance == 2:
  p_value = 1.2
else:
  p_value = 1.4

if utilisation == 1:
  u_value = 0.9
elif utilisation == 2:
  u_value = 1.1
else:
  u_value = 1.25

prime = base * r_value * p_value * u_value

print("Le prime d'assurance est :", prime)