def print_board(board):
    for i in range(3):
        print(board[i*3] + '|' + board[i*3+1] + '|' + board[i*3+2])
        if i < 2:
            print('-+-+-')

def make_move(board, position, player):
    board[position] = player

def is_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in line) for line in win_positions)

def is_draw(board):
    return ' ' not in board

def available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for move in available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_val = -float('inf')
    move = -1
    for i in available_moves(board):
        board[i] = 'O'
        move_val = minimax(board, 0, False)
        board[i] = ' '
        if move_val > best_val:
            best_val = move_val
            move = i
    return move

def play_game():
    board = [' ' for _ in range(9)]
    human = 'X'
    ai = 'O'

    while True:
        print_board(board)
        
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        make_move(board, move, human)
        
        if is_winner(board, human):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        move = best_move(board)
        make_move(board, move, ai)
        
        if is_winner(board, ai):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
