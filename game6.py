# -*- coding: utf-8 -*-
from Tkinter import Tk, Canvas, Frame, Button, LEFT, Label, StringVar
from monster import Monster
import tkFont


data = {'red': {'pattern': [(-1,1), (1,1), (-2,0)],
                'start': [(3, 7, False),
                         (8, 19, False),
                         (10, 20, True), (12, 1, True), (13, 5, False), (14, 11, False),
                         (17, 20, False), (18, 11, True), (19, 0, False)]
                },
        'green': {'pattern': [(1,1), (-2,0), (0,-2)],
                  'start': [(0, 14, True), (1, 1, True), (1, 7, True), (2, 12, False), (3, 9, True), (3, 15, True), (4, 12, True),
                           (6, 7, True), (6, 20, True), (7, 3, True), (7, 20, True), (8, 2, True), (9, 2, False),
                           (11, 8, False), (11, 12, False), (12, 15, False), (15, 17, True),
                           (16, 13, True), (17, 13, False), (18, 15, True)]
                  },
        'blue': {'pattern': [(-2,-2), (2,1), (1,-1)],
                 'start': [(3, 6, False), (3, 8, False),
                          (9, 4, True), (9, 10, True),
                          (15, 18, False), (15, 20, True), (16, 19, False)]
                 },
        'yellow': {'pattern': [(-3,1), (2,0), (-2,-1)],
                   'start': [(3, 20, False), (4, 7, False),
                            (7, 18, False), (9, 5, True),
                            (10, 16, False), (10, 19, True), (11, 0, True)]
                   },
        'pink': {'pattern': [(-2,1), (2,-3), (1,3)],
                 'start': [(1, 2, False), (4, 19, True),
                          (7, 15, False), (8, 9, False),
                          (10, 5, True), (13, 20, False),
                          (15, 16, False)]
                 },
        'brown': {'pattern': [(0,-2), (3,0), (0,2)],
                  'start': [(0, 19, True), (4, 20, True),
                           (7, 4, False), (7, 6, True),
                           (11, 11, False), (12, 4, False), (13, 10, True), (14, 18, True),
                           (19, 6, False), (19, 9, False)]
                  }
        }

red_patterns = [(-1,1), (1,1), (-2,0)]
green_patterns = [(1,1), (-2,0), (0,-2)]
blue_patterns = [(-2,-2), (2,1), (1,-1)]
yellow_patterns = [(-3,1), (2,0), (-2,-1)]
pink_patterns = [(-2,1), (2,-3), (1,3)]
brown_patterns = [(0,-2), (3,0), (0,2)]


dna = [(0, 1, 'U'), (0, 5, 'G'), (0, 15, 'G'),
         (1, 10, 'U'), (1, 13, 'A'),
         (2, 3, 'A'), (2, 7, 'C'), (2, 19, 'C'),
         (3, 16, 'A'),
         (4, 0, 'C'), (4, 1, 'A'), (4, 8, 'A'), (4, 14, 'C'),
         (5, 2, 'G'), (5, 5, 'U'), (5, 11, 'G'),
         (6, 3, 'C'), (6, 11, 'A'), (6, 16, 'U'), (6, 18, 'C'),
         (7, 9, 'C'),
         (8, 5, 'G'), (8, 10, 'U'), (8, 20, 'G'),
         (9, 1, 'G'), (9, 15, 'G'), (9, 18, 'A'),
         (10, 14, 'U'),
         (11, 1, 'A'), (11, 3, 'C'), (11, 19, 'U'),
         (12, 5, 'A'), (12, 7, 'C'), (12, 10, 'C'), (12, 16, 'C'),
         (13, 0, 'U'), (13, 12, 'G'),
         (14, 9, 'C'), (14, 15, 'A'), (14, 19, 'G'),
         (15, 13, 'U'),
         (16, 4, 'C'), (16, 7, 'U'), (16, 20, 'C'),
         (17, 15, 'G'), (17, 17, 'A'),
         (18, 0, 'A'), (18, 4, 'U'), (18, 9, 'G'),
         (19, 4, 'A'), (19, 12, 'A'), (19, 19, 'G'),
         (20, 2, 'G'), (20, 8, 'A'), (20, 14, 'C'), (20, 20, 'U')
        ]


class App:
    def __init__(self, master):
        self.board = [[None for i in range(21)] for j in range(21)]
        self.jump_counter = 0
        self.meet_counter = 0
        self.child_counter = 0

        self.collection = {'red': [], 'blue': [], 'green': [], 'yellow': [], 'pink': [], 'brown': []}

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
            for x, y, sick in values['start']:
                monsters.append(Monster(self.board, color, (x, y), values['pattern'], sick=sick))
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
        for x, y, sign in dna:
            self.canvas.create_text(space * x + 39, space * y + 39, text=sign, font=font, fill='lightgrey')

        color_r = {'red': (1, 1), 'green': (1, 2), 'blue': (1, 3), 'yellow': (2, 1), 'pink': (2, 2), 'brown': (2, 3)}
        for monster in self.monsters:
            x1, y1 = monster.position
#            r = color_r.get(monster.color) * 2
            r = 2
            shift_x, shift_y = color_r.get(monster.color)

            # self.canvas.create_oval((1.5 + x1) * space - 14 - r + shift_y * 7, (1.5 + y1) * space - 14 - r + shift_x * 10,
            #                     (1.5 + x1) * space - 14 + r + shift_y * 7, (1.5 + y1) * space - 14 + r + shift_x * 10,
            #                     outline=monster.color, width=2)
            font_life = tkFont.Font(family='Helvetica', size=9, weight="bold")
            sign = str(monster.life)
            if monster.sick:
                sign += '†'
            self.canvas.create_text((1.5 + x1) * space - 16 + r + shift_y * 7, (1.5 + y1) * space - 16 + r + shift_x * 10, text=sign, font=font_life, fill=monster.color)

    def jump(self):
        self.canvas.delete('all')

        print
        print('ROUND {0}'.format(self.jump_counter + 1))
        print

        positions = {}
        self.board = [['  ' for i in range(21)] for j in range(21)]

        track_positions = {}
        for m in self.monsters:
            if m.life > 0:
                x, y = m.jump()
                # check for dna on the board
                item = self.check_fields(m, dna)
                if item:
                    self.collection[m.color].append(item)
                # track position of all monsters in this round
                if (x, y) in track_positions:
                    # already one monster on this location
                    track_positions[(x, y)].append(m)
                else:
                    track_positions[(x, y)] = [m]

                if m.sick:
                    m.life -= 1
            else:
                self.monsters.remove(m)

        for position, monsters in track_positions.iteritems():
            # meeting happened
            if len(monsters) > 1:
                print "Meet @ {}: {}".format(position, [mon.color for mon in monsters])

                self.meet_counter += 1

                sick_monsters = [mon.sick for mon in monsters]
                if True in sick_monsters:
                    for mon in monsters:
                        print '{} is sick: {}. Has been infected!'.format(mon.color, mon.sick)
                        mon.sick = True

        print(self.collection)
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
                fields.remove((x_f, y_f, value))
                return value
        return ''


#create view
root = Tk()
app = App(root)
root.mainloop()
