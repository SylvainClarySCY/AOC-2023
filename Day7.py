import itertools

def sort_high(high_list, card, cartes):
    high_sort = [[] for i in range(len(cartes))]
    
    for i in range(len(high_list)):
        for j in range(len(cartes)):
            if high_list[i][0][card] == cartes[j]:
                high_sort[j].append(high_list[i])
                
    for i in range(len(high_sort)):
        if len(high_sort[i]) > 1:
            high_sort[i] = sort_high(high_sort[i], card+1, cartes)
                
    return list(itertools.chain.from_iterable(high_sort))

with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")

cartes = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")

hands = [[] for i in range(7)]

for i in range(len(data)):
    data[i] = data[i].split(' ')
    
    nombre_cartes = [data[i][0].count(x) for x in cartes]
    
    if 5 in nombre_cartes:
        hands[0].append(data[i])
        
    elif 4 in nombre_cartes:
        hands[1].append(data[i])
        
    elif 3 in nombre_cartes:
        if 2 in nombre_cartes:
            hands[2].append(data[i])
        else:
            hands[3].append(data[i])
            
    else:
        pair = nombre_cartes.count(2)
        if pair == 2:
            hands[4].append(data[i])
        elif pair == 1:
            hands[5].append(data[i])
        else:
            hands[6].append(data[i])

for i in range(len(hands)):
    hands[i] = sort_high(hands[i], 0, cartes)

sorted_hands = list(itertools.chain.from_iterable(hands))

winnings = 0

for i in range(len(sorted_hands)):
    winnings += int(sorted_hands[i][1])*(len(sorted_hands) - i)
    
print(winnings)

cartes = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")

hands = [[] for i in range(7)]

for i in range(len(data)):    
    nombre_cartes = [data[i][0].count(x) for x in cartes[:-1]]
    max_index = nombre_cartes.index(max(nombre_cartes))
    
    nombre_cartes[max_index] = nombre_cartes[max_index] + data[i][0].count('J')
    
    if 5 in nombre_cartes:
        hands[0].append(data[i])
        
    elif 4 in nombre_cartes:
        hands[1].append(data[i])
        
    elif 3 in nombre_cartes:
        if 2 in nombre_cartes:
            hands[2].append(data[i])
        else:
            hands[3].append(data[i])
            
    else:
        pair = nombre_cartes.count(2)
        if pair == 2:
            hands[4].append(data[i])
        elif pair == 1:
            hands[5].append(data[i])
        else:
            hands[6].append(data[i])

for i in range(len(hands)):
    hands[i] = sort_high(hands[i], 0, cartes)

sorted_hands = list(itertools.chain.from_iterable(hands))

winnings = 0

for i in range(len(sorted_hands)):
    winnings += int(sorted_hands[i][1])*(len(sorted_hands) - i)
    
print(winnings)