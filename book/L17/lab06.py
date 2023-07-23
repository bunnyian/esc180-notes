'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
    



def num_to_coords(square_num):
    return [(square_num - 1) // 3, (square_num - 1) % 3]

def put_in_board(board, mark, square_num):
    coords = num_to_coords(square_num)
    row, column = coords[0], coords[1]
    
    if board[row][column] == " ":
        board[row][column] = mark
        return True
    else:
        return False
    


    
    
def get_move_from_user(board, mark):
    move = int(input("Enter your move: "))
    while not put_in_board(board, mark, move):
        move = int(input("Enter your move: "))
        

def get_free_squares(board, mark):
    free = []
    for i in range(1, 10):
        coords = num_to_coords(i)
        row, column = coords[0], coords[1]
        if board[row][column] == " ":
            free.append(i)
    return free

def random_comp_move(board, mark):
    free = get_free_squares(board, mark)
    
    rand_move = free[int(random.random()*len(free))]
    
    put_in_board(board, mark, rand_move)


    

def is_row_all_three(board, mark, row_num):
    return board[row_num] == [mark] * 3
    
def is_col_all_three(board, mark, col_num):
    for i in range(3):
        if board[i][col_num] != mark:
            return False
    return True
    
def is_left_diag_all_three(board, mark):
    for i in range(3):
        if board[i][i] != mark:
            return False
    return True
    
def is_right_diag_all_three(board, mark):
    for i in range(3):
        if board[i][2-i] != mark:
            return False
    return True
    
def is_win(board, mark):
    for i in range(3):
        if is_row_all_three(board, mark, i):
            return True
    
    for i in range(3):
        if is_col_all_three(board, mark, i):
            return True
            
    if is_right_diag_all_three(board, mark):
        return True
        
    if is_left_diag_all_three(board, mark):
        return True
        
    return False
        
        

def make_computer_move_attack(board, mark):
    free_squares = get_free_squares(board, mark)
    for sq in free_squares:
        coords = num_to_coords(sq)
        row, column = coords[0], coords[1]
        board[row][column] = mark
        if is_win(board, mark):
            return
        
        board[row][column] = " "
        
    random_comp_move(board, mark)
            
    
def play_ttt():
    board = make_empty_board()
    print_board_and_legend(board)
    while True:
        
        print("Getting computer move...")
        make_computer_move_attack(board, "X")
        print_board_and_legend(board)
        
        #get_move_from_user(board, "O")
        #print("\n")
        #print_board_and_legend(board)
        
            
        if is_win(board, "X"):
            print("Computer wins!")
            break
        
        #get_move_from_user(board, "O")
        get_move_from_user(board, "O")
        print("\n")
        print_board_and_legend(board)
        
        if is_win(board, "O"):
            print("User wins!")
            break
            
if __name__ == '__main__':
    play_ttt()
    