fichier = open("domains.xml", "r")

list = []

lignes = fichier.readlines()

for line in lignes:
    line = line.replace("</column>\n", "")
    list.append(line)

fichier.close()
list2 = [s for s in list if '<column name="domain">' in s]
print(len(list2))