from Tkinter import Tk
from game import App

" - MONSTER 2 - "

red_patterns = [(-1,-1), (2,-2), (-2,0)]
green_patterns = [(1,2), (1,-2), (1,0)]
blue_patterns = [(1,2), (-2,-1), (-1,1)]
yellow_patterns = [(0,-2), (1,2), (1,1)]
pink_patterns = [(-1,1), (-1,-2), (-1,1)]
brown_patterns = [(1,-1), (1,0), (1,-1)]

start_positions_reds = [(1, 12),
                        (5, 1), (6, 3), (7, 13), (8, 10), (8, 13), (9, 2), (9, 15),
                        (13, 10),
                        (15, 16), (17, 15), (18, 14), (19, 1)]

start_positions_greens = [(1, 7), (1, 10), (3, 2), (3, 11),
                          (5, 9),
                          (10, 15), (11, 7), (11, 15),
                          (16, 5), (18, 7)]

start_positions_blues = [(0, 19),
                         (5, 8), (6, 0), (6, 20),
                         (11, 5), (14, 11),
                         (15, 10), (17, 3), (17, 11), (19, 10), (20, 3), (20, 18)]

start_positions_yellows = [(1, 17), (2, 7), (2, 11), (2, 15), (4, 16),
                           (6, 7), (6, 9), (7, 11), (8, 15),
                           (10, 4), (11, 3), (11, 12), (12, 13),
                           (19, 6), (20, 13), (20, 14)]

start_positions_pinks = [(1, 16), (2, 8), (2, 10), (3, 5),
                         (9, 7),
                         (11, 11), (13, 2),
                         (16, 10), (17, 5), (17, 10), (17, 16)]

start_positions_browns = [(1, 18), (2, 1), (2, 9), (2, 14), (2, 18), (3, 10), (3, 13), (4, 14), (4, 18),
                          (5, 19), (8, 14), (9, 1), (9, 8), (9, 11), (9, 17), (9, 19),
                          (16, 0), (17, 14), (18, 1), (18, 9), (18, 19), (19, 14), (19, 16), (19, 19)]


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


class Game2(App):
    def __init__(self, tk_root, monsters_initdata, board_dim, board_signs):
        super(Game2, self).__init__(tk_root, monsters_initdata, board_dim, board_signs)


#create view
root = Tk()
app = Game2(root, data, (21,21), [])
root.mainloop()
