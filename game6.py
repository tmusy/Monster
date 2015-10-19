from itertools import combinations
from Tkinter import Tk, Canvas, mainloop, Frame, Button, LEFT, Label, StringVar
from monster import Monster


" - MONSTER 1 - "

red_patterns = [(1,-2), (1,2), (1,0)]
green_patterns = [(1,-2), (1,1), (1,-2)]
blue_patterns = [(-1,2), (3,-1), (-1,1)]
yellow_patterns = [(-1,-1), (-1,2), (-1,-3)]
pink_patterns = [(-1,-1), (0,3), (-1,-1)]
brown_patterns = [(-1,-1), (-1,2), (-1,-1)]

start_positions_reds = [(1, 13), (2, 10), (4, 9), (4, 14),
                        (5, 5), (6, 16), (7, 5), (7, 7), (7, 13), (8, 6),(8, 7), (8, 14),
                        (13, 17), (13, 18), (14, 5), (14, 13), (15, 7), (15, 16), (15, 19),
                        (16, 19), (17, 8), (17, 9), (17, 15), (17, 18), (19, 6), (20, 5), (20, 10)]

start_positions_greens = [(0, 4), (0, 7), (1, 14), (4, 17),
                          (5, 1), (6, 14), (7, 4), (7, 20), (8, 5), (8, 17), (8, 18),
                          (16, 1), (17, 5), (17, 19)]

start_positions_blues = [(0, 17), (1, 6), (1, 9), (3, 1), (4, 4), (4, 16),
                         (6, 0), (7, 3), (8, 16), (9, 8), (9, 19),
                         (10, 5), (10, 6), (10, 17), (12, 0), (12, 5), (12, 8), (12, 17),
                         (16, 5)]

start_positions_yellows = [(0, 0), (1, 1), (1, 12), (1, 16), (1, 19), (4, 3),
                           (5, 13),
                           (13, 16), (14, 10), (14, 16),
                           (19, 0), (20, 16), (20, 18)]

start_positions_pinks = [(0, 13), (1, 7), (2, 7),
                         (9, 1), (9, 3), (9, 10),
                         (11, 9), (12, 12),
                         (15, 10), (17, 4),]

start_positions_browns = [(0, 10), (3, 6), (4, 8), (4, 15),
                          (5, 12), (5, 18), (6, 18), (7, 9), (7, 17),
                          (12, 9), (12, 14), (13, 6), (15, 4), (15, 6),
                          (18, 10), (18, 14), (19, 8), (19, 18)]

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

start_positions_greens = [(1, 8), (3, 2),
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

" - MONSTER 5 - "

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

# " - MONSTER 6 - "
#
# red_patterns = [(-1,1), (1,1), (-2,0)]
# green_patterns = [(1,1), (-2,0), (0,-2)]
# blue_patterns = [(-2,-2), (2,1), (1,-1)]
# yellow_patterns = [(-3,1), (2,0), (-2,-1)]
# pink_patterns = [(-2,1), (2,-3), (1,3)]
# brown_patterns = [(0,-2), (3,0), (0,2)]
#
# start_positions_reds = [(3, 7, False),
#                         (8, 19, False),
#                         (10, 20, True), (12, 1, True), (13, 5, False), (14, 11, True),
#                         (17, 20, True), (18, 11, False), (19, 0, True)]
#
# start_positions_greens = [(0, 14, True), (1, 1, True), (1, 7, True), (2, 12, False), (3, 9, True), (3, 15, True), (4, 12, True),
#                           (6, 7, True), (6, 20, True), (7, 3, True), (7, 20, True), (8, 2, True), (9, 2, False),
#                           (11, 8, False), (11, 12, False), (12, 15, False), (15, 17, True),
#                           (16, 13, True), (17, 13, False), (18, 15, True)]
#
# start_positions_blues = [(3, 6, False), (3, 8, False),
#                          (9, 4, True), (9, 10, True),
#                          (15, 18, False), (15, 20, True), (16, 19, False)]
#
# start_positions_yellows = [(3, 20, False), (4, 7, False),
#                            (7, 18, False), (9, 5, True),
#                            (10, 16, False), (10, 19, True), (11, 0, True)]
#
# start_positions_pinks = [(1, 2, False), (4, 19, True),
#                          (7, 15, False), (8, 9, False),
#                          (10, 5, True), (13, 20, False),
#                          (15, 16, False)]
#
# start_positions_browns = [(0, 19, True), (4, 20, True),
#                           (7, 4, False), (7, 6, True),
#                           (11, 11, False), (12, 4, False), (13, 10, True), (14, 18, True),
#                           (19, 6, False), (19, 9, False)]

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
        self.sick_counter = 0

        self.yellows = []
        self.greens = []
        self.browns = []
        self.pinks = []
        self.blues = []
        self.reds = []

        self.text_red = 'red: '
        self.text_green = 'green: '
        self.text_blue = 'blue: '
        self.text_yellow = 'yellow: '
        self.text_pink = 'pink: '
        self.text_brown = 'brown: '

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

        self.text_counter = StringVar(self.jump_counter)
        self.lable_counter = Label(frame, textvariable=self.text_counter, justify=LEFT)
        self.lable_counter.pack()

        self.text_meet_counter = StringVar(self.meet_counter)
        self.lable_meet_counter = Label(frame, textvariable=self.text_meet_counter, justify=LEFT)
        self.lable_meet_counter.pack()

        self.text_child_counter = StringVar(self.child_counter)
        self.lable_child_counter = Label(frame, textvariable=self.text_child_counter, justify=LEFT)
        self.lable_child_counter.pack()

        self.draw_board()
        self.init_monsters()

    def init_monsters(self):
        sick = False
        for start_position in start_positions_yellows:
            if len(start_position) == 3:
                sick = start_position[2]
                start_position = start_position[0:2]
            self.yellows.append(Monster(self.board, 'yellow', start_position, self.canvas, yellow_patterns, sick=sick))

        for start_position in start_positions_greens:
            if len(start_position) == 3:
                sick = start_position[2]
                start_position = start_position[0:2]
            self.greens.append(Monster(self.board, 'green', start_position, self.canvas, green_patterns, sick=sick))

        for start_position in start_positions_browns:
            if len(start_position) == 3:
                sick = start_position[2]
                start_position = start_position[0:2]
            self.browns.append(Monster(self.board, 'brown', start_position, self.canvas, brown_patterns, sick=sick))

        for start_position in start_positions_pinks:
            if len(start_position) == 3:
                sick = start_position[2]
                start_position = start_position[0:2]
            self.pinks.append(Monster(self.board, 'pink', start_position, self.canvas, pink_patterns, sick=sick))

        for start_position in start_positions_blues:
            if len(start_position) == 3:
                sick = start_position[2]
                start_position = start_position[0:2]
            self.blues.append(Monster(self.board, 'blue', start_position, self.canvas, blue_patterns, sick=sick))

        for start_position in start_positions_reds:
            if len(start_position) == 3:
                sick = start_position[2]
                start_position = start_position[0:2]
            self.reds.append(Monster(self.board, 'red', start_position, self.canvas, red_patterns, sick=sick))

    def jump(self):
        self.canvas.delete('all')
        self.draw_board()
        positions = {}
        self.sick_counter = 0

        for r in self.reds:
            if r.sick:
                self.sick_counter += 1
            if r.life == 0:
                continue
            x, y = r.do_jump()
            positions[r] = (x, y)
            #self.text_red += self.check_fields(x, y, alpha)
            #self.text_red += self.check_fields(x, y, numbers)
            self.text_red += self.check_fields(x, y, dna)

        for g in self.greens:
            if g.sick:
                self.sick_counter += 1
            if g.life == 0:
                continue
            x, y = g.do_jump()
            positions[g] = (x, y)
            #self.text_green += self.check_fields(x, y, alpha)
            #self.text_green += self.check_fields(x, y, numbers)
            self.text_green += self.check_fields(x, y, dna)

        for b in self.blues:
            if b.sick:
                self.sick_counter += 1
            if b.life == 0:
                continue
            x, y = b.do_jump()
            positions[b] = (x, y)
            #self.text_blue += self.check_fields(x, y, alpha)
            #self.text_blue += self.check_fields(x, y, numbers)
            self.text_blue += self.check_fields(x, y, dna)

        for ye in self.yellows:
            if ye.sick:
                self.sick_counter += 1
            if ye.life == 0:
                continue
            x, y = ye.do_jump()
            positions[ye] = (x, y)
            #self.text_yellow += self.check_fields(x, y, alpha)
            #self.text_yellow += self.check_fields(x, y, numbers)
            self.text_yellow += self.check_fields(x, y, dna)

        for p in self.pinks:
            if p.sick:
                self.sick_counter += 1
            if p.life == 0:
                continue
            x, y = p.do_jump()
            positions[p] = (x, y)
            #self.text_pink += self.check_fields(x, y, alpha)
            #self.text_pink += self.check_fields(x, y, numbers)
            self.text_pink += self.check_fields(x, y, dna)

        for br in self.browns:
            if br.sick:
                self.sick_counter += 1
            if br.life == 0:
                continue
            x, y = br.do_jump()
            positions[br] = (x, y)
            #self.text_brown += self.check_fields(x, y, alpha)
            #self.text_brown += self.check_fields(x, y, numbers)
            self.text_brown += self.check_fields(x, y, dna)


        #print(positions.values())
        print
        print
        print('ROUND {0}'.format(self.jump_counter + 1))
        print
        print(self.text_red)
        print(self.text_green)
        print(self.text_blue)
        print(self.text_yellow)
        print(self.text_pink)
        print(self.text_brown)
        print
        print(self.sick_counter)
        print

        flipped = {}

        for key, value in positions.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)
                m1 = flipped[value][0]
                m2 = key
                #self.fuck(m1, m2)
                #m1.rest = not m1.rest
                #m2.rest = not m2.rest
                if m1.sick or m2.sick:
                    m1.sick = True
                    m2.sick = True
                self.meet_counter += 1

        # for key, value in flipped.iteritems():
        #     if len(value) > 2:
        #         combos = combinations(value)
        #         for m1, m2 in combos:
        #             self.fuck(m1, m2)
        #             m1.rest = not m1.rest
        #             m2.rest = not m2.rest


        self.jump_counter += 1
        self.text_counter.set(str(self.jump_counter))
        self.text_meet_counter.set(str(self.meet_counter))
        self.text_child_counter.set(str(self.child_counter))

    def check_fields(self, x, y, fields):
        for x_f, y_f, value in fields:
            if x == x_f and y == y_f:
                return value
        return ''

    def fuck(self, m1, m2):
        if (m1.color == 'red' and m2.color == 'green') or (m1.color == 'green' and m2.color == 'red'):
            self.blues.append(Monster(self.board, 'blue', m1.get_position(), self.canvas, blue_patterns))
            print("New Monster: blue")
            self.child_counter += 1
        elif (m1.color == 'green' and m2.color == 'blue') or (m1.color == 'blue' and m2.color == 'green'):
            self.yellows.append(Monster(self.board, 'yellow', m1.get_position(), self.canvas, yellow_patterns))
            print("New Monster: yellow")
            self.child_counter += 1
        elif (m1.color == 'blue' and m2.color == 'yellow') or (m1.color == 'yellow' and m2.color == 'blue'):
            self.pinks.append(Monster(self.board, 'pink', m1.get_position(), self.canvas, pink_patterns))
            print("New Monster: pink")
            self.child_counter += 1
        elif (m1.color == 'yellow' and m2.color == 'pink') or (m1.color == 'pink' and m2.color == 'yellow'):
            self.browns.append(Monster(self.board, 'brown', m1.get_position(), self.canvas, brown_patterns))
            print("New Monster: brown")
            self.child_counter += 1
        elif (m1.color == 'pink' and m2.color == 'brown') or (m1.color == 'brown' and m2.color == 'pink'):
            self.reds.append(Monster(self.board, 'red', m1.get_position(), self.canvas, red_patterns))
            print("New Monster: red")
            self.child_counter += 1
        elif (m1.color == 'brown' and m2.color == 'red') or (m1.color == 'red' and m2.color == 'brown'):
            self.greens.append(Monster(self.board, 'green', m1.get_position(), self.canvas, green_patterns))
            print("New Monster: green")
            self.child_counter += 1

    def draw_board(self):
        self.canvas.delete('all')

        canvas_width = 600
        canvas_height = 600

        self.board
        space = canvas_width / (len(self.board) + 2)
        for i in range(1, len(self.board) + 2):
            self.canvas.create_line(space, space * i, canvas_width - space, space * i, fill='#476042')
            self.canvas.create_line(space * i, space, space * i, canvas_width - space, fill='#476042')

#create view
root = Tk()
app = App(root)
root.mainloop()
