"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import random
import pah_tum_controller
import sys
from pah_tum_controller_class import PahTum
from pah_tum_controller_class2 import PahTumAI
import tkinter as tk


__author__ = "6785468: Robert am Wege, 6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def menue():
    """a procedure for printing a menue we assume"""

    print("...Welcome to the Menue....................")
    print("...........................................")
    print("...Press 1 to start Pah Tum TUI Mode.......")
    print("...Press 2 to start Pah Tum GUI PvP Mode...")
    print("...Press 3 to start Pah Tum GUI AI Mode....")
    print("...Press 4 to see the manual...............")
    print("...Press 5 to exit.........................")
    print("...........................................")
    print("...........................................")


def helpings_gui():
    """A gui version of the help file"""
    window = tk.Tk()
    file = open("game-manual.txt")
    data = file.read()
    file.close()
    results = tk.Label(window, text=data)
    results.grid(row=1, column=1)
    window.attributes("-topmost", True)
    window.mainloop()


def helpings():
    """Procedure for opening a file and printing it to the console."""

    print("\n")
    fobj = open("game-manual.txt")
    for line in fobj:
        print(line.rstrip())

    print("\n")
    fobj.close()
    print("Press any button to exit\n")


def main():

    while(True):
        menue()
        inp = ""
        inp = input()
        if (inp == "1"):
            pah_tum_controller.controller()
            inp = ""
        elif (inp == "2"):
            root = tk.Tk()
            obj = PahTum(root)
            root.mainloop()
            inp = ""
        elif (inp == "3"):
            root = tk.Tk()
            obj = PahTumAI(root)
            root.mainloop()
            inp = ""
        elif (inp == "4"):
            helpings()
            helpings_gui()
            inp = ""
        elif (inp == "5"):
            sys.exit()
        else:
            print("Wrong Input. Choose a number between 1 and 5, please\n")


if __name__ == '__main__':
    main()
