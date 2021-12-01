with open('input.txt') as f:
    readindex = 0
    lines = f.read().splitlines()

increased = 0

for index, line1 in enumerate(lines):
    if (index != 0 and (index < len(lines)-2)):
        
        first_window = int(lines[index-1])+int(lines[index])+int(lines[index+1])
        second_window = int(lines[index])+int(lines[index+1])+int(lines[index+2])
        if ((second_window - first_window) > 0):
            print(second_window, "(increased)")
            increased+=1
        elif ((second_window - first_window)  == 0):
            print(second_window, "(no change)")
        else: 
            print(second_window, "(decreased)")
    elif (index == 0):
        print(int(lines[index])+int(lines[index+1])+int(lines[index+2]), "(N/A - no previous sum)")

print("Number of increases = ", increased)