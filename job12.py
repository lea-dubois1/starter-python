file = open("data.txt", "rt")
data = file.read()
mots = data.split()

print("Le nombre de mots: ", len(mots))