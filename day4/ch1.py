filename = "input.txt"
# Read the first line to prepare the draw numbers in an int array
with open(filename) as f:
    first_line = f.readline()
draw_numbers = [int(value) for value in first_line.split(',')]
print(draw_numbers)

# Import the board numbers in the a 3D array/matrix. 
import numpy as np
all_boards = np.loadtxt(filename, skiprows = 1).astype(int)
all_boards = np.vsplit(all_boards, all_boards.size/25)

original_boards = all_boards.copy(); 
draw_complete = False

winning_board_sum = 0
winning_draw_num = 0
# iterate through draw numbers
for draw in draw_numbers: 
    # iterate through all boards
    for board_index in range(len(all_boards)):
        # replace the draw number with "-1" in the board. 
        all_boards[board_index] = np.where(all_boards[board_index]==draw,-1,all_boards[board_index])

        # check if there's any rows or columns with all marked number. ie all "-1", sum should be -5
        # check columns
        if (-5 in np.sum(all_boards[board_index],0)): 
            draw_complete=True
        # check all rows
        if (-5 in np.sum(all_boards[board_index],1)): 
            draw_complete=True

        if draw_complete:
            # calculate the winnng board sum
            winning_board_sum = np.sum(np.where(all_boards[board_index]>=0,all_boards[board_index],0))
            print(all_boards[board_index])
            print(original_boards[board_index])
            break
        
    if draw_complete:
        # save the winning draw number
        winning_draw_num = draw
        break

# print the answer        
print("Answer = ", winning_draw_num * winning_board_sum)
