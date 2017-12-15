"""Docstring: A very short sentence explaining the function. < 79 characters. 

Additional information if required and more infos. Complete sentences please.
"""

import random
import pah_tum_controller
import sys
#from pah_tum_controller_class import PahTum
from pah_tum_controller_class2 import PahTum
import tkinter as tk

__author__ = "123456: John Cleese, 654321: Terry Gilliam"  # put your data here
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "your email address" 

def menue():
    """a procedure for printing a menue we assume"""
    
    print("...Welcome to the Menue................")
    print(".......................................")
    print("...Press 1 to start Pah Tum TUI Mode...")
    print("...Press 2 to start Pah Tum GUI Mode...")
    print("...Press 3 to see the manual...........")
    print("...Press 4 for help....................")
    print("...Press 5 to Exit.....................")
    print(".......................................")
    print(".......................................")


def main():
    # delete at end of construction work
    root = tk.Tk()
    obj = PahTum(root)
    root.mainloop()
    # delete part above - Wear your hard hat
    while(True):
        menue()
        inp = input()
        if (inp == "1"):
            pah_tum_controller.controller()
        if (inp == "2"):
            root = tk.Tk()
            obj = PahTum(root)
            root.mainloop()
        if (inp == "5"):
            pah_tum_controller.autism()
            sys.exit()

if __name__ == '__main__':
    main()

