with open('input.txt') as f:
    lines = f.read().splitlines()

increased = 0

for index, line1 in enumerate(lines):
    if (index != 0):
        current_value = int(lines[index])
        previous_value = int(lines[index-1])
        if ((current_value - previous_value) > 0):
            print(current_value, "(increased)")
            increased+=1
    elif (index == 0):
        print(lines[index], "(N/A - no previous measurement)")    

print("Number of increases = ", increased)