"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import random
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import sys
import os
# from pah_tum.pah_tum_controller import color_change
import time
from tkinter.messagebox import showwarning

__author__ = "6785468: Robert am Wege, 6770541: Niels Heissel"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


class PahTumAI():
    tiles_dict = {}
    move_list = []
    game_mode = 0
    rand_start = 0
    call_counter = 0  # to count the number of calls for ai_controller

    def __init__(self, root, tic=0):
        """The Constructor

        Called from the main, and handed over a tk root, which is the basis for the window.
        In the constructor we bind every widget to its belonging root window
        """
        self.root = root
        self.tic = tic
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.geometry('+900+50')  # sets the default window position
        self.root.title("Pah Tum")

        self.wait = tk.Toplevel()
        self.wait.attributes("-topmost", True)
        self.wait.geometry('+900+50')  # sets the default window position to do: Wdht and height
        prompt_string = '{:^80}'.format("Please selected number of blocked tiles")
        self.label_1 = tk.Label(self.wait, text=prompt_string)
        self.blocked_numb = tk.StringVar(self.wait)
        self.blocked_numb.set("Select number")  # initial value
        self.blocked_tiles = ttk.OptionMenu(
            self.wait, self.blocked_numb, "5", "7", "9", "11", "13")
        self.click = tk.Button(self.wait, text="OK", command=self.enter_configs)
        self.label_1.pack()
        self.blocked_tiles.pack()
        self.click.pack()
        self.root.wm_withdraw()

        count = 0
        for i in range(7):
            for j in range(7):
                count += 1
                self.a = "l" + str(i + 1) + str(j + 1)
                self.a = tk.Label(self.root, width=6, height=3,
                                  bg="light cyan", highlightthickness=1, highlightbackground= "grey")
                self.a.bind("<Button-1>", self.color_change)
                self.a.grid(row=i, column=j)

        self.tic_label = tk.Label(self.root, text="Tic: ", width=6, height=3,
                                  bg="plum2", highlightthickness=1, highlightbackground= "grey")
        self.tic_label.grid(row=0, column=8)

        self.score_label_1 = tk.Label(self.root, text="Score: ", width=6, height=3,
                                      bg="palegreen", highlightthickness=1, highlightbackground= "grey")
        self.score_label_1.grid(row=1, column=8)

        self.score_label_2 = tk.Label(self.root, text="Score: ", width=6, height=3,
                                      bg="tomato", highlightthickness=1, highlightbackground= "grey")
        self.score_label_2.grid(row=2, column=8)

        self.undo_label = tk.Label(self.root, text="Undo", width=6, height=3,
                                   bg="mediumpurple2", highlightthickness=1, highlightbackground= "grey")
        self.undo_label.grid(row=3, column=8)
        self.undo_label.bind("<Button-1>", self.undo_func)  # Undo Button constructed

        self.ai_label = tk.Label(self.root, text="START", width=6, height=3,
                                 bg="firebrick", highlightthickness=1, highlightbackground= "grey", cursor="gumby")
        self.ai_label.grid(row=4, column=8)
        self.ai_label.bind("<Button-1>", self.ai_controller)  # Ai Mode Button constructed

        self.restart_label = tk.Label(self.root, text="Restart", width=6, height=3,
                                      bg="bisque2", highlightthickness=1, highlightbackground= "grey")
        self.restart_label.grid(row=5, column=8)
        self.restart_label.bind("<Button-1>", self.restart)  # Restart Button constructed

        self.exit_label = tk.Label(self.root, text="Exit", width=6, height=3,
                                   bg="SteelBlue", highlightthickness=1, highlightbackground= "grey")
        self.exit_label.grid(row=6, column=8)
        self.exit_label.bind("<Button-1>", self.exit)  # Exit Button constructed

        self.root.mainloop

        self.tiles_dict_constructor()
        self.rand_start_assigner()  # generates the starting player for ai game mode

    def restart(self, event):
        "something with an exit code maybe"
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def rand_start_assigner(self):
        rand_start = random.randint(0, 1)
        self.rand_start = rand_start

    def enter_configs(self):
        if self.blocked_numb.get() == "Select number":
            self.label_1.config(text="Please select from dropdown!")
        else:
            self.tiles_blocker()
            self.wait.destroy()
            self.root.deiconify()

    def undo_func(self, event):
        if len(self.move_list) != 0:
            print(self.move_list)
            slaves_list = []
            slaves_list.extend(self.root.grid_slaves())
            slaves_list.reverse()
            key = self.move_list[-1]
            self.tiles_dict[key] = ""
            key = self.coord_to_tile_number(key)
            slaves_list[int(key) - 1].config(bg="light cyan")
            self.move_list.remove(self.move_list[-1])
            self.tic = self.tic - 1
            self.tic_label.config(text="Tic: " + str(self.tic))
            self.get_score()
        else:
            if (self.game_mode == 1):
                self.ai_controller(event)

    def read_tic(self):
        """returns the tic"""
        return self.tic

    def inc_tic(self, tic):
        """increases the tic"""
        a = self.read_tic()
        self.tic = (a + 1)

    def color_change(self, event):
        """Partly a core function. recolors every label, keeps the score, increases the tic"""
        if (self.call_counter == 0):
            showwarning("Start", "Please press Start on the right")

        elif (self.tic < 49 - int(self.blocked_numb.get())):

            # print("Tic", self.tic)

            self.label_coordinator(event.widget)

            if (self.tic % 2 == 0):
                if (self.tiles_dict[self.label_coordinator(event.widget)] == ""):
                    self.tiles_dict[self.label_coordinator(
                        event.widget)] = "A"
                    event.widget.config(bg="lightgreen")
                    self.inc_tic(self.tic)
                    tic_str = "Tic: " + str(self.read_tic())
                    self.tic_label.config(text=tic_str)
                    self.move_list.append(self.label_coordinator(event.widget))

            else:
                if (self.tiles_dict[self.label_coordinator(event.widget)] == ""):
                    self.tiles_dict[self.label_coordinator(
                        event.widget)] = "B"
                    event.widget.config(bg="tomato")
                    self.inc_tic(self.tic)
                    tic_str = "Tic: " + str(self.read_tic())
                    self.tic_label.config(text=tic_str)
                    self.move_list.append(self.label_coordinator(event.widget))

            self.get_score()
        else:
            score1, score2 = self.get_score()
            if (score1 > score2):
                winner_string = "Congrats Player1, you are the Winner"
                messagebox.showinfo("WINNER", winner_string)
            elif (score1 < score2):
                winner_string = "Congrats Player2, you are the Winner"
                messagebox.showinfo("WINNER", winner_string)
            else:
                winner_string = "Congrats you are both Winners"
                messagebox.showinfo("WINNER", winner_string)

        if (self.game_mode == 1):
            self.ai_controller(event)

    def controller(self):
        print("Controller does nothing.")

    def tiles_dict_constructor(self):
        """Puts every tile coordinate in a dict"""
        for i in range(7):
            for j in range(7):
                a = str(i) + str(j)
                self.tiles_dict[a] = ""

    def label_coordinator(self, label_widget):
        """Allows to transform a coordinate into a tiles number"""
        if len(str(label_widget)) == 9:
            coordninates = str(label_widget)[-2:]
        elif len(str(label_widget)) == 8:
            coordninates = str(label_widget)[-1]
        else:
            coordninates = 1

        coordninates = int(coordninates)

        dict_key1 = (coordninates - 1) // 7
        dict_key2 = (coordninates - 1) % 7

        return str(dict_key1) + str(dict_key2)

    def on_enter(self, event):
        """if a tile is blocked, tic label shows blocked"""
        self.tic_label.configure(text="Blocked")

    def on_leave(self, event):
        """reverses the on_enter effect"""
        self.tic_label.configure(text="Tic: " + str(self.read_tic()))

    def tiles_blocker(self):
        """blocks the tiles"""
        tiles_number_to_block = int(self.blocked_numb.get())

        slaves_list = []
        slaves_list.extend(self.root.grid_slaves())
        slaves_list.reverse()

        for i in range(tiles_number_to_block):
            while True:
                n_random = random.randint(0, 6)
                m_random = random.randint(0, 6)
                key = str(n_random) + str(m_random)
                if self.tiles_dict[key] == "":
                    break
                else:
                    continue
            self.tiles_dict[key] = "X"

            key = self.coord_to_tile_number(key)
            print(key)
            slaves_list[int(key) - 1].config(bg="ivory")
            print(slaves_list[int(key) - 1])
            slaves_list[int(key) - 1].bind("<Enter>", self.on_enter)
            slaves_list[int(key) - 1].bind("<Leave>", self.on_leave)

    def coord_to_tile_number(self, coord):
        """translates a tile to a coordinate"""
        if (len(str(coord)) == 1):
            tile_number = str(0) + str(int(coord + 1))
            return tile_number
        else:
            tile_number = str(int(coord[0]) * 7 + int(coord[1]) + 1)
            return tile_number

    def get_score_column(self, player):
        """Function to add and return all possible column scores"""
        column_score = 0
        for j in range(7):
            possible_score = ""
            for i in range(7):
                key = str(i) + str(j)

                if (self.tiles_dict[key] == player):
                    possible_score += self.tiles_dict[key]
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

    def get_score_row(self, player):
        """Function to add and return all possible row scores"""
        row_score = 0
        for i in range(7):
            possible_score = ""
            for j in range(7):
                key = str(i) + str(j)

                if (self.tiles_dict[key] == player):
                    possible_score += self.tiles_dict[key]
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

        return (row_score)

    def mod_get_score_row(self):
        """Part of the ai

        Functions to determine if a row offers a nice place for the ai to place its stone on
        """
        for i in range(7):
            possible_score = ""
            for j in range(7):
                key = str(i) + str(j)

                if (self.tiles_dict[key] == "A"):
                    possible_score += self.tiles_dict[key]
                elif (self.tiles_dict[key] == "B"):
                    possible_score += self.tiles_dict[key]
                elif (self.tiles_dict[key] == "X"):
                    possible_score += "X"
                else:
                    possible_score += "_"

            print("Row:", i, possible_score)
            if(self.rand_start == 1):
                if (possible_score.find("B_B") != -1):
                    if(possible_score.find("B_B") != -1):
                        possible_key = str(i) + str(possible_score.find("B_B") + 1)
                        return(possible_key)
                    elif(possible_score.find("_BB") != -1):
                        possible_key = str(i) + str(possible_score.find("_BB"))
                        return(possible_key)
                    elif(possible_score.find("BB_") != -1):
                        possible_key = str(i) + str(possible_score.find("BB_") + 2)
                        return(possible_key)
                    elif(possible_score.find("B_B") != -1):
                        possible_key = str(i) + str(possible_score.find("B_B") + 1)
                        return(possible_key)
                elif (possible_score.find("B" * 2) != -1):
                    if(possible_score.find("B_B") != -1):
                        possible_key = str(i) + str(possible_score.find("B_B") + 1)
                        return(possible_key)
                    elif(possible_score.find("_BB") != -1):
                        possible_key = str(i) + str(possible_score.find("_BB"))
                        return(possible_key)
                    elif(possible_score.find("BB_") != -1):
                        possible_key = str(i) + str(possible_score.find("BB_") + 2)
                        return(possible_key)
                    elif(possible_score.find("B_B") != -1):
                        possible_key = str(i) + str(possible_score.find("B_B") + 1)
                        return(possible_key)
                elif (possible_score.find("_BB") != -1):
                    if(possible_score.find("B_B") != -1):
                        possible_key = str(i) + str(possible_score.find("B_B") + 1)
                        return(possible_key)
                    elif(possible_score.find("_BB") != -1):
                        possible_key = str(i) + str(possible_score.find("_BB"))
                        return(possible_key)
                    elif(possible_score.find("BB_") != -1):
                        possible_key = str(i) + str(possible_score.find("BB_") + 2)
                        return(possible_key)
                    elif(possible_score.find("B_B") != -1):
                        possible_key = str(i) + str(possible_score.find("B_B") + 1)
                        return(possible_key)
            elif (self.rand_start == 0):
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

    def mod_get_score_column(self):
        """Part of the ai

        Functions to determine if a column offers a nice place for the ai to place its stone on
        """
        for j in range(7):
            possible_score = ""
            for i in range(7):
                key = str(i) + str(j)

                if (self.tiles_dict[key] == "A"):
                    possible_score += self.tiles_dict[key]
                elif (self.tiles_dict[key] == "B"):
                    possible_score += self.tiles_dict[key]
                elif (self.tiles_dict[key] == "X"):
                    possible_score += "X"
                else:
                    possible_score += "_"

            print("Column:", i, possible_score)
            if(self.rand_start == 1):
                if (possible_score.find("B_B") != -1):
                    if(possible_score.find("B_B") != -1):
                        possible_key = str(j) + str(possible_score.find("B_B") + 1)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("_BB") != -1):
                        possible_key = str(j) + str(possible_score.find("_BB"))
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("BB_") != -1):
                        possible_key = str(j) + str(possible_score.find("BB_") + 2)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("B_B") != -1):
                        possible_key = str(j) + str(possible_score.find("B_B") + 1)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                elif (possible_score.find("B" * 2) != -1):
                    if(possible_score.find("B_B") != -1):
                        possible_key = str(j) + str(possible_score.find("B_B") + 1)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("_BB") != -1):
                        possible_key = str(j) + str(possible_score.find("_BB"))
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("BB_") != -1):
                        possible_key = str(j) + str(possible_score.find("BB_") + 2)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("B_B") != -1):
                        possible_key = str(j) + str(possible_score.find("B_B") + 1)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                elif (possible_score.find("_BB") != -1):
                    if(possible_score.find("B_B") != -1):
                        possible_key = str(j) + str(possible_score.find("B_B") + 1)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("_BB") != -1):
                        possible_key = str(j) + str(possible_score.find("_BB"))
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("BB_") != -1):
                        possible_key = str(j) + str(possible_score.find("BB_") + 2)
                        print("Place Stone here", possible_key)
                        return(possible_key)
                    elif(possible_score.find("B_B") != -1):
                        possible_key = str(j) + str(possible_score.find("B_B") + 1)
                        print("Place Stone here", possible_key)
                        return(possible_key)
            elif (self.rand_start == 0):
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

    def make_self_decision(self):
        """Make self Decision

        If a row or a column doesnt offer a nice tile to intercept any scoring ambitions, the ai 
        chooses to go for some scoring points itself
        """
        for i in range(7):
            possible_place = ""
            for j in range(7):
                key = str(i) + str(j)

                if (self.tiles_dict[key] == "A"):
                    possible_place += self.tiles_dict[key]
                elif (self.tiles_dict[key] == "B"):
                    possible_place += self.tiles_dict[key]
                elif (self.tiles_dict[key] == "X"):
                    possible_place += "X"
                else:
                    possible_place += "_"

            print("Row  :", i, possible_place)
            if(possible_place.find("_") > -1):
                possible_place = str(i) + str(possible_place.find("_"))
                return(possible_place)
            else:
                continue

    def get_score(self):
        """Combines row and column score and prints it to a score label"""
        total_score_1 = 0
        row_score_1 = self.get_score_row("A")
        column_score_1 = self.get_score_column("A")
        total_score_1 += row_score_1 + column_score_1
        self.score_label_1.config(text=str(total_score_1))

        total_score_2 = 0
        row_score_2 = self.get_score_row("B")
        column_score_2 = self.get_score_column("B")
        total_score_2 += row_score_2 + column_score_2
        self.score_label_2.config(text=str(total_score_2))

        return(total_score_1, total_score_2)

    def game_over(self):
        """If tic reaches 49 minus blocked tiles, the game is over"""
        self.toplevel = tk.Toplevel()
        self.label1 = tk.Label(self.toplevel, text="Game Over", height=6, width=18)
        self.label1.pack()
        self.toplevel.attributes("-topmost", True)  # put the root to foreground
        self.toplevel.geometry('+920+70')

    def exit(self, event):
        """for exiting the program"""
        sys.exit()

    def start_communicator(self):
        """tells a player if he is player 1 or 2"""
        if (self.rand_start == 0):
            messagebox.showinfo("Player initialization", "Randomly chosen Player 1 to start")
        elif (self.rand_start == 1):
            messagebox.showinfo("Player initialization", "Randomly chosen the Computer to start")

    def clear_game(self, event):
        """clears the game"""
        for k in self.tiles_dict:
            self.undo_func(event)

    def ai_controller(self, event):
        """Ai Controller

        Uses the three functions (mod_get_score_row, mod_get_score_column and make_self_decision
        above to work, and emits a click signal to a specific label
        """
        if (self.call_counter == 0):
            self.start_communicator()
            self.clear_game(event)
            self.call_counter = 1

        self.game_mode = 1
        slaves_list = []
        slaves_list.extend(self.root.grid_slaves())
        slaves_list.reverse()
        slaves_list = slaves_list[0: 48]
        if (self.tic < 49 - int(self.blocked_numb.get())):
            if (self.tic % 2 != self.rand_start):

                if (self.mod_get_score_row() == -1 and
                        self.mod_get_score_column() == -1):

                    a = self.make_self_decision()
                    a = int(a[0]) * 7 + int(a[1])
                    print("A List Index: ", a)
                    print(slaves_list[a].event_generate("<Button-1>"))

                elif (self.mod_get_score_column() == -1):
                    a = self.mod_get_score_row()  # returns int
                    a = int(a[0]) * 7 + int(a[1])
                    print("B List Index: ", a)
                    print(slaves_list[a].event_generate("<Button-1>"))
                else:
                    a = self.mod_get_score_column()  # returns int
                    a = int(a[0]) + int(a[1]) * 7
                    print("C List Index: ", a)
                    print(slaves_list[a].event_generate("<Button-1>"))

    def __del__(self):
        print("Instance deleted.")
