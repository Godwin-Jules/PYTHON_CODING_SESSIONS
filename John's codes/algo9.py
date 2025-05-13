nombre = int(input("entrez un nombre entre 10 et 20: "))
while nombre >= 10 or nombre <= 20:
    print("superbe ")
    break
if nombre  < 10:
        print("entrée un nombre plus grand que 10")
elif nombre > 20:
        print("entrée un nombre plus petit que 20")