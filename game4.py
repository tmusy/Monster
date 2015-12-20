from Tkinter import Tk
from game import App


" - MONSTER 4 - "

red_patterns = [(-2,-2), (0,3), (-1,-1)]
green_patterns = [(-1,2), (2,0), (0,1)]
blue_patterns = [(0,1), (-2,-3), (-1,0)]
yellow_patterns = [(-1,2), (2,0), (1,-2)]
pink_patterns = [(-1,-2), (1,-1), (2,0)]
brown_patterns = [(-2,-2), (2,0), (-3,3)]

start_positions_reds = [(4, 14),
                        (5, 9),
                        (13, 14), (14, 3), (14, 14),
                        (15, 13), (19, 5), (19, 8)]

start_positions_greens = [(1, 8), (3, 2), (3, 20),
                          (6, 15), (8, 15),
                          (11, 5), (11, 18), (11, 20), (14, 2), (14, 15),
                          (15, 6), (15, 16), (15, 20), (20, 19), (20, 20)]

start_positions_blues = [(0, 2), (0, 18), (2, 13), (4, 0), (4, 10),
                         (5, 0),
                         (12, 9), (12, 10),
                         (17, 20), (18, 0), (19, 18)]

start_positions_yellows = [(0, 16), (2, 3), (2, 7), (2, 15),
                           (5, 17), (6, 3), (6, 13), (8, 5), (8, 17),
                           (11, 4), (12, 5), (12, 14), (14, 7),
                           (17, 5), (17, 6), (17, 13), (18, 6), (18, 17), (20, 6), (20, 11), (20, 14)]

start_positions_pinks = [(4, 3), (4, 12), (4, 16), (4, 18),
                         (5, 20), (6, 2), (6, 14), (8, 3), (8, 20), (9, 18),
                         (10, 0), (10, 18), (11, 12), (13, 4),
                         (16, 19), (17, 16), (20, 5)]

start_positions_browns = [(0, 1), (0, 9), (0, 14), (0, 20), (1, 4), (3, 4), (4, 7),
                          (5, 2), (8, 8), (8, 10),
                          (10, 6), (11, 13), (13, 6), (14, 6), (14, 11),
                          (17, 1), (20, 8), (20, 10)]


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


class Game4(App):
    def __init__(self, tk_root, monsters_initdata, board_dim, board_signs):
        super(Game4, self).__init__(tk_root, monsters_initdata, board_dim, board_signs)

    def meet(self, track_positions):
        for position, monsters in track_positions.iteritems():
            # meeting happened
            if len(monsters) > 1:
                if not monsters[0].rest:
                    print "Meet @ {}: {}".format(position, [mon.color for mon in monsters])
                    self.meet_counter += 1

                    # check if fuck
                    #self.fuck(monsters[0], monsters[1])
                else:
                    print "Rest @ {}: {}".format(position, [mon.color for mon in monsters])

                for mon in monsters:
                    mon.rest = not mon.rest

#create view
root = Tk()
app = Game4(root, data, (21,21), [])
root.mainloop()
