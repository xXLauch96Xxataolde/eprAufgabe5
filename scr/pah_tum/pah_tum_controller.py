"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import random
import tkinter as tk
import os
import sys

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


def get_score_column(player, tiles_dict):
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

        tiles_dict[key] = "blocked"

    return tiles_dict


def undo_func(move_list, tic, tiles_dict):
    if len(move_list) != 0:
        key = move_list[-1]
        tiles_dict[key] = ""
        move_list.remove(move_list[-1])
        tic = tic - 2

        return move_list, tic, tiles_dict


def check_for_row(tiles_dict, index):
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
    if os.name == "nt":
        to_print = "\n   0   1   2   3   4   5   6  \n"
        for i in range(0, 7):
            to_print += str(i) + " "
            for j in range(0, 7):
                index = str(i) + str(j)
                if str(tiles_dict[index]) == "":
                    to_draw = "[ ]"
                elif str(tiles_dict[index]) == "blocked":
                    to_draw = '[/]'
                elif str(tiles_dict[index]) == "player1":
                    to_draw = '[X]'
                elif str(tiles_dict[index]) == "player2":
                    to_draw = '[O]'
                to_print += to_draw + " "

            to_print += "\n \n"

    else:
        to_print = "\n   0   1   2   3   4   5   6  \n"
        for i in range(0, 7):
            to_print += str(i) + " "
            for j in range(0, 7):
                index = str(i) + str(j)
                if str(tiles_dict[index]) == "":
                    to_draw = "[ ]"
                elif str(tiles_dict[index]) == "blocked":
                    to_draw = '\033[1;47m[I]\033[1;m'
                elif str(tiles_dict[index]) == "player1":
                    if check_for_row(tiles_dict, index) is True:
                        to_draw = '\033[1;41m[X]\033[1;m'
                    else:
                        to_draw = '\033[1;31m[X]\033[1;m'
                elif str(tiles_dict[index]) == "player2":
                    if check_for_row(tiles_dict, index) is True:
                        to_draw = '\033[1;42m[O]\033[1;m'
                    else:
                        to_draw = '\033[1;32m[O]\033[1;m'
                to_print += to_draw + " "

            to_print += "\n \n"

    print(to_print)


def controller():
    os.system('clear')
    tic = 0
    move_list = []
    while True:
        blocked_numb = input("How many blocked tiles do you want to play with? "
                             "Choose an uneven number between 5 and 13.  ")
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
                    print("\nYou didn't enter a valid input. Either type in your tile-coordinate on"
                          " which you want to put your stone or type 'menu', 'exit' or 'restart'."
                          " For further information look at our help file in the menu.")
                    continue
            except KeyError:
                continue
        if tile.isdigit():
            if tic % 2 == 0:
                tiles_dict[tile] = "player1"

            elif tic % 2 == 1:
                tiles_dict[tile] = "player2"
        os.system('clear')
        field_printer(tiles_dict)

        p1_column = get_score_column("player1", tiles_dict)
        p1_row = get_score_row("player1", tiles_dict)

        print("Score of Player 1 =", p1_column + p1_row)

        p2_column = get_score_column("player2", tiles_dict)
        p2_row = get_score_row("player2", tiles_dict)

        print("Score of Player 2 =", p2_column + p2_row)

        tic += 1

    print("\n Well played guys! \nGame is over")

    p1_score = get_score_column("player1", tiles_dict) + get_score_row("player1", tiles_dict)
    p2_score = get_score_column("player2", tiles_dict) + get_score_row("player2", tiles_dict)

    if p1_score > p2_score:
        print("\n Player 1 you have to most points, therefore you have won. Congratulations!")
    elif p1_score < p2_score:
        print("\n Player 2 you have to most points, therefore you have won. Congratulations!")
    else:
        print("You have the same number of points. No one won, you are both looser ;)")
