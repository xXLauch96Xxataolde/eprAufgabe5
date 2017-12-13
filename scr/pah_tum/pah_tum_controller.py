"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import random
import tkinter as tk
import os

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


def read_tic(tic):
    return tic


def inc_tic():
    a = read_tic()
    return (a + 1)


def color_change(event):
    print("something", event.widget)
    event.widget.config(bg="lightgreen")


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
        n_random = random.randint(0, 6)
        m_random = random.randint(0, 6)
        key = str(n_random) + str(m_random)
        tiles_dict[key] = "blocked"

    return tiles_dict


def convert_tile_to_coord(tile):
    # here we convert char into numbers 'A2' => '02'
    # maybe change your dict keys...
    None


def controller():
    tic = 0
    move_list = []
    while True:
        blocked_numb = input("How many blocked tiles do you want to play with?")
        if blocked_numb in ["5", "7", "9", "11", "13"]:
            blocked_numb = int(blocked_numb)
            break
        else:
            print("You didn't enter a number.")
    tiles_dict = tiles_dict_constructor(blocked_numb)

    while tic < 49 - blocked_numb:
        tic += 1
        print(tiles_dict)

        while True:
            tile = input("Please type your Field you want to assign to your stone.")

            if tile:
                break
            else:
                continue

        if tic % 2 == 0:
            print("Player 1 it's your turn.")
            tiles_dict[tile] = "player1"

        elif tic % 2 == 1:
            print("Player 2, it's you who shall set his figure.")
            tiles_dict[tile] = "player2"


        os.system('cls')
        abc = ["A", "B", "C", "D", "E", "F", "G"]
        to_print = "\n   0   1   2   3   4   5   6  \n"
        for i in range(0, 7):
            to_print += str(i) + " "
            for j in range(0, 7):
                index = str(i) + str(j)
                if str(tiles_dict[index]) == "":
                    to_draw = "[ ]"
                elif str(tiles_dict[index]) == "blocked":
                    to_draw = "[/]"
                elif str(tiles_dict[index]) == "player1":
                    to_draw = "[X]"
                elif str(tiles_dict[index]) == "player2":
                    to_draw = "[O]"
                to_print += to_draw + " "

            to_print += "\n \n"

        print(to_print)

    print("Well played guys! \n Game is over")
