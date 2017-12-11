"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import random
import tkinter as tk

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


class PahTum():
    tiles_dict = {}

    def __init__(self, root, tic=0):
        self.root = root
        self.tic = tic
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.geometry('+1000+0')  # sets the default window position
        self.root.title("Pah Tuuuum")
        for i in range(7):
            for j in range(7):
                # every even i should get a border
                self.a = "l" + str(i + 1) + str(j + 1)
                self.a = tk.Label(self.root, text=self.a, width=5, height=5, bg="light cyan", borderwidth=0.1, relief="solid")
                self.a.bind("<Button-1>", self.color_change)
                self.a.grid(row=i, column=j)
        self.tic_label = tk.Label(self.root, text="Tic: ", width=5, height=5, bg="cyan", borderwidth=1, relief="solid")
        self.tic_label.grid(row=1, column=8)
        print(self.root.grid_slaves())
        self.root.mainloop

        self.tiles_dict_constructor()
        self.tiles_blocker()
        print(self.tiles_dict)

    def read_tic(self):
        return self.tic

    def inc_tic(self, tic):
        a = self.read_tic()
        self.tic = (a + 1)

    def color_change(self, event):
        print("something", event.widget)
        
        print("Tic", self.tic)

        self.label_coordinator(event.widget)

        if (self.tic % 2 == 0):            
            if (self.tiles_dict[self.label_coordinator(event.widget)] == ""):
                self.tiles_dict[self.label_coordinator(event.widget)] = "player1"            
                event.widget.config(bg="lightgreen")
                tic_str = "Tic: " + str(self.read_tic())
                self.tic_label.config(text=tic_str)
                self.inc_tic(self.tic)
                print(self.tiles_dict)  
            
        else:
            if (self.tiles_dict[self.label_coordinator(event.widget)] == ""):
                self.tiles_dict[self.label_coordinator(event.widget)] = "player2"            
                event.widget.config(bg="tomato")
                tic_str = "Tic: " + str(self.read_tic())
                self.tic_label.config(text=tic_str)
                self.inc_tic(self.tic)
                print(self.tiles_dict)         

    def autism(self):
        """Autism - to be renamed

        Here we should either open n = NN>0 Windows or more in sequence or open n windows all together
        We have to load special images for each a = root object. Like buy viagra, sexy girls in your neihghbourhood
        lets find out bilals address to get him spooked a little bit.
        Sexy girls in (Bilals Area) are looking for fun
        Sexy Boooooooiz in Bilals Area are looking for hook up
        Buy our Kitchen Aid for 299

        """
        for i in range(10):
            a = str(i)
            a = tk.Tk()
            a.attributes("-topmost", True)
            a.mainloop()

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
    
    def tiles_blocker(self):
        tiles_number_to_block = [5, 7, 9, 11, 13]
        n_random = [0, 1, 2, 3, 4, 5, 6]
        m_random = [0, 1, 2, 3, 4, 5, 6]
        tiles_number_to_block = random.choice(tiles_number_to_block)
        
        for i in range(tiles_number_to_block):
            n = random.choice(n_random)
            m = random.choice(m_random)
            key = str(n) + str(m)
            self.tiles_dict[key] = "blocked"

        
