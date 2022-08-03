"""
creating the GUI for the sudoku

display
-------------
9x9 grid                    ]
2 solid horizontal lines    ]   layout
2 solid vertical lines      ]

premade numbers displaying at the center of each box


"""

from tkinter import *
from grid import is_valid_move, solve
import time


#window settings
game_window = Tk()
game_window.geometry("750x750")
game_window.title("Sudoku")
game_window.config (background = "black")
grid = [[0, 0, 6, 1, 5, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [7, 0, 0, 0, 8, 4, 0, 0, 0],
        [3, 0, 0, 9, 0, 8, 5, 6, 1],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 0, 8],
        [0, 0, 7, 0, 0, 0, 6, 0, 3],
        [5, 3, 0, 6, 0, 0, 9, 8, 4],
        [0, 4, 0, 0, 0, 1, 0, 0, 7]]

frame = Frame(game_window)
frame.pack()


game_window.mainloop()

