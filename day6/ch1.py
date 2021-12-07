with open("input.txt") as f:
    line = f.readline()

number_of_day = 80

print(list(range(0,number_of_day+1)))

state = [int(fish) for fish in line.split(',')]
print(type(state[0]))

for day in range(0,number_of_day+1):
    if (day==0):
        print("Initial State :", state)
    else:
        new_fish = []
        for fish in range(0,len(state)): 
            if (state[fish]==0):
                new_fish.append(8)
                state[fish]=6
            else:
                state[fish] = state[fish] - 1
        state = state+new_fish
        print("After", day, " days :", state)

print("Answer:" , len(state))