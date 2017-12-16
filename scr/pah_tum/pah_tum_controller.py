"""TUI Game-mode Controller:

This module is in charge of letting players play in the TUI mode. A basic feature of the exercise
"""

import random
import tkinter as tk
import os
import sys

__author__ = "6785468: Robert am Wege, 6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"

def ai_controller(call_counter, game_mode, tic, blocked_numb, tiles_dict):
    """Ai Controller
    Uses the three functions (mod_get_score_row, mod_get_score_column and make_self_decision
    above to work, and emits a click signal to a specific label
    """
    if (call_counter == 0):
        call_counter = 1
    game_mode = 1

    if (tic < 49 - int(blocked_numb)):
        if (tic % 2 != 0):
            if (mod_get_score_row(tiles_dict) == -1 and
                    mod_get_score_column(tiles_dict) == -1):
                a = make_self_decision(tiles_dict)
                a = int(a[0]) * 7 + int(a[1])
                print("A List Index: ", a)
                tiles_dict[a] = "B"

            elif (mod_get_score_column(tiles_dict) == -1):
                a = mod_get_score_row(tiles_dict)  # returns int
                a = int(a[0]) * 7 + int(a[1])
                print("B List Index: ", a)
                tiles_dict[a] = "B"
            else:
                a = mod_get_score_column(tiles_dict)  # returns int
                a = int(a[0]) + int(a[1]) * 7
                print("C List Index: ", a)
                tiles_dict[a] = "B"

    return tiles_dict, game_mode, call_counter

def mod_get_score_row(tiles_dict):
    for i in range(7):
        possible_score = ""
        for j in range(7):
            key = str(i) + str(j)
            if (tiles_dict[key] == "A"):
                possible_score += tiles_dict[key]
            elif (tiles_dict[key] == "B"):
                possible_score += tiles_dict[key]
            elif (tiles_dict[key] == "X"):
                possible_score += "X"
            else:
                possible_score += "_"
        print("Row:", i, possible_score)
        if (possible_score.find("A_A") != -1):
            if(possible_score.find("A_A") != -1):
                possible_key = str(i) + str(possible_score.find("A_A") + 1)
                return(possible_key)
            elif(possible_score.find("_AA") != -1):
                possible_key = str(i) + str(possible_score.find("_AA"))
                return(possible_key)
            elif(possible_score.find("AA_") != -1):
                possible_key = str(i) + str(possible_score.find("AA_") + 2)
                return(possible_key)
            elif(possible_score.find("A_A") != -1):
                possible_key = str(i) + str(possible_score.find("A_A") + 1)
                return(possible_key)
        elif (possible_score.find("A" * 2) != -1):
            if(possible_score.find("A_A") != -1):
                possible_key = str(i) + str(possible_score.find("A_A") + 1)
                return(possible_key)
            elif(possible_score.find("_AA") != -1):
                possible_key = str(i) + str(possible_score.find("_AA"))
                return(possible_key)
            elif(possible_score.find("AA_") != -1):
                possible_key = str(i) + str(possible_score.find("AA_") + 2)
                return(possible_key)
            elif(possible_score.find("A_A") != -1):
                possible_key = str(i) + str(possible_score.find("A_A") + 1)
                return(possible_key)
        elif (possible_score.find("_AA") != -1):
            if(possible_score.find("A_A") != -1):
                possible_key = str(i) + str(possible_score.find("A_A") + 1)
                return(possible_key)
            elif(possible_score.find("_AA") != -1):
                possible_key = str(i) + str(possible_score.find("_AA"))
                return(possible_key)
            elif(possible_score.find("AA_") != -1):
                possible_key = str(i) + str(possible_score.find("AA_") + 2)
                return(possible_key)
            elif(possible_score.find("A_A") != -1):
                possible_key = str(i) + str(possible_score.find("A_A") + 1)
                return(possible_key)
    return -1

def mod_get_score_column(tiles_dict):
    for j in range(7):
        possible_score = ""
        for i in range(7):
            key = str(i) + str(j)
            if (tiles_dict[key] == "A"):
                possible_score += tiles_dict[key]
            elif (tiles_dict[key] == "B"):
                possible_score += tiles_dict[key]
            elif (tiles_dict[key] == "X"):
                possible_score += "X"
            else:
                possible_score += "_"
        print("Column:", i, possible_score)
        if (possible_score.find("A_A") != -1):
            if(possible_score.find("A_A") != -1):
                possible_key = str(j) + str(possible_score.find("A_A") + 1)
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("_AA") != -1):
                possible_key = str(j) + str(possible_score.find("_AA"))
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("AA_") != -1):
                possible_key = str(j) + str(possible_score.find("AA_") + 2)
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("A_A") != -1):
                possible_key = str(j) + str(possible_score.find("A_A") + 1)
                print("Place Stone here", possible_key)
                return(possible_key)
        elif (possible_score.find("A" * 2) != -1):
            if(possible_score.find("A_A") != -1):
                possible_key = str(j) + str(possible_score.find("A_A") + 1)
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("_AA") != -1):
                possible_key = str(j) + str(possible_score.find("_AA"))
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("AA_") != -1):
                possible_key = str(j) + str(possible_score.find("AA_") + 2)
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("A_A") != -1):
                possible_key = str(j) + str(possible_score.find("A_A") + 1)
                print("Place Stone here", possible_key)
                return(possible_key)
        elif (possible_score.find("_AA" * 2) != -1):
            if(possible_score.find("A_A") != -1):
                possible_key = str(j) + str(possible_score.find("A_A") + 1)
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("_AA") != -1):
                possible_key = str(j) + str(possible_score.find("_AA"))
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("AA_") != -1):
                possible_key = str(j) + str(possible_score.find("AA_") + 2)
                print("Place Stone here", possible_key)
                return(possible_key)
            elif(possible_score.find("A_A") != -1):
                possible_key = str(j) + str(possible_score.find("A_A") + 1)
                print("Place Stone here", possible_key)
                return(possible_key)
    return -1

def make_self_decision(tiles_dict):
    for i in range(7):
        possible_place = ""
        for j in range(7):
            key = str(i) + str(j)
            if (tiles_dict[key] == "A"):
                possible_place += tiles_dict[key]
            elif (tiles_dict[key] == "B"):
                possible_place += tiles_dict[key]
            elif (tiles_dict[key] == "X"):
                possible_place += "X"
            else:
                possible_place += "_"
        print("Row  :", i, possible_place)
        if(possible_place.find("_") > -1):
            possible_place = str(i) + str(possible_place.find("_"))
            return(possible_place)
        else:
            continue


def get_score_column(player, tiles_dict):
    """Check score in columns.

    Checks if there are three or more stones from the same player in a row in a column.
    Assign the predefined points for the length of the row.
    player -- either 'A' or 'B' depending on which score is to check.
    """
    column_score = 0
    for j in range(7):
        possible_score = ""
        for i in range(7):
            key = str(i) + str(j)

            if (tiles_dict[key] == player):
                possible_score += tiles_dict[key]
            else:
                possible_score += "_"

        if (possible_score.count(player * 7) != 0):
            column_score += 119
        elif (possible_score.count(player * 6) != 0):
            column_score += 56
        elif (possible_score.count(player * 5) != 0):
            column_score += 25
        elif (possible_score.count(player * 4) != 0):
            column_score += 10
        elif (possible_score.count(player * 3) != 0):
            column_score += 3 * possible_score.count(player * 3)

    return (column_score)


def get_score_row(player, tiles_dict):
    """Check score in rows.

    Checks if there are three or more stones from the same player in a row in a field-row.
    Assign the predefined points for the length of the row.
    player -- either 'A' or 'B' depending on which score is to check.
    """
    row_score = 0
    for i in range(7):
        possible_score = ""
        for j in range(7):
            key = str(i) + str(j)

            if (tiles_dict[key] == player):
                possible_score += tiles_dict[key]
            else:
                possible_score += "_"

        if (possible_score.count(player * 7) != 0):
            row_score += 119
        elif (possible_score.count(player * 6) != 0):
            row_score += 56
        elif (possible_score.count(player * 5) != 0):
            row_score += 25
        elif (possible_score.count(player * 4) != 0):
            row_score += 10
        elif (possible_score.count(player * 3) != 0):
            row_score += 3 * possible_score.count(player * 3)

    return row_score


def autism():
    """Autism - to be renamed

    Here we should either open n = NN>0 Windows or more in sequence or open n windows all together
    We have to load special images for each a = root object. Like buy viagra, sexy girls in your 
    neihghbourhood lets find out bilals address to get him spooked a little bit.
    Sexy girls in (Bilals Area) are looking for fun
    Sexy Boooooooiz in Bilals Area are looking for hook up
    Buy our Kitchen Aid for 299

    """
    for i in range(2):
        a = tk.Tk()
        a.attributes("-topmost", True)
        photo = tk.PhotoImage(file="cat.gif")
        w = tk.Label(a, image=photo)
        w.image = photo
        w.pack()


def tiles_dict_constructor(blocked_numb):
    """Constructs the tiles dictionary and blocks random fields."""
    tiles_dict = {}
    for i in range(7):
        for j in range(7):
            a = str(i) + str(j)
            tiles_dict[a] = ""

    for i in range(blocked_numb):
        while True:
            n_random = random.randint(0, 6)
            m_random = random.randint(0, 6)
            key = str(n_random) + str(m_random)
            if tiles_dict[key] == "":
                break
            else:
                continue

        tiles_dict[key] = "X"

    return tiles_dict


def undo_func(move_list, tic, tiles_dict):
    """Undo-function lets you undo the last step, which is saved in a list."""
    if len(move_list) != 0:
        key = move_list[-1]
        tiles_dict[key] = ""
        move_list.remove(move_list[-1])
        tic = tic - 2

        return move_list, tic, tiles_dict


def check_for_row(tiles_dict, index):
    """This function checks if there is a row that gives points, to color."""
    # check rows
    try:
        if str(tiles_dict[str(index)]) == str(tiles_dict[index[0] + str(int(index[1]) + 1)]) == str(
                tiles_dict[index[0] + str(int(index[1]) + 2)]):
            return True
    except KeyError:
        None

    try:
        if str(tiles_dict[str(index)]) == str(tiles_dict[index[0] + str(int(index[1]) + 1)]) == str(
                tiles_dict[index[0] + str(int(index[1]) - 1)]):
            return True
    except KeyError:
        None

    try:
        if str(tiles_dict[str(index)]) == str(tiles_dict[index[0] + str(int(index[1]) - 1)]) == str(
                tiles_dict[index[0] + str(int(index[1]) - 2)]):
            return True
    except KeyError:
        None

    # check columns
    try:
        if str(tiles_dict[str(index)]) == str(tiles_dict[str(int(index[0]) + 1) + index[1]]) == str(
                tiles_dict[str(int(index[0]) + 2) + index[1]]):
            return True
    except KeyError:
        None

    try:
        if str(tiles_dict[str(index)]) == str(tiles_dict[str(int(index[0]) - 1) + index[1]]) == str(
                tiles_dict[str(int(index[0]) + 1) + index[1]]):
            return True
    except KeyError:
        None

    try:
        if str(tiles_dict[str(index)]) == str(tiles_dict[str(int(index[0]) - 1) + index[1]]) == str(
                tiles_dict[str(int(index[0]) - 2) + index[1]]):
            return True
    except KeyError:
        None


def field_printer(tiles_dict):
    """This procedure gets the current state of the field and prints it."""
    # for Windows-user
    if os.name == "nt":
        to_print = "\n   0   1   2   3   4   5   6  \n"
        for i in range(0, 7):
            to_print += str(i) + " "
            for j in range(0, 7):
                index = str(i) + str(j)
                if str(tiles_dict[index]) == "":
                    to_draw = "[ ]"
                elif str(tiles_dict[index]) == "X":
                    to_draw = '[/]'
                elif str(tiles_dict[index]) == "A":
                    to_draw = '[X]'
                elif str(tiles_dict[index]) == "B":
                    to_draw = '[O]'
                to_print += to_draw + " "

            to_print += "\n \n"

    # for OS X and Linux
    else:
        to_print = "\n   0   1   2   3   4   5   6  \n"
        for i in range(0, 7):
            to_print += str(i) + " "
            for j in range(0, 7):
                index = str(i) + str(j)
                if str(tiles_dict[index]) == "":
                    to_draw = "[ ]"
                elif str(tiles_dict[index]) == "X":
                    to_draw = '\033[1;47m[I]\033[1;m'
                elif str(tiles_dict[index]) == "A":
                    if check_for_row(tiles_dict, index) is True:
                        to_draw = '\033[1;41m[X]\033[1;m'
                    else:
                        to_draw = '\033[1;31m[X]\033[1;m'
                elif str(tiles_dict[index]) == "B":
                    if check_for_row(tiles_dict, index) is True:
                        to_draw = '\033[1;42m[O]\033[1;m'
                    else:
                        to_draw = '\033[1;32m[O]\033[1;m'
                to_print += to_draw + " "

            to_print += "\n \n"

    print(to_print)


def controller():
    """The main controller of the TUI game.

    This controller is the heart of the TUI game, being in charge of coordinating all procedures
    and function, that are needed for a good game-flow.
    The game is active when we are in the second while-loop. The first one takes the input for
    the number of blocked tiles.
    """

    if os.name != "nt":  # only for OS X and Linux
        os.system('clear')
    game_mode = 0
    call_counter = 0
    tic = 0
    move_list = []  # list of the last moves, later needed for undo-func.
    while True:
        blocked_numb = input("How many blocked tiles do you want to play with? "
                             "Choose an uneven number between 5 and 13.  ")
        if blocked_numb == "exit":
            sys.exit()
        if blocked_numb in ["5", "7", "9", "11", "13"]:
            blocked_numb = int(blocked_numb)
            break
        else:
            print("You didn't enter a valid input.")
    tiles_dict = tiles_dict_constructor(blocked_numb)
    field_printer(tiles_dict)

    while tic < 49 - blocked_numb:
        if tic % 2 == 0:
            print("Player 1 it's your turn.")
        elif tic % 2 == 1:
            print("Player 2, it's you who shall set his figure.")

        while True:
            tile = input("Please type your Field you want to assign to your stone.")
            tile = tile.replace(" ", "")
            if tile == "undo":
                print("Undoing last step...")
                move_list, tic, tiles_dict = undo_func(move_list, tic, tiles_dict)
                print(tic, move_list, tiles_dict)
                break
            elif tile == "exit":
                print("Okay, bye.")
                sys.exit()
            elif tile == "restart":
                print("Restarting Game")
                controller()
                return
            elif tile == "menu":
                return
            try:
                if tiles_dict[tile] == "":
                    move_list.append(tile)
                    break
                else:
                    print("\nYou didn't enter a valid input. Either type in your tile-coordinate"
                          " (like '14') on which you want to put your stone or type 'menu', "
                          "'exit' or 'restart'. For further information look at our help file in "
                          "the menu. FYI your tile should be empty ;)")
                    continue
            except KeyError:
                continue

        if tile.isdigit():
            if tic % 2 == 0:
                tiles_dict[tile] = "A"

            elif tic % 2 == 1:
                tiles_dict[tile] = "B"

        if os.name != "nt":
            os.system('clear')
        field_printer(tiles_dict)

        # gets and prints the score for player 1 and player 2
        p1_column = get_score_column("A", tiles_dict)
        p1_row = get_score_row("A", tiles_dict)
        print("Score of Player 1 =", p1_column + p1_row)
        p2_column = get_score_column("B", tiles_dict)
        p2_row = get_score_row("B", tiles_dict)
        print("Score of Player 2 =", p2_column + p2_row)

        tic += 1

        # turn over. next players turn.

    print("\n Well played guys! \nGame is over")

    p1_score = get_score_column("A", tiles_dict) + get_score_row("A", tiles_dict)
    p2_score = get_score_column("B", tiles_dict) + get_score_row("B", tiles_dict)

    if p1_score > p2_score:
        print("\n Player 1 you have to most points, therefore you have won. Congratulations!")
    elif p1_score < p2_score:
        print("\n Player 2 you have to most points, therefore you have won. Congratulations!")
    else:
        print("You have the same number of points. No one won, you are both looser ;)")
