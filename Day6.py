with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")

for i in range(len(data)):
    data[i] = [int(x) for x in data[i][10:].split(" ") if x != '']

product = 1

for i in range(len(data[0])):
    possibilities = 0
    
    for j in range(data[0][i]):
        travel_distance = j * (data[0][i] - j)
        
        if travel_distance > data[1][i]:
            possibilities += 1
    
    if possibilities > 0 :
        product = product * possibilities
        
        
print(product)

time = ''
distance = ''

for i in range(len(data[0])):
    time += str(data[0][i])
    distance += str(data[1][i])
    
time = int(time)
distance = int(distance)

possibilities = 0

for j in range(time):
    travel_distance = j * (time - j)
    
    if travel_distance > distance:
        possibilities += 1

print(possibilities)