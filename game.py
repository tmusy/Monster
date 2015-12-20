from Tkinter import Canvas, Frame, Button, LEFT, Label, StringVar
from monster import Monster
import tkFont


class App(object):
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
        print
        print('ROUND {0}'.format(self.jump_counter + 1))
        print

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
        pass
