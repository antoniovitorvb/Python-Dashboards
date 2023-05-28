import numpy as np
import os
import random as rd

class Tabuleiro:
    def __init__(self):
        self.reset()

    def print_tab(self):
        print("")
        print(" " + self.tab[0][0] + " | " + self.tab[0][1] + " | " + self.tab[0][2])
        print("-----------")
        print(" " + self.tab[1][0] + " | " + self.tab[1][1] + " | " + self.tab[1][2])
        print("-----------")
        print(" " + self.tab[2][0] + " | " + self.tab[2][1] + " | " + self.tab[2][2])

    def reset(self):
        self.tab = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "],]

    def player_move(self):
        pass

    def make_move(self):
        pass

    def check_result(self):
        pass
    
Tabuleiro().print_tab()