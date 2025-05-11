# def salutation():
#   print("Salut tout le monde !")
#   print("Comment tu vas aujourd'hui ?")

# salutation()

# def calcul():
#   a = int(input("Veuillez saisir la première valeur : "))
#   b = int(input("Veuillez saisir la deuxième valeur : "))
#   result = a + b
#   return result

# print(calcul())

def calcul(val_1, val_2, operator="add"):
  result = 0
  if operator.lower() == "add":
    result = val_1 + val_2
  elif operator.lower() == "sub":
    result = val_1 - val_2
  elif operator.lower() == "mul":
    result = val_1 * val_2
  elif operator.lower() == "div":
    result = val_1 / val_2

  return result

print(calcul(7, 3,"DIV"))