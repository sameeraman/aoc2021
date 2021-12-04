filename = "input.txt"

# Read the first line to prepare the draw numbers in an int array
with open(filename) as f:
    first_line = f.readline()
draw_numbers = [int(value) for value in first_line.split(',')]

# Import the board numbers in the a 3D array/matrix. 
import numpy as np
all_boards = np.loadtxt(filename, skiprows = 1).astype(int)
all_boards = np.vsplit(all_boards, all_boards.size/25)

draw_complete = False
winning_board_index = []

last_winning_board_sum = 0
winning_draw_num = 0
# iterate through draw numbers
for draw in draw_numbers: 
    winning_board_index = []
    # iterate through all boards

    for board_index in range(len(all_boards)):
        board_won = False
        # replace the draw number with "-1" in the board. 
        all_boards[board_index] = np.where(all_boards[board_index]==draw,-1,all_boards[board_index])

        # check if there's any rows or columns with all marked number. ie all "-1", sum should be -5
        # check columns
        if (-5 in np.sum(all_boards[board_index],0)): 
            board_won=True
        # check all rows
        if (-5 in np.sum(all_boards[board_index],1)): 
            board_won=True


        # if the board is won schedule to remove it from the all_boards
        if board_won:
            # print("size : ", len(all_boards))
            if ((len(all_boards)-len(winning_board_index))==1):
                # if this is the last board, calculate the sum
                last_winning_board_sum = np.sum(np.where(all_boards[board_index]>=0,all_boards[board_index],0))
                print ("last winning board sum = ", last_winning_board_sum)
                draw_complete = True
                break
            else:
                # add the index to delete. 
                winning_board_index.append(board_index)

    winning_board_index.sort(reverse=True)
    # print('list to remove : ', winning_board_index)
    for index in winning_board_index:
        all_boards.pop(index)

    if draw_complete:
        # save the winning draw number
        winning_draw_num = draw
        print ("winning draw number = ", winning_draw_num)
        break

# print the answer        
print("Answer = ", winning_draw_num * last_winning_board_sum)


