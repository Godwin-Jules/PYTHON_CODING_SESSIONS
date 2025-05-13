# je veux créer une strucure selective permettant de faire des calculs grace au choix de l'utilisateur 
print("Choose an operator:")
print("[1] - for add")
print("[2] - for sub")
print("[3] - for mul")
print("[4] - for div")
ope = input("Enter operator: ")
a=int(input("Enter  number: "))
b=int(input("Enter  number: "))
def calcule(a,b,operateur=ope):
    if operateur == "1":
        return a+b
    elif operateur == "2":
        return a-b
    elif operateur == "3":
        return a*b
    elif operateur == "4":
        if b == 0:
            print("error: la division par zero est interdite")
        else:
            return a/b
    else:
        print("Invalid operator")
print(calcule(a,b,operateur=ope))
