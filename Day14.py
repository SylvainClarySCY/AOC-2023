with open("input.txt") as f:
    data = f.read().strip()

data = data.split('\n')

def north_support_lead_load(data):
    total_load = 0
    
    for i in range(len(data[0])):
        rounded_rock = 0
        obstacle = len(data) + 1
        
        for j in range(len(data)):        
            if data[j][i] == 'O':
                rounded_rock += 1
            elif data[j][i] == '#':
                for k in range(obstacle-1, obstacle-rounded_rock-1, -1):
                    total_load += k
                
                obstacle = len(data)-j
                rounded_rock = 0
        
        for k in range(obstacle-1, obstacle-rounded_rock-1, -1):
            total_load += k
            
    return total_load
                
print(north_support_lead_load(data))

def north_tilt(data):
    tilted_data = ['' for x in data]
    
    for i in range(len(data[0])):
        rounded_rock = 0
        obstacle = -1
        
        for j in range(len(data)):        
            if data[j][i] == 'O':
                rounded_rock += 1
            elif data[j][i] == '#':
                for k in range(obstacle+1, obstacle+rounded_rock+1):
                    tilted_data[k] += 'O'
                
                for k in range(obstacle+rounded_rock+1,j):
                    tilted_data[k] += '.'
                    
                tilted_data[j] += '#'                
                obstacle = j
                rounded_rock = 0
        
        for k in range(obstacle+1, obstacle+rounded_rock+1):
            tilted_data[k] += 'O'
        
        for k in range(obstacle+rounded_rock+1,len(data)):
            tilted_data[k] += '.'
            
    return tilted_data

def cycles(data, number):
    seen = {}
    platform = [x for x in data]
    cycle = 0
    
    while tuple(platform) not in seen and cycle < number:
        seen[tuple(platform)] = cycle
        
        for i in range(4):
            platform = north_tilt(platform)
            platform = [''.join(list(i)[::-1]) for i in zip(*platform)]
        
        cycle += 1
        
    repeat = seen[tuple(platform)]
    final_cycle = (number - repeat) % (cycle - repeat) + repeat

    return next(key for key, value in seen.items() if value == final_cycle)

def north_support_lead(data):
    total_load = 0
    
    for i in range(len(data[0])):
        for j in range(len(data)):        
            if data[j][i] == 'O':
                total_load += len(data)-j
            
    return total_load

print(north_support_lead(cycles(data, 1000000000)))