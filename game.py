from itertools import combinations
from Tkinter import Tk, Canvas, mainloop, Frame, Button, LEFT, Label, StringVar
from monster import Monster
import tkFont


" - MONSTER 4 - "

data = {'red': {'pattern': [(0,-1), (1,0), (1,2)],
                'start': [(1, 0), (1, 18), (2, 19), (3, 10), (4, 5),
                  (6, 5), (6, 7), (7, 18), (8, 14),
                  (10, 1), (10, 6), (10, 15), (12, 18),
                  (15, 1), (15, 16), (17, 5), (19, 0), (19, 3)]
                },
        'green': {'pattern': [(1,1), (-2,1), (0,1)],
                  'start': [(0, 13), (1, 5), (2, 7), (2, 10), (3, 7), (4, 2), (4, 12),
                    (8, 12), (9, 16),
                    (10, 10), (11, 10), (13, 16), (14, 18),
                    (15, 17), (15, 20),(17, 1), (18, 11), (20, 2)]
                  },
        'blue': {'pattern': [(-2,2), (0,-2), (1,0)],
                 'start': [(0, 5), (1, 13), (2, 4), (2, 14), (4, 13),
                   (6, 9),
                   (10, 14), (12, 17), (14, 16),
                   (16, 12), (19, 5), (19, 14), (19, 15)]
                 },
        'yellow': {'pattern': [(0,-2), (1,2), (1,-3)],
                   'start': [(0, 2), (1, 4), (4, 11),
                     (5, 18), (8, 9), (8, 20), (9, 5),
                     (12, 11), (14, 9),
                     (18, 2)]
                   },
        'pink': {'pattern': [(1,1), (1,0), (1,-1)],
                 'start': [(5, 14), (7, 10), (9, 15), (9, 19),
                   (10, 2), (11, 0), (11, 9), (11, 11), (14, 13),
                   (16, 0)]
                 },
        'brown': {'pattern': [(-1,1), (0,-2), (-1,-1)],
                  'start': [(5, 13), (6, 0),
                    (10, 16), (11, 1), (11, 2), (11, 17),
                    (15, 2), (16, 16), (18, 17), (20, 15)]
                  }
        }


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


alpha = [(0, 3, 'I'), (0, 12, 'U'), (0, 20, 'H'),
         (1, 0, 'E'), (1, 4, 'E'), (1, 6, 'F'),
         (2, 2, 'E'), (2, 9, 'F'), (2, 11, 'C'), (2, 13, 'F'), (2, 17, 'B'), (2, 19, 'L'),
         (3, 1, 'C'), (3, 3, 'N'), (3, 5, 'D'), (3, 8, 'N'), (3, 18, 'S'),
         (4, 10, 'I'), (4, 14, 'E'),
         (5, 1, 'N'), (5, 6, 'A'), (5, 11, 'R'), (5, 19, 'S'),
         (6, 4, 'I'), (6, 7, 'N'), (6, 9, 'U'), (6, 12, 'N'), (6, 17, 'IE'),
         (7, 0, 'N'), (7, 10, 'Z'), (7, 18, 'D'), (7, 10, 'A'),
         (8, 9, 'B'),
         (9, 6, 'S'), (9, 8, 'E'), (9, 15, 'S'),

         (11, 0, 'R'), (11, 3, 'U'), (11, 8, 'C'), (11, 14, 'E'),
         (12, 10, 'U'), (12, 13, 'L'), (12, 16, 'F'),
         (13, 2, 'F'), (13, 4, 'E'), (13, 11, 'E'),
         (14, 0, 'L'), (14, 5, 'I'), (14, 7, 'F'), (14, 16, 'I'),
         (15, 3, 'N'), (15, 10, 'V'),
         (16, 4, 'V'), (16, 6, 'E'), (16, 9, 'S'), (16, 12, 'I'), (16, 20, 'U'),
         (17, 1, 'S'), (17, 7, 'U'), (17, 13, 'E'), (17, 19, 'H'),
         (18, 4, 'R'), (18, 11, 'L'), (18, 17, 'N'),
         (19, 0, 'T'), (19, 2, 'N'), (19, 4, 'E'), (19, 16, 'F'), (19, 18, 'V'), (19, 20, 'W'),
         (20, 1, 'L'), (20, 5, 'U'), (20, 7, 'W'), (20, 10, 'H'), (20, 13, 'N'), (20, 19, 'E'),
        ]


class App:
    def __init__(self, tk_root, monsters_initdata, board_dim, board_signs):
        self.board = [[None for i in range(board_dim[0])] for j in range(board_dim[0])]
        self.jump_counter = 0
        self.meet_counter = 0
        self.data = monsters_initdata
        self.signs = board_signs

        self.collect = {'red': [], 'blue': [], 'green': [], 'yellow': [], 'pink': [], 'brown': []}
        self.init_gui(tk_root)
        self.monsters = self.init_monsters()
        self.draw_board()

    def init_gui(self, tk_root):
        # GUI
        frame = Frame(tk_root)

        canvas_width = 600
        canvas_height = 600

        self.canvas = Canvas(frame, width=canvas_width, height=canvas_height)
        self.canvas.pack()
        frame.pack()

        self.quit_button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit_button.pack(side=LEFT)
        self.jump_button = Button(frame, text="JUMP", command=self.jump)
        self.jump_button.pack(side=LEFT)

        self.text_counter = StringVar()
        self.text_counter.set('Round: {}'.format(self.jump_counter))
        self.label_counter = Label(frame, textvariable=self.text_counter, justify=LEFT)
        self.label_counter.pack()

        self.text_meet_counter = StringVar(self.meet_counter)
        self.label_meet_counter = Label(frame, textvariable=self.text_meet_counter, justify=LEFT)
        self.label_meet_counter.pack()

    def init_monsters(self):
        monsters = []
        for color, values in self.data.iteritems():
            for start_position in values['start']:
                monsters.append(Monster(self.board, color, start_position, values['pattern']))
        return monsters

    def draw_board(self):
        self.canvas.delete('all')

        canvas_width = 600
        canvas_height = 600

        self.board
        space = canvas_width / (len(self.board) + 2)
        font = tkFont.Font(family='Helvetica', size=12, weight='bold')
        for i in range(1, len(self.board) + 2):
            self.canvas.create_line(space, space * i, canvas_width - space, space * i, fill='#476042')
            self.canvas.create_line(space * i, space, space * i, canvas_width - space, fill='#476042')
        for i in range(len(self.board)):
            self.canvas.create_text(space * (i+1) + 12, 18, text=i, font=font)
            self.canvas.create_text(18, space * (i+1) + 12, text=i, font=font)

        font = tkFont.Font(family='Helvetica', size=20, weight='bold')
        for x, y, sign in self.signs:
            self.canvas.create_text(space * x + 39, space * y + 39, text=sign, font=font, fill='lightgrey')

        color_r = {'red': (1, 1), 'green': (1, 2), 'blue': (1, 3), 'yellow': (2, 1), 'pink': (2, 2), 'brown': (2, 3)}
        for monster in self.monsters:
            x1, y1 = monster.position
#            r = color_r.get(monster.color) * 2
            r = 2
            shift_x, shift_y = color_r.get(monster.color)
            # self.canvas.create_oval((1.5 + x1) * space - r, (1.5 + y1) * space - r,
            #                     (1.5 + x1) * space + r, (1.5 + y1) * space + r,
            #                     outline=monster.color, width=2)
            self.canvas.create_oval((1.5 + x1) * space - 14 - r + shift_y * 7, (1.5 + y1) * space - 14 - r + shift_x * 10,
                                (1.5 + x1) * space - 14 + r + shift_y * 7, (1.5 + y1) * space - 14 + r + shift_x * 10,
                                outline=monster.color, width=2)

    def jump(self):
        #self.canvas.delete('all')

        print
        print('ROUND {0}'.format(self.jump_counter + 1))
        print

        #positions = {}
        #self.board = [['  ' for i in range(21)] for j in range(21)]

        track_positions = {}
        for m in self.monsters:
            if m.rest:
                x, y = m.stay()
            else:
                x, y = m.jump()
                # check for signs on the board
                item = self.check_fields(m, self.signs)
                if item:
                    self.collect[m.color].append(item)
            # track position of all monsters in this round
            if (x, y) in track_positions:
                # already one monster on this location
                track_positions[(x, y)].append(m)
            else:
                track_positions[(x, y)] = [m]

        self.meet(track_positions)

        print(self.collect)
        print

        self.draw_board()
        self.jump_counter += 1

        print('Meet counter: {}'.format(self.meet_counter))
        self.text_counter.set(str(self.jump_counter))

    def check_fields(self, monster, fields):
        x, y = monster.position
        for x_f, y_f, value in fields:
            if x == x_f and y == y_f:
                monster.collection += value
                print '{} > {} -- {}'.format(monster.color, monster.collection, monster.positions)
                return value
        return ''

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
app = App(root, data, (21,21), [])
root.mainloop()
