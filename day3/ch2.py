with open('input.txt') as f:
    lines = f.read().splitlines()

def oxygen_generator_rating(sublines, index):
    ones = 0
    ones_list = []
    zeros = 0
    zeros_list = []
    for line in sublines: 
        value = list(line)[index]
        if (value=="1"):
            ones+=1
            ones_list.append(line)
        else:
            zeros+=1
            zeros_list.append(line)
    if (ones>zeros):
        if (len(ones_list)>1):
            return oxygen_generator_rating(ones_list,index+1)
        else:
            return ones_list[0]
    elif (ones==zeros):
        if (len(ones_list)>1):
            return oxygen_generator_rating(ones_list,index+1)
        else:
            return ones_list[0]
    else:
        if (len(zeros_list)>1):
            return oxygen_generator_rating(zeros_list,index+1)
        else:
            return zeros_list[0]

def co2_scrubber_rating(sublines, index):
    ones = 0
    ones_list = []
    zeros = 0
    zeros_list = []
    for line in sublines: 
        value = list(line)[index]
        if (value=="1"):
            ones+=1
            ones_list.append(line)
        else:
            zeros+=1
            zeros_list.append(line)
    if (ones<zeros):
        if (len(ones_list)>1):
            return co2_scrubber_rating(ones_list,index+1)
        else:
            return ones_list[0]
    elif (ones==zeros):
        if (len(zeros_list)>1):
            return co2_scrubber_rating(zeros_list,index+1)
        else:
            return zeros_list[0]
    else:
        if (len(zeros_list)>1):
            return co2_scrubber_rating(zeros_list,index+1)
        else:
            return zeros_list[0]

oxygen_value = oxygen_generator_rating(lines,0)
co2_value = co2_scrubber_rating(lines,0)
life_support_rating = (int(oxygen_value,2)*int(co2_value,2))
print("oxygen generator rating =", oxygen_value , int(oxygen_value,2))
print("co2 generator rating =", co2_value , int(co2_value,2))
print("life support rating =", life_support_rating)
