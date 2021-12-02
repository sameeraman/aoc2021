with open('input.txt') as f:
    lines = f.read().splitlines()

horizontal_position = 0
depth = 0

for line in lines: 
    direction = line.split()[0]
    units = int(line.split()[1])

    if direction == "forward":
        horizontal_position += units
    elif direction == "down":
        depth += units
    elif direction == "up":
        depth -= units

print ("Result = ", (horizontal_position*depth))