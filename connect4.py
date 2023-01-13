##On load, I want the program to offer an opportunity to play with a human or comp P2
##Turn counter
##Get chips to show up on the board (take-turn)
##Get chips to fall (gravity)
##Win conditions (3 of them)

import random

print("Welcome to Connect 4!")
print("--------------------")

possible_letters = ["A","B","C","D","E","F","G"]
game_board = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]
rows = 6
cols = 7

def print_game_board():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if(game_board[x][y] == "🔵"):
                print("", game_board[x][y], end=" |")
            elif(game_board[x][y] == "🔴"):
                print("", game_board[x][y], end=" |")
            else:
                print(" ", game_board[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def check_win(chip):
    #This loop checks for horizontal win
    for x in range(rows):
        for y in range(cols - 3):
            if (game_board[x][y] == chip and game_board[x][y+1] == chip and game_board[x][y+2] == chip and game_board[x][y+3] == chip):
                print("\nWinner, winner, chicken-dinner!", chip, " wins! Thanks for playing!")
                return True
    
    #This loop checks for vertical win
    #Swapped the first line of this loop, check back to see if it's broken later
    for x in range(rows-3):
        for y in range(cols):
            if (game_board[x][y] == chip and game_board[x+1][y] == chip and game_board[x+2][y] == chip and game_board[x+3][y] == chip):
                print("\nWinner, winner, chicken-dinner!", chip, "wins! Thanks for playing!")
                return True

    #This loop checks for diagonal win from Top Left to Bot Right
    for x in range(rows - 3):
        for y in range(3, cols):
            if (game_board[x][y] == chip and game_board[x+1][y-1] == chip and game_board[x+2][y-2] == chip and game_board[x+3][y-3] == chip):
                print("\nWinner, winner, chicken-dinner!", chip, "wins! Thanks for playing!")
                return True 

    #This loop checks for diagonal win from Top Right to Bot Left
    for x in range(rows - 3):
        for y in range(cols - 3):
            if (game_board[x][y] == chip and game_board[x+1][y+1] == chip and game_board[x+2][y+2] == chip and game_board[x+3][y+3] == chip):
                print("\nWinner, winner, chicken-dinner!", chip, "wins! Thanks for playing!")
                return True

    return False

def coordinate_parser(input_string):
    coordinate = [None] * 2
    if(input_string[0] == "A"):
        coordinate[1] = 0
    elif(input_string[0] == "B"):
        coordinate[1] = 1
    elif(input_string[0] == "C"):
        coordinate[1] = 2
    elif(input_string[0] == "D"):
        coordinate[1] = 3
    elif(input_string[0] == "E"):
        coordinate[1] = 4
    elif(input_string[0] == "F"):
        coordinate[1] = 5
    elif(input_string[0] == "G"):
        coordinate[1] = 6
    else:
        print("Invalid Entry")
    coordinate[0] = int(input_string[1])
    return coordinate

def is_space_available(intended_coordinate):
    if(game_board[intended_coordinate[0]][intended_coordinate[1]] == "🔴"):
        return False
    elif(game_board[intended_coordinate[0]][intended_coordinate[1]] == "🔵"):
        return False
    return True

def modify_array(space_picked, turn):
    game_board[space_picked[0]][space_picked[1]] = turn

def gravity_checker(intended_coordinate):
    #Calculate space below
    space_below = [None] * 2
    space_below[0] = intended_coordinate[0] + 1
    space_below[1] = intended_coordinate[1]
    if(space_below[0] == 6):
        return True
    if (is_space_available(space_below) == False):
        return True
    return False

def first_turn():
    go = random.randint(1, 2)
    if go == 1:
        return "P1"
    else:
        return "P2"

#This list will tell the program whether we are playing a human or comp opponent
selected_opponent = []
turn = first_turn()

#Main Game Loop

game_over = False

while game_over == False:
    if game_over == True:
        print_game_board()
        break

    while turn != "P2":
        print_game_board()
        if game_over == False:
            player_choice = input("\nChoose a space:")
            coordinate = coordinate_parser(player_choice)
            try:
                if (is_space_available(coordinate) and gravity_checker(coordinate)):
                    modify_array(coordinate, "🔵")
                    turn = "P2"
                else:
                    print("Not a valid coordinate.")
            except:
                print("Error occured. Please try again.")
        if check_win("🔵"):
            game_over = True

    else:
        print_game_board()
        if game_over == False:
            cpu_choice = [random.choice(possible_letters), random.randint(0,5)]
            cpu_coordinate = coordinate_parser(cpu_choice)
            if(is_space_available(cpu_coordinate) and gravity_checker(cpu_coordinate)):
                modify_array(cpu_coordinate, "🔴")
                turn = "P1"
            if check_win("🔴"):
                game_over = True


                
    