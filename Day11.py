import re

with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")

def length(initial, expansion):
    coordonnees = []
    for i in range(len(initial)):
        coordonnees += list(map(lambda e: (i, e), [m.start() for m in re.finditer('#', initial[i])]))
    
    galaxyless_rows = []
    galaxyless_columns = []

    for i in range(len(initial)):
        if initial[i] == '.'*len(initial[0]):
            galaxyless_rows.append(i)

    for i in range(len(initial[0])):
        column = ''
        for j in range(len(initial)):
            column += initial[j][i]
        
        if not '#' in column:
            galaxyless_columns.append(i)
    
    sum_length = 0

    for i in range(len(coordonnees)):
        for j in range(i+1, len(coordonnees)):
            for k in range(min(coordonnees[i][0],coordonnees[j][0]),max(coordonnees[i][0],coordonnees[j][0])):
                if k in galaxyless_rows:
                    sum_length += expansion
                else:
                    sum_length += 1
            
            for k in range(min(coordonnees[i][1],coordonnees[j][1]),max(coordonnees[i][1],coordonnees[j][1])):
                if k in galaxyless_columns:
                    sum_length += expansion
                else:
                    sum_length += 1

    return sum_length

print(length(data, 2))
print(length(data, 1000000))