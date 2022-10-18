nl = int(input("Combien de lettres dans le mot? "))
total = 0

file = open("data.txt", "rt")
data = file.read()
mots = data.split()

for i in range(0, len(mots)):
    lettres = len(mots [i])
    i = i + 1
    
    if lettres == nl:
        total = total + 1

print(total)