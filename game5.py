from itertools import combinations
from Tkinter import Tk, Canvas, mainloop, Frame, Button, LEFT, Label, StringVar
from monster import Monster
import tkFont


" - MONSTER 5 - "

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


red_patterns = [(0,-1), (1,0), (1,2)]
green_patterns = [(1,1), (-2,1), (0,1)]
blue_patterns = [(-2,2), (0,-2), (1,0)]
yellow_patterns = [(0,-2), (1,2), (1,-3)]
pink_patterns = [(1,1), (1,0), (1,-1)]
brown_patterns = [(-1,1), (0,-2), (-1,-1)]

start_positions_reds = [(1, 0), (1, 18), (2, 19), (3, 10), (4, 5),
                        (6, 5), (6, 7), (7, 18), (8, 14),
                        (10, 1), (10, 6), (10, 15), (12, 18),
                        (15, 1), (15, 16), (17, 5), (19, 0), (19, 3)]

start_positions_greens = [(0, 13), (1, 5), (2, 7), (2, 10), (3, 7), (4, 2), (4, 12),
                          (8, 12), (9, 16),
                          (10, 10), (11, 10), (13, 16), (14, 18), (15, 17), (15, 20),
                          (17, 1), (18, 11), (20, 2)]

start_positions_blues = [(0, 5), (1, 13), (2, 4), (2, 14), (4, 13),
                         (6, 9),
                         (10, 14), (12, 17), (14, 16),
                         (16, 12), (19, 5), (19, 14), (19, 15)]

start_positions_yellows = [(0, 2), (1, 4), (4, 11),
                           (5, 18), (8, 9), (8, 20), (9, 5),
                           (12, 11), (14, 9),
                           (18, 2)]

start_positions_pinks = [(5, 14), (7, 10), (9, 15), (9, 19),
                         (10, 2), (11, 0), (11, 9), (11, 11), (14, 13),
                         (16, 0)]

start_positions_browns = [(5, 13), (6, 0),
                          (10, 16), (11, 1), (11, 2), (11, 17),
                          (15, 2), (16, 16), (18, 17), (20, 15)]


numbers = [(0, 11, '='),
         (1, 6, '9'), (1, 16, '1'), (1, 19, '8'),
         (2, 0, '6'),
         (3, 5, '-'), (3, 8, '6'), (3, 12, '='), (3, 17, '5'),
         (4, 15, '3'),
         (5, 2, '-'), (5, 5, '3'), (5, 7, '5'), (5, 9, '='),
         (6, 8, '-'), (6, 11, '7'), (6, 15, '8'),
         (7, 2, '2'), (7, 12, '4'), (7, 20, '2'),
         (8, 0, '1'), (8, 4, '7'), (8, 15, '6'),
         (9, 1, '-'), (9, 10, '6'),
         (10, 9, '5'), (10, 11, '2'),
         (11, 7, '+'), (11, 18, '+'),
         (12, 8, '='), (12, 13, '9'),
         (13, 4, '4'), (13, 9, '8'), (13, 19, '-'),
         (14, 6, '2'), (14, 15, '1'),
         (15, 5, '3'), (15, 9, '9'), (15, 13, '-'), (15, 18, '+'),
         (16, 2, '5'), (16, 11, '+'),
         (17, 4, '4'), (17, 6, '-'), (17, 8, '1'), (17, 20, '+'),
         (18, 6, '='), (18, 12, '+'), (18, 18, '9'),
         (19, 7, '2'), (19, 11, '7'),
         (20, 0, '4'), (20, 9, '2'), (20, 17, '1'), (20, 19, '=')
        ]


class App:
    def __init__(self, master):
        self.board = [[None for i in range(21)] for j in range(21)]
        self.jump_counter = 0
        self.meet_counter = 0
        self.child_counter = 0

        self.collect = {'red': [], 'blue': [], 'green': [], 'yellow': [], 'pink': [], 'brown': []}

        # GUI
        frame = Frame(master)

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

        self.text_child_counter = StringVar(self.child_counter)
        self.label_child_counter = Label(frame, textvariable=self.text_child_counter, justify=LEFT)
        self.label_child_counter.pack()

        self.monsters = self.init_monsters()
        self.draw_board()

    def init_monsters(self):
        monsters = []
        for color, values in data.iteritems():
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
        for x, y, sign in numbers:
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
        self.canvas.delete('all')

        print
        print('ROUND {0}'.format(self.jump_counter + 1))
        print

        positions = {}
        self.board = [['  ' for i in range(21)] for j in range(21)]

        track_positions = {}
        for m in self.monsters:
            if m.rest:
                x, y = m.stay()
            else:
                x, y = m.jump()
                # check for numbers and operators on the board
                item = self.check_fields(m, numbers)
                if item:
                    self.collect[m.color].append(item)
            # track position of all monsters in this round
            if (x, y) in track_positions:
                # already one monster on this location
                track_positions[(x, y)].append(m)
            else:
                track_positions[(x, y)] = [m]

        for position, monsters in track_positions.iteritems():
            # meeting happened
            if len(monsters) > 1:
                if not monsters[0].rest:
                    print "Meet @ {}: {}".format(position, [mon.color for mon in monsters])
                    self.meet_counter += 1

                    # check if fuck
                    self.fuck(monsters[0], monsters[1])
                else:
                    print "Rest @ {}: {}".format(position, [mon.color for mon in monsters])

                for mon in monsters:
                    mon.rest = not mon.rest

        print(self.collect)
        print

        self.draw_board()
        self.jump_counter += 1
        self.text_counter.set(str(self.jump_counter))
        self.text_meet_counter.set(str(self.meet_counter))
        self.text_child_counter.set(str(self.child_counter))

    def check_fields(self, monster, fields):
        x, y = monster.position
        for x_f, y_f, value in fields:
            if x == x_f and y == y_f:
                monster.collection += value
                print '{} > {} -- {}'.format(monster.color, monster.collection, monster.positions)
                return value
        return ''

    def fuck(self, m1, m2):
        if m1.rest or m2.rest:
            return

        baby = None
        if (m1.color == 'red' and m2.color == 'green') or (m1.color == 'green' and m2.color == 'red'):
            baby = Monster(self.board, 'blue', m1.position, blue_patterns)
            position = baby.jump()
            self.monsters.append(baby)
            print("New Monster: blue @ {}".format(baby.position))
            self.child_counter += 1
        elif (m1.color == 'green' and m2.color == 'blue') or (m1.color == 'blue' and m2.color == 'green'):
            baby = Monster(self.board, 'yellow', m1.position, yellow_patterns)
            position = baby.jump()
            self.monsters.append(baby)
            print("New Monster: yellow @ {}".format(baby.position))
            self.child_counter += 1
        elif (m1.color == 'blue' and m2.color == 'yellow') or (m1.color == 'yellow' and m2.color == 'blue'):
            baby = Monster(self.board, 'pink', m1.position, pink_patterns)
            position = baby.jump()
            self.monsters.append(baby)
            print("New Monster: pink @ {}".format(baby.position))
            self.child_counter += 1
        elif (m1.color == 'yellow' and m2.color == 'pink') or (m1.color == 'pink' and m2.color == 'yellow'):
            baby = Monster(self.board, 'brown', m1.position, brown_patterns)
            position = baby.jump()
            self.monsters.append(baby)
            print("New Monster: brown @ {}".format(baby.position))
            self.child_counter += 1
        elif (m1.color == 'pink' and m2.color == 'brown') or (m1.color == 'brown' and m2.color == 'pink'):
            baby = Monster(self.board, 'red', m1.position, red_patterns)
            position = baby.jump()
            self.monsters.append(baby)
            print("New Monster: red @ {}".format(baby.position))
            self.child_counter += 1
        elif (m1.color == 'brown' and m2.color == 'red') or (m1.color == 'red' and m2.color == 'brown'):
            baby = Monster(self.board, 'green', m1.position, green_patterns)
            position = baby.jump()
            self.monsters.append(baby)
            print("New Monster: green @ {}".format(baby.position))
            self.child_counter += 1

        if baby:
            # check for numbers and operators on the board
            item = self.check_fields(baby, numbers)
            if item:
                self.collect[baby.color].append(item)


#create view
root = Tk()
app = App(root)
root.mainloop()
