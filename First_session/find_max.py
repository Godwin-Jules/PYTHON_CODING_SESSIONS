"""
  l'algo qui permet de trouver le max entre trois nombres
"""

num_1 = int(input("Saisir le premier nombre : "))
num_2 = int(input("Saisir le deuxième nombre : "))
num_3 = int(input("Saisir le troisième nombre : "))
# 12 45 33
if num_1 > num_2:
  if num_1 > num_3:
    print(num_1)
  else:
    print(num_3)
elif num_2 > num_3:
  print(num_2)
else:
  print(num_3)