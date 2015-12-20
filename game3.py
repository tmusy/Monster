from Tkinter import Tk
from game import App


" - MONSTER 3 - "

red_patterns = [(-1,-1), (2,0), (0,-1)]
green_patterns = [(1,-1), (-1,-1), (-2,2)]
blue_patterns = [(2,-3), (0,3), (1,0)]
yellow_patterns = [(1,-1), (0,3), (-2,0)]
pink_patterns = [(-1,-1), (-2,1), (0,-2)]
brown_patterns = [(0,2), (2,0), (0,1)]

start_positions_reds = [(0, 18), (0, 19), (3, 6),
                        (5, 10), (8, 13), (9, 5),
                        (10, 19), (12, 6),
                        (16, 19), (17, 14), (20, 11), (20, 15), (20, 17)]

start_positions_greens = [(5, 9), (6, 6), (8, 3),
                          (10, 14), (11, 19), (12, 1), (12, 19), (14, 11),
                          (15, 16), (15, 19), (19, 13)]

start_positions_blues = [(0, 2), (1, 15), (2, 7), (3, 16), (4, 16), (4, 19),
                         (7, 7), (8, 18), (9, 2),
                         (10, 17), (12, 14), (13, 8),
                         (16, 8), (17, 5), (19, 17)]

start_positions_yellows = [(0, 7),
                           (5, 0), (8, 14), (9, 3),
                           (10, 11), (11, 15), (12, 8), (14, 3), (14, 18),
                           (15, 11), (15, 15), (15, 18), (20, 2)]

start_positions_pinks = [(0, 1), (2, 8), (3, 9), (4, 13), (4, 17),
                         (7, 14), (9, 20),
                         (11, 1), (11, 17), (13, 5), (14, 10),
                         (15, 5), (16, 5), (16, 14), (18, 2), (19, 10)]

start_positions_browns = [(8, 0),
                          (10, 8), (12, 18), (13, 10),
                          (15, 1), (15, 6), (18, 6)]

data = {'red': {'pattern': red_patterns,
                'start': start_positions_reds
                },
        'green': {'pattern': green_patterns,
                  'start': start_positions_greens
                  },
        'blue': {'pattern': blue_patterns,
                 'start': start_positions_blues
                 },
        'yellow': {'pattern': yellow_patterns,
                   'start': start_positions_yellows
                   },
        'pink': {'pattern': pink_patterns,
                 'start': start_positions_pinks
                 },
        'brown': {'pattern': brown_patterns,
                  'start': start_positions_browns
                  }
        }


alpha = [(0, 3, 'I'), (0, 12, 'U'), (0, 20, 'H'),
         (1, 0, 'E'), (1, 4, 'E'), (1, 6, 'F'),
         (2, 2, 'E'), (2, 9, 'F'), (2, 11, 'C'), (2, 13, 'F'), (2, 17, 'B'), (2, 19, 'L'),
         (3, 1, 'C'), (3, 3, 'N'), (3, 5, 'D'), (3, 8, 'N'), (3, 18, 'S'),
         (4, 10, 'I'), (4, 14, 'E'),
         (5, 1, 'N'), (5, 6, 'A'), (5, 11, 'R'), (5, 19, 'S'),
         (6, 4, 'I'), (6, 7, 'N'), (6, 9, 'U'), (6, 12, 'N'), (6, 17, 'E'),
         (7, 0, 'N'), (7, 10, 'Z'), (7, 18, 'D'), (7, 20, 'A'),
         (8, 9, 'B'),
         (9, 6, 'S'), (9, 8, 'E'), (9, 15, 'S'),

         (11, 0, 'R'), (11, 3, 'U'), (11, 8, 'C'), (11, 14, 'E'),
         (12, 10, 'U'), (12, 13, 'L'), (12, 16, 'F'),
         (13, 2, 'F'), (13, 4, 'E'), (13, 11, 'E'),
         (14, 0, 'L'), (14, 5, 'I'), (14, 7, 'F'), (14, 16, 'I'),
         (15, 3, 'N'), (15, 10, 'V'),
         (16, 4, 'V'), (16, 6, 'E'), (16, 9, 'S'), (16, 12, 'I'), (16, 20, 'U'),
         (17, 1, 'S'), (17, 7, 'U'), (17, 13, 'E'), (17, 19, 'H'),
         (18, 3, 'R'), (18, 11, 'L'), (18, 17, 'N'),
         (19, 0, 'T'), (19, 2, 'N'), (19, 4, 'E'), (19, 16, 'F'), (19, 18, 'V'), (19, 20, 'W'),
         (20, 1, 'L'), (20, 5, 'U'), (20, 7, 'W'), (20, 10, 'H'), (20, 13, 'N'), (20, 19, 'E'),
        ]


class Game3(App):
    def __init__(self, tk_root, monsters_initdata, board_dim, board_signs):
        super(Game3, self).__init__(tk_root, monsters_initdata, board_dim, board_signs)


#create view
root = Tk()
app = Game3(root, data, (21,21), alpha)
root.mainloop()
