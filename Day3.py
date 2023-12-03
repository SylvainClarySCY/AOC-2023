with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")
data_augmented = ["."*(len(data[0])+2)]*2
for e in data:
    data_augmented.insert(-1, "."+e+".")

somme = 0

for i in range(len(data_augmented)):
    nombre = ""
    j_min = 0
    part_number = False
    for j in range(len(data_augmented[0])):
        if data_augmented[i][j].isdigit():
            if nombre == "":
                j_min = max(j - 1, 0)
            nombre += data_augmented[i][j]
        if nombre !="" and not data_augmented[i][j].isdigit():
            for k in range(i-1,i+2):
                for l in range(j_min, j+1):
                    if data_augmented[k][l] !="." and not data_augmented[k][l].isdigit():
                        part_number = True
            if part_number:
                somme += int(nombre)
            nombre = ""
            j_min = 0
            part_number = False
  
print(somme)

def trouve_number(L, donnees):
    nombre = donnees[L[0]][L[1]]
    j = L[1]-1
    while donnees[L[0]][j].isdigit():
        nombre = donnees[L[0]][j] + nombre
        j = j -1
    j = L[1]+1
    while donnees[L[0]][j].isdigit():
        nombre = nombre + donnees[L[0]][j]
        j += 1
    return int(nombre)

somme = 0

for i in range(len(data_augmented)):
    adjacent_numbers = []
    number = False
    for j in range(len(data_augmented[0])):
        if data_augmented[i][j] == "*":
            for k in range(i-1,i+2):
                for l in range(j-1, j+2):
                    if data_augmented[k][l].isdigit() and not number:
                        adjacent_numbers.append([k,l])
                        number = True
                    
                    if number and not data_augmented[k][l].isdigit():
                        number = False
                
                number = False
                
            if len(adjacent_numbers) == 2:
                produit = 1
                for e in adjacent_numbers:
                    produit = produit * trouve_number(e, data_augmented)
                somme += produit
            adjacent_numbers = []
  
print(somme)