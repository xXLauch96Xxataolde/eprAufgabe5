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


def read_tic(tic):
    return tic


def inc_tic():
    a = read_tic()
    return(a + 1)
    

def color_change(event):
    print("something", event.widget)   
    event.widget.config(bg="lightgreen")

    
def autism():
    """Autism - to be renamed
    
    Here we should either open n = NN>0 Windows or more in sequence or open n windows all together
    We have to load special images for each a = root object. Like buy viagra, sexy girls in your neihghbourhood
    lets find out bilals address to get him spooked a little bit.
    Sexy girls in (Bilals Area) are looking for fun
    Sexy Boooooooiz in Bilals Area are looking for bareback anal
    Buy our Kitchen Aid for 299
    
    """
    for i in range(10):
        a = str(i)
        a = tk.Tk()
        a.attributes("-topmost", True)
        a.mainloop()


def controller():
    root = tk.Tk()
    root.attributes("-topmost", True)  # put the root to foreground
    for i in range(7):
        for j in range(7):
            a = "l" + str(i + 1) + str(j + 1)
            a = tk.Label(root, text=a, width=5, height=5)
            a.bind("<Button-1>", color_change)
            a.grid(row=i, column=j)
        
    print("do some shit")
    33
    
    root.mainloop()
