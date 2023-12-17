with open("input.txt") as f:
    data = f.read().strip()

data = data.split(',')

def hash_alg(string):
    result = 0
    
    for e in string:
        result += ord(e)
        result *= 17
        result %= 256
    
    return result

sum_data = 0
for e in data:
    sum_data += hash_alg(e)
    
print(sum_data)

boxes = [[] for i in range(256)]
focuses = [[] for i in range(256)]

for e in data:
    if '-' in e:
        for i in range(len(boxes)):
            try:
                index = boxes[i].index(e[:-1])
            except ValueError:
                index = -1
            if index != -1:
                boxes[i].pop(index)
                focuses[i].pop(index)
                break
    
    elif '=' in e:
        string, focus = e.split('=')
        box = hash_alg(string)
        if string not in boxes[box]:
            boxes[box].append(string)
            focuses[box].append(focus)
        else:
            index = boxes[box].index(string)
            focuses[box][index] = focus
    
total_focusing_power = 0

for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        total_focusing_power += (i+1)*(j+1)*int(focuses[i][j])
        
print(total_focusing_power)