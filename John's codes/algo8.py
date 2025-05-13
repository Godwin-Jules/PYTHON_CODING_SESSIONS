for i in range(1, 3, 1):
    print("traitemant de la commande n° ", i)
    quantité_stock = 5000
quantité_commande = int(input("entrée la quantité commandée "))
seuil_min = 100
if quantité_commande <= quantité_stock:
    print("la commande est livrée ")
    quantité_restante = quantité_stock - quantité_commande
if quantité_restante <= seuil_min:
    print("la commande est impossible")
    print("réaprovisionnement du stock necessair")
    reaprovisionnement = int(input("entrée la quantité de réaprovisionnement "))
    quantité_stock = quantité_restante + reaprovisionnement
    print("le stock est de ", quantité_stock)
