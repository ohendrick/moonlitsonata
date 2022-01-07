#!/usr/bin/python
# Oscar Hendrick
# Wall project
# Defining the wall


import numpy as np
import psycopg2


class MoonBoard:
    """
    This class returns a MoonBoard object
    that defines a board with LED positions

    0 - LED
    1 - Holes for Holds
    2 - Climbing Route

    name and climb_difficulty are strings
    """

    def __init__(self, name, author, rating, climb_difficulty):

        self.name = name
        self.author = author
        self.rating = rating
        self.climb_difficulty = climb_difficulty

        # Define each part of the moonboard
        # Top, mid, bot and kickboard are sections of the board
        self.top = np.ones((11, 21), dtype=int)
        self.top[0:11:2,0:21:2] = 0

        self.mid = np.ones((12, 21), dtype=int)
        self.mid[1:12:2,0:21:2] = 0

        self.bot = np.ones((13, 21), dtype=int)
        self.bot[0:13:2,0:21:2] = 0

        self.kickboard = np.ones((4, 21), dtype=int)
        self.kickboard[1:3:2,0:21:2] = 0
        self.kickboard[3,1:21:2] = 0

        # This is the entire board
        self.board = np.concatenate((self.top, self.mid, self.bot, \
                                     self.kickboard))

        ''' print(a.board.shape) 40x21 or 840'''



#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database mydb''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()


a = MoonBoard("the climb", "Oscar", "4", "v1")
print(a.board.flatten().shape)






''' print(a.board.shape) 40x21 or 840
[[1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0]]
'''

