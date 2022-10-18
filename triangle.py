hauteur = int(input("hauteur: "))

for i in range (hauteur):
    if i == 0: # Pour la première ligne
        print (" " * (hauteur - 1) + "/" + "\\")

    elif i == (hauteur - 1): # Pour la dernière ligne
        print ("/" + "_" * (i*2) + "\\")

    else: # Pour le millieu
        print (" " * (hauteur-i-1) + "/" + " " * (i*2) + "\\")