with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")

points = 0
number_cards = 0
list_copies = [0 for e in data]

for i in range(len(data)):
    data[i] = data[i][9:].split("|")
    data[i] = [[x for x in data[i][0].split(" ") if x != ''],[x for x in data[i][1].split(" ") if x != '']]
    
    points_carte = 0
    copies = 0
    
    for e in data[i][1]:
        if e in data[i][0]:
            if points_carte == 0:
                points_carte += 1
            else:
                points_carte = points_carte*2
            copies += 1
            
    for j in range(i+1, i+copies+1):
        list_copies[j] += list_copies[i] + 1
        
    points += points_carte
    number_cards += list_copies[i] + 1
    
print(points)
print(number_cards)