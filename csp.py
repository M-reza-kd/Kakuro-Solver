import random
import sys

from KCG import KakuroCustomGame
from KUI import KakuroUI, load_another, load_for_100_time
from tkinter import Tk
import time

random.seed(time.time())
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Wrong number of arguments! Enter mode (custom or random) to run in as argument.\n"
              "Example Usage: python kakuro.py random to run random puzzles\n"
              "Going forward with random...\n")
        load_another()
    elif sys.argv[1] == 'random':
        load_another()
    elif sys.argv[1] == 'custom':
        game = KakuroCustomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()

    elif sys.argv[1] == 'random_average':
        print("Random")
        load_for_100_time()
    else:
        print("Wrong number or format of arguments! Enter mode (custom or random) to run in as argument.\n"
              "Example Usage: python kakuro.py random to run random puzzles\n"
              "Going forward with random...\n")
        load_another()
