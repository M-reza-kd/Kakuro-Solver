import math
import sys
import random
from datetime import datetime
from KRG import KakuroRandomGame
from KUI import KakuroUI
from tkinter import Tk
import time

random.seed(time.time())
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


def BT_constraint(variables, target_sum, assignment):
    assigned_values = [assignment[var] for var in variables if var in assignment]
    if len(assigned_values) != len(set(assigned_values)):
        return False

    if sum(assigned_values) <= target_sum:
        return False

    return True


if __name__ == '__main__':
    game = KakuroRandomGame()
    root = Tk()
    ui = KakuroUI(root, game)
    print('\n\n*******\n\n', game.data_fills[0], '\n\n****\n\n')
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()
    ui.solve()
