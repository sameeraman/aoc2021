with open("input.txt") as f:
    line = f.readline()

crab_positions = [int(crab) for crab in line.split(',')]
positions = range(max(crab_positions))
costs = [0]*len(positions)

for position in positions:
    position_cost = 0
    for crab_position in crab_positions:
        cost = max(crab_position,position)-min(crab_position,position)
        position_cost += int(cost*(cost+1)/2)
    costs[position] = position_cost

print("Answer: Index =", costs.index(min(costs)), ", Fuel= ", min(costs))



