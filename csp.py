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


if __name__ == '__main__':
    game = KakuroRandomGame()
    root = Tk()
    ui = KakuroUI(root, game)
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()
    ui.solve()
