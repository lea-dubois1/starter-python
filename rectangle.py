from os import forkpty


largeur=int(input("largeur: "))
hauteur=int(input("hauteur: "))

for i in range (hauteur):
    if i == 0 or i == (hauteur-1): # i == 0 c'est la première ligne et i == (hauteur-1) c'est la dernière. Le -1 c'est parceque on commence à 0
        print ("|" + "-" * largeur + "|")
    
    else:
        print ("|" + " " * largeur + "|")