#!/usr/bin/python
# Oscar Hendrick
# Wall project
# Defining the wall


import numpy as np


class MoonBoard:
    """
    This class returns a MoonBoard object that defines a board with LED
    LED positions

    0 - Holes for Holds
    1 - LED
    2 - Climbing Route

    name and climb_difficulty are strings
    climb_route is a numpy array of ones and twos of the same size as the board
    """

    def __init__(self, name, author, mastery, difficulty, route):
        self.name = name
        self.author = author
        self.mastery = mastery
        self.difficulty = difficulty
        self.route = route


        # Top mid, bot and kickboard are the sections of the board
        self.top = np.zeros((11, 21), dtype=int)
        self.top[0:11:2,0:21:2] = 1

        self.mid = np.zeros((12, 21), dtype=int)
        self.mid[1:12:2,0:21:2] = 1

        self.bot = np.zeros((13, 21), dtype=int)
        self.bot[0:13:2,0:21:2] = 1

        self.kickboard = np.zeros((4, 21), dtype=int)
        self.kickboard[1:3:2,0:21:2] = 1
        self.kickboard[3,1:21:2] = 1

        # This is the entire board
        self.board = np.concatenate((self.top, self.mid, self.bot, \
                                     self.kickboard))


    def createRoute(self, route):
        return self.board*route

a = MoonBoard("the climb", "Oscar", "meh", "v4", 1)
print(a.board)
