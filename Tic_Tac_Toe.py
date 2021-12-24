import random

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def quit_game(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing! I hope you enjoyed the game.")
        return True
    else: return False

def number_check(user_input):
    if user_input.isnumeric() and int(user_input) <= 9: return True
    elif user_input.isnumeric() and int(user_input) >= 9:
        print("This number is higher than 9.")
        return False
    else:
        print("This is not a number.")
        return False

def coordinates(user_input):
    row = int((user_input - 1) / 3)
    column = (user_input - 1) % 3
    return (row, column)

def exist_check(position, board):
    if board[position[0]][position[1]] != "-":
        print("This move already exists. Enter a different move.")
        return True
    else:
        return False

def write_board(position, board, symbol):
    board[position[0]][position[1]] = symbol

def comp_turn(board):
    print("\nYour turn: \n")
    print_board(board)
    print("\nComputer's Turn= \n")
    comp_position = (1, 1)
    while board[comp_position[0]][comp_position[1]] != "y":
        rand_number = random.randint(1, 9)
        comp_position = coordinates(rand_number)
        if board[comp_position[0]][comp_position[1]] == "-":
            write_board(comp_position, board, "O")
            break

def check_row_col(board, symbol):
   is_win = False
   for i in range(3):
       row_counter = 0
       column_counter = 0
       for j in range(3):
           if board[i][j] == symbol: row_counter += 1
           if board[j][i] == symbol: column_counter += 1
       if row_counter == 3 or column_counter == 3:
           is_win = True
           break

   if is_win: return True

def check_diag(board, symbol):
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    elif board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    else:
        return False

def check_win(board, symbol):
    row_col_check = check_row_col(board, symbol)
    diagonal_check = check_diag(board, symbol)
    if row_col_check or diagonal_check: return True
    else: return False

def check_tie(board):
    is_tie = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                is_tie = False
                break
    return is_tie

while True:
    print_board(board)
    user_input = input("Please enter your move 1 thru 9. If you want to quit enter \"q\". ")
    if quit_game(user_input): break
    if not number_check(user_input):
        continue
    user_input = int(user_input)
    position = coordinates(user_input)
    if exist_check(position, board):
        continue
    write_board(position, board, "X")
    if check_win(board, "X"):
        print_board(board)
        print("Congratulations!! you WON!")
        break
    elif check_tie(board):
        print_board(board)
        print("Its a Tie! Try again!")
        break

    comp_turn(board)
    if check_win(board, "O"):
        print_board(board)
        print("Sorry, you lost this time! try again!")
        break
    elif check_tie(board):
        print_board(board)
        print("Its a Tie! Try again!")
        break


