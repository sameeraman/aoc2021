with open('input.txt') as f:
    lines = f.read().splitlines()

gamma = ""
epsilon = ""

for index in range(len(lines[0])):
    ones = 0
    zeros = 0
    for line in lines: 
        value = list(line)[index]
        if (value=="1"):
            ones+=1
        else:
            zeros+=1
    if (ones>zeros):
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0" 
        epsilon+="1"

print("gamma", gamma, int(gamma,2))
print("epsilon", epsilon, int(epsilon,2))
print("power =", int(gamma,2)*int(epsilon,2))