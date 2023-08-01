MOVES = [1, 2]
GOAL_SUM = 21


def is_winning_move_simple(s):
    '''Return True iff we can win the race to GOAL_SUM by getting to sum s, 
    assuming the only move is + 1
    '''
    if s == GOAL_SUM:
        return True
    
    return not is_winning_move_simple(s + 1)

def is_winning_sum(s):
    '''Return True iff we can win the race to GOAL_SUM by getting to sum s, 
    assuming the moves available are in MOVES
    '''
    if s == GOAL_SUM:
        return True
    
    #Try every possible move the opponent could make, and if none of the moves 
    #lead to a winning sum, that means that we can win
    #
    #So we return True iff there is no move such that is_winning_sum(s + move) is 
    #True
    for move in MOVES:
        if is_winning_sum(s + move):
            return False
    
    #Didn't find a winning move for the opponent, so return True
    return True


def computer_move(current_sum):
    #Try all possible move and see if we can find one that wins
    for move in MOVES:
        if is_winning_sum(current_sum + move):
            return move
    
    #No sum is winning, so return a random move and hope for the best
    return MOVES[int(random.random()*len(MOVES))]




def play_nim(mover = 'computer'):
    current_sum = 0
    movers = ['computer', 'user']
    
    
    while current_sum < GOAL_SUM:
        print('Current sum: %d\n' % current_sum)
        if mover == 'computer':
            move = computer_move(current_sum)
            print('The computer\'s move: %d' % move)
        else:
            move = int(input('Your move: '))
            
        current_sum += move
        
        if current_sum == GOAL_SUM:
            print('%s won!!!' % mover)
            return
            
        #A complicated expression which is perhaps better-done
        #with an if-else statement. But it works! Think about it.
        mover = movers[(movers.index(mover)+1) % 2]
        
    print('No one won!')



def print_winning_sums():
    '''Find all the winning sums in the race to GOAL_SUM with possible
    moves MOVES and print them
    '''
    
    winning_sums = []
    for i in range(GOAL_SUM):
        if is_winning_sum(i):
            winning_sums.append(i)
    print('Winning sums: ', winning_sums)