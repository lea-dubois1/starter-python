debut = int(input("Donnez-moi un nombre par lequel commencer: "))
fin = int(input("Donnez-moi un nombre auquel m'arrêter: "))

if debut == fin:
        print("Valeurs égales")

elif debut < fin:
    for i in range(debut + 1, fin):
        print(i)

elif debut > fin:
    for i in range(debut -1, fin, -1):
        print(i)
