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
    tiles_dic = {}

    def __init__(self, root, tic=0):
        self.root = root
        self.tic = tic
        self.root.attributes("-topmost", True)  # put the root to foreground
        self.root.geometry('+1000+0')  # sets the default window position
        for i in range(7):
            for j in range(7):
                self.a = "l" + str(i + 1) + str(j + 1)
                self.a = tk.Label(self.root, text=self.a, width=5, height=5, bg = "light cyan")
                self.a.bind("<Button-1>", self.color_change)
                self.a.grid(row=i, column=j)
        self.tic_label = tk.Label(self.root, textvariable=self.tic, width=5, height=5, bg = "cyan")
        self.tic_label.grid(row = 1, column = 8)
        self.root.mainloop

    def read_tic(self):
        return self.tic

    def inc_tic(self, tic):
        a = self.read_tic()
        self.tic = (a + 1)

    def color_change(self, event):
        print("something", event.widget)
        self.inc_tic(self.tic)
        print("Tic", self.tic)
        if (self.tic % 2 == 0):
            event.widget.config(bg="lightgreen")
        else:
            event.widget.config(bg="tomato")

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
