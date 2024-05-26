board = [['']*3, ['']*3, ['']*3]

def format(index):
    return int(index)

def board_print(board):
    for x in board:
        print("\n", x, "\n")

# todo check board
def vertikal(board):
    for i in range(3):
        vertikal = board[0][i]+board[1][i]+board[2][i]
        
        if vertikal == 'xxx':
            return board[0][i]
        elif vertikal == '000':
            return board[0][i]
    
    return ""

def vline(board):
    v1 = board[0][0]+board[1][1]+board[2][2]
    v2 = board[0][2]+board[1][1]+board[2][0]
    
    if v1 == 'xxx':
        return board[0][0]
    elif v2 == 'xxx':
        return board[0][2]

    if v1 == '000':
        return board[0][0]
    elif v2 == '000':
        return board[0][2]

    return ""
        
def horizontal(board):
    for i in range(3):
        sum = board[i][0]+board[i][1]+board[i][2]
        
        if sum == 'xxx':
            return board[i][0]
        elif sum == '000':
            return board[i][0]
    else:
        return ""

def check_board(board):
    winner = ''
    
    winner = horizontal(board)
    if winner != '':
        return winner
    
    winner = vertikal(board)
    if winner != '':
        return winner
    
    winner = vline(board)
    if winner != '':
        return winner
    
    return winner        

def check_position(board, row, col):
    if board[row][col] == '':
        return True
    
    return False

def no_winner_check(board):
    counter = 0
    for i in range(3):
        sum = board[i][0]+board[i][1]+board[i][2]
        counter += len(sum)
    
    if counter == 9:
        return False
    else:
        return True
    
board_print(board)
flag, game = True, True
char = "x"
while game:
    data = input(f"{char} Turn (ex: 1,1) = ")
    index = data.split(",")
    
    row = format(index[0])
    col = format(index[1])
    board[row][col]
    
    position = check_position(board, row, col)
    if position:
        if flag:
            board[row][col] = 'x'
            flag = False
            char = "0"
        else:
            board[row][col] = '0'
            flag = True
            char = "x"
    else:
        print("cannot insert into that position!\n")

    board_print(board)
    result = check_board(board)
    if result != "":
        print("The winner is", result)
        game = False
    
    check = no_winner_check(board)
    if check == False:
        game = check