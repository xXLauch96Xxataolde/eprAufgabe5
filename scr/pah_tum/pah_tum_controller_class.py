"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import random
import tkinter as tk
from tkinter import PhotoImage

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


class PahTum():
    tiles_dict = {}
    move_list = []

    def __init__(self, root, tic=0):
        self.root = root
        self.tic = tic
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.geometry('+900+50')  # sets the default window position
        self.root.title("Pah Tuuuum, Niels ist duuuum")
        count = 0
        for i in range(7):
            for j in range(7):
                count += 1
                self.a = "l" + str(i + 1) + str(j + 1)
                self.a = tk.Label(self.root, text=self.a, width=6, height=3,
                                  bg="light cyan", borderwidth=0.5)
                self.a.bind("<Button-1>", self.color_change)
                self.a.grid(row=i, column=j)

        self.tic_label = tk.Label(self.root, text="Tic: ", width=6, height=3,
                                  bg="plum2", borderwidth=1, relief="solid")
        self.tic_label.grid(row=0, column=8)

        self.score_label_1 = tk.Label(self.root, text="Score: ", width=6, height=3,
                                    bg="palegreen", borderwidth=1, relief="solid")
        self.score_label_1.grid(row=1, column=8)

        self.score_label_2 = tk.Label(self.root, text="Score: ", width=6, height=3,
                                    bg="tomato", borderwidth=1, relief="solid")
        self.score_label_2.grid(row=2, column=8)

        self.undo_label = tk.Label(self.root, text="Undo", width=6, height=3,
                                    bg="mediumpurple2", borderwidth=1, relief="solid")
        self.undo_label.grid(row=3, column=8)
        self.undo_label.bind("<Button-1>", self.undo_func)  # Undo Button constructed
        
        print(self.root.grid_slaves())
        self.root.mainloop

        self.tiles_dict_constructor()
        self.tiles_blocker()
        print(self.tiles_dict)

        print(self.coord_to_tile_number("15"))
    
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
    
    def read_tic(self):
        return self.tic

    def inc_tic(self, tic):
        a = self.read_tic()
        self.tic = (a + 1)

    def color_change(self, event):
        
        if (self.tic < 49):
            print("something", event.widget)
    
            print("Tic", self.tic)
    
            self.label_coordinator(event.widget)
    
            if (self.tic % 2 == 0):
                if (self.tiles_dict[self.label_coordinator(event.widget)] == ""):
                    self.tiles_dict[self.label_coordinator(
                        event.widget)] = "player1"
                    event.widget.config(bg="lightgreen")
                    self.inc_tic(self.tic)
                    tic_str = "Tic: " + str(self.read_tic())
                    self.tic_label.config(text=tic_str)
                    print(self.tiles_dict)
                    self.move_list.append(self.label_coordinator(event.widget))
    
            else:
                if (self.tiles_dict[self.label_coordinator(event.widget)] == ""):
                    self.tiles_dict[self.label_coordinator(
                        event.widget)] = "player2"
                    event.widget.config(bg="tomato")
                    self.inc_tic(self.tic)
                    tic_str = "Tic: " + str(self.read_tic())
                    self.tic_label.config(text=tic_str)
                    print(self.tiles_dict)
                    self.move_list.append(self.label_coordinator(event.widget))
            
            
            self.get_score()
        else:
            print("GAME OVER GAME OVER")
            # something with a prompt box

    def autism(self):
        """Autism - to be renamed

        Here we should either open n = NN>0 Windows or more in sequence or openn windows all together
        We have to load special images for each a = root object. Like buy viagra, sexy girls in your neihghbourhood
        lets find out bilals address to get him spooked a little bit.
        Sexy girls in (Bilals Area) are looking for fun
        Sexy Boooooooiz in Bilals Area are looking for hook up
        Buy our Kitchen Aid for 299

        """
        for i in range(2):
            a = tk.Tk()
            a.attributes("-topmost", True)
            photo = PhotoImage(file="cat.gif")
            w = tk.Label(a, image=photo)
            w.photo = photo
            w.pack()

    def controller(self):
        print("Controller does nothing.")

    def tiles_dict_constructor(self):
        for i in range(7):
            for j in range(7):
                a = str(i) + str(j)
                self.tiles_dict[a] = ""

    def label_coordinator(self, label_widget):
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
        self.tic_label.configure(text="Blocked")

    def on_leave(self, event):
        self.tic_label.configure(text="Tic: " + str(self.read_tic()))

    def tiles_blocker(self):
        tiles_number_to_block = [5, 7, 9, 11, 13]
        tiles_number_to_block = random.choice(tiles_number_to_block)

        slaves_list = []
        slaves_list.extend(self.root.grid_slaves())
        slaves_list.reverse()
        # print(slaves_list)

        for i in range(tiles_number_to_block):
            n_random = random.randint(0, 6)
            m_random = random.randint(0, 6)
            key = str(n_random) + str(m_random)
            self.tiles_dict[key] = "blocked"

            key = self.coord_to_tile_number(key)
            print(key)
            slaves_list[int(key) - 1].config(bg="ivory")
            print(slaves_list[int(key) - 1])
            slaves_list[int(key) - 1].bind("<Enter>", self.on_enter)
            slaves_list[int(key) - 1].bind("<Leave>", self.on_leave)

    def coord_to_tile_number(self, coord):
        tile_number = str(int(coord[0]) * 7 + int(coord[1]) + 1)
        return tile_number

    def get_score_column(self, player):
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

            # print("ColumnScore:", column_score)
        return (column_score)

    def get_score_row(self, player):
        row_score = 0
        for i in range(7):
            possible_score = ""
            for j in range(7):
                key = str(i) + str(j)

                if (self.tiles_dict[key] == player):
                    possible_score += self.tiles_dict[key]
                else:
                    possible_score += "_"

            # print(possible_score)

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

            # print("___RowScore:", row_score)
        return (row_score)

    def get_score(self):
        total_score_1 = 0
        row_score_1 = self.get_score_row("player1")
        column_score_1 = self.get_score_column("player1")
        total_score_1 += row_score_1 + column_score_1
        self.score_label_1.config(text=str(total_score_1))

        total_score_2 = 0
        row_score_2 = self.get_score_row("player2")
        column_score_2 = self.get_score_column("player2")
        total_score_2 += row_score_2 + column_score_2
        self.score_label_2.config(text=str(total_score_2))
