with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")

sum_next_values = 0
sum_previous_values = 0

for i in range(len(data)):
    data[i] = [int(x) for x in data[i].split(' ')]
    
    liste_derniers = []
    liste_premiers = []
    current_differences = [x for x in data[i]]
    
    while current_differences.count(0)!=len(current_differences):
        liste_premiers.append(current_differences[0])
        for j in range(len(current_differences)-1):
            current_differences[j] = current_differences[j+1] - current_differences[j]
        liste_derniers.append(current_differences.pop())
    
    extrapolated_first = 0
    
    for j in range(len(liste_derniers)):
        sum_next_values += liste_derniers[j]
        extrapolated_first = liste_premiers[len(liste_premiers)-j-1] - extrapolated_first
    
    sum_previous_values += extrapolated_first
        
print(sum_next_values)
print(sum_previous_values)