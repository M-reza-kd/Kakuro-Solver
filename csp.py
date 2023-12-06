import math
import sys
import random
from datetime import datetime
from KRG import KakuroRandomGame
from KUI import KakuroUI, load_another
from tkinter import Tk
import time

random.seed(time.time())
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


if __name__ == '__main__':
    load_another()
