with open("input.txt") as f:
    line = f.readline()

number_of_day = 256


#print(list(range(0,number_of_day+1)))

state = [int(fish) for fish in line.split(',')]

state_inverse = [0]*9

# load initial state 
for fish in state:
    state_inverse[fish]+=1
print(state_inverse[3])

for day in range(number_of_day):
    newfish = state_inverse[0]
    state_inverse[0] = state_inverse[1]
    state_inverse[1] = state_inverse[2]
    state_inverse[2] = state_inverse[3]
    state_inverse[3] = state_inverse[4]
    state_inverse[4] = state_inverse[5]
    state_inverse[5] = state_inverse[6]
    state_inverse[6] = (state_inverse[7]+newfish)
    state_inverse[7] = state_inverse[8]
    state_inverse[8] = newfish

print(list(range(number_of_day)))
print(state_inverse)
print("Answer:" , sum(state_inverse))