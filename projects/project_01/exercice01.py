def return_entries():
  while True:
    try:
      a = input("Veuillez saisir la première valeur : ")
      a = float (a)
      break
    except:
      print("Valeur entrée incorrecte, veuillez reprendre !\n")

  while True:
    try:
      b = input("Veuillez saisir la deuxième valeur : ")
      b = float(b)
      break
    except:
      print("Valeur entrée incorrecte, veuillez reprendre !\n")

  return a, b

def return_operator():
  OPERATORS = {
    1: "ADDITION",
    2: "SOUSTRATION",
    3: "MULTIPLICATION",
    4: "DIVISION"
  }
  print("Veuillez choisir un opérateur grâce aux chiffres de 1 à 4")
  print("\t[1] - Addition")
  print("\t[2] - Soustration")
  print("\t[3] - Multiplication")
  print("\t[4] - Division")
  print("Une saisie incorrecte vaut 1 par défaut\n")

  saisie = input("Veuillez faire votre choix : ")

  try:
    saisie = int(saisie)
    if saisie in [1, 2, 3, 4]:
      print(f"Opérateur choisi : \"{OPERATORS[saisie]}\"")
      return saisie
    else:
      print(f"Opérateur par défaut choisi : \"{OPERATORS[1]}\"")
      return 1
  except:
    print(f"Saisie incorrecte, opérateur par défaut choisi \"{OPERATORS[1]}\"")
    return 1

def main():
  print("\t\t***********************************")
  print("\t\t|\tPROGRAMME DE CALCUL \t  |")
  print("\t\t***********************************\n")

  val_1, val_2 = return_entries()
  operator = return_operator()
  result = 0
  OPERATORS = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
  }

  if operator == 1:
    result = val_1 + val_2
  elif operator == 2:
    result = val_1 - val_2
  elif operator == 3:
    result = val_1 * val_2
  elif operator == 4:
    if val_2 == 0:
      print("\nDivision par zéro impossible, à reprendre !")
      return None
    else:
      result = val_1 / val_2
  else:
    result = 0

  print(f"\nRESUTAT DES CALCULS : {val_1} {OPERATORS[operator]} {val_2} = {result:.2f}")

main()