with open("input.txt") as f:
    data = f.read().strip()

data = data.split("\n")

movements = [x for x in data[0]]

nodes = {}

for i in range(2,len(data)):
    nodes[data[i][:3]] = [data[i][7:10],data[i][12:15]]
    
current_node = 'AAA'
steps = 0

while current_node != 'ZZZ':
    if movements[steps%len(movements)]=='L':
        current_node = nodes[current_node][0]
    else:
        current_node = nodes[current_node][1]
    steps += 1

print(steps)

first_nodes = [x for x in nodes if x[2] == 'A']
steps = [0 for x in first_nodes]
cycles = [0 for x in first_nodes]

for i in range(len(first_nodes)):
    current_node = first_nodes[i]
    step = 0
    ends_seen = {}
    while current_node not in ends_seen:
        if current_node[2] == 'Z':
            ends_seen[current_node] = step
        
        if movements[step%len(movements)]=='L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        step += 1
        
    steps[i] = step
    cycles[i] = step - ends_seen[current_node]


#Works because each cycle is half the initial number of steps
'''

Here, this might help make it clear:

       o-----o       o-----o       o-----o
       |     |   h   |     |   m   |     |
------>|  A  +------>| ... +------>|  Z  |
       |     |       |     |       |     |
       o-----o       o-----o       o--+--o
                        ^             |
                        |      t      |
                        o-------------o

Each ghost starts at an "A" node, and goes some number of steps, h, until it reaches the head of the cycle. 
Then there's m steps in the middle until we reach a "Z" node, followed by the tail steps, t to return to the 
beginning of the cycle.

So your cycle detection finds a cycle of length m + t. But if you look carefully at the steps, you'll see 
that the input is constructed so that there's only one "Z" node reached, and also that h = t. In other 
words, the time from the "A" node to the "Z" node is exactly the same as the cycle time. So you can ignore 
the time from "A" to the head of the cycle, and just focus on how often the cycles line up. Which, of 
course, is the LCM.
'''

def LCM(a, b): 
    greater = max(a, b) 
    smallest = min(a, b) 
    for i in range(greater, a*b+1, greater): 
        if i % smallest == 0: 
            return i
        
min_steps = LCM(cycles[0],cycles[1])
for i in range(2,len(steps)):
    min_steps = LCM(min_steps,cycles[i])
    
print(min_steps)