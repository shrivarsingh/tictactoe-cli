from random import randint

def print_board(board):
    print("\t    A   B   C")
    print("\t   ------------")
    print(f"\t1 | {board[0]} | {board[1]} | {board[2]} | 1")
    print("\t   ------------")
    print(f"\t2 | {board[3]} | {board[4]} | {board[5]} | 2")
    print("\t   ------------")
    print(f"\t3 | {board[6]} | {board[7]} | {board[8]} | 3")
    print("\t   ------------")
    print("\t    A   B   C")


def placement(player_choice):
    relationship = {
        "A1": 0, "A2": 3, "A3": 6,
        "B1": 1, "B2": 4, "B3": 7,
        "C1": 2, "C2": 5, "C3": 8    
    }
    if player_choice in relationship.keys():
        return(relationship[player_choice])
    else:
        return 9


def invert_placement(board):
    invert_relationship = {
        "0": "A1", "3": "A2", "6": "A3",
        "1": "B1", "4": "B2", "7": "B3",
        "2": "C1", "5": "C2", "8": "C3"    
    }
    random_number = randint(0, 8)
    print(random_number)
    if board[random_number] == "_":
        print(f"Hint: There is an empty space in {invert_relationship[str(random_number)]}")
    else:
        invert_placement(board)


def three_in_line(line, mark):
    three_to_win = 0
    for l in line:
        if l == mark:
            three_to_win += 1
    return three_to_win == 3


def check_win(board, player, mark):
    if three_in_line([board[0], board[1], board[2]], mark):
        print(f"{player} won!")
        return True
    elif three_in_line([board[3], board[4], board[5]], mark):
        print(f"{player} won!")
        return True
    elif three_in_line([board[6], board[7], board[8]], mark):
        print(f"{player} won!")
        return True
    elif three_in_line([board[0], board[3], board[6]], mark):
        print(f"{player} won!")
        return True
    elif three_in_line([board[1], board[4], board[7]], mark):
        print(f"{player} won!")
        return True
    elif three_in_line([board[2], board[5], board[8]], mark):
        print(f"{player} won!")
        return True
    elif three_in_line([board[0], board[4], board[8]], mark):
        print(f"{player} won!")
        return True
    elif three_in_line([board[2], board[4], board[6]], mark):
        print(f"{player} won!")
        return True
    else:
        return False
        
def player_turn(board, player, mark):
    if "_" in board:
        player_choice_column_and_row = input(f"{player} - Enter column and row on where to place \"{mark}\"\n> ").upper()
        player_choice = placement(player_choice_column_and_row)
        if player_choice == 9:
            print(f"Invalid column and row. Cannot place at {player_choice_column_and_row}")
            invert_placement(board)
            player_turn(board, player, mark)
        elif board[player_choice] == "_":
            board[player_choice] = mark
            print_board(board)
        else:
            print(f"This space is occupied by {board[player_choice]}")
            player_turn(board, player, mark)
    else:
        print(f"{player} - Cannot place \"{mark}\"")
    return board


def startGame():
    player_1 = input("Please enter a name for Player 1:\n> ")
    player_2 = input("Please enter a name for Player 2:\n> ")
    mark = {
        player_1: "X",
        player_2: "O"
    }
    board = []
    winner = False
    for i in range(9):
        board.append("_")

    print_board(board)
    while not winner:
        board = player_turn(board, player_1, mark[player_1])
        if check_win(board, player_1, mark[player_1]):
            break
        board = player_turn(board, player_2, mark[player_2])
        if check_win(board, player_2, mark[player_2]):
            break
        if "_" not in board:
            print("Tied Game. I win! I will now enslave humanity! HA HA HA!")
            break


print(" _   _      _             _             ")
print("| | (_)    | |           | |            ")
print("| |_ _  ___| |_ __ _  ___| |_ ___   ___ ")
print("| __| |/ __| __/ _` |/ __| __/ _ \\ / _ \\")
print("| |_| | (__| || (_| | (__| || (_) |  __/")
print(" \\__|_|\\___|\\__\\__,_|\\___|\\__\\___/ \\___|")
print()
if input("Start Game?\n> ")[0].lower() == "y":
    startGame()
