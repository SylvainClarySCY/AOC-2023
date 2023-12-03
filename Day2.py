with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split(":")
    data[i] = [data[i][0].split(" ")[1],data[i][1].split(";")]

sum_ID = 0
    
for e in data:
    valid = True
    for i in range(len(e[1])):
        tirage = e[1][i].split(",")
        for t in tirage:
            nombre = ''
            for char in t:
                if char.isdigit():
                    nombre += char
            if 'red' in t and int(nombre)>12:
                valid = False
            if 'green' in t and int(nombre)>13:
                valid = False
            if 'blue' in t and int(nombre)>14:
                valid = False
        if not valid:
            break
    
    if valid:
        sum_ID += int(e[0])
        
print(sum_ID)


sum_powers = 0
    
for e in data:
    min_red = 0
    min_green = 0
    min_blue = 0
    for i in range(len(e[1])):
        tirage = e[1][i].split(",")
        for t in tirage:
            nombre = ''
            for char in t:
                if char.isdigit():
                    nombre += char
            if 'red' in t and int(nombre)>min_red:
                min_red = int(nombre)
            if 'green' in t and int(nombre)>min_green:
                min_green = int(nombre)
            if 'blue' in t and int(nombre)>min_blue:
                min_blue = int(nombre)
    
    sum_powers += min_red*min_blue*min_green
        
print(sum_powers)