text = input("Donnez-moi un texte: ")

fichier = open("output.txt", "a")
fichier.write(text)
fichier = open("output.txt", "r")
print (fichier.read())
fichier.close
