
class Monster(object):
    positions = []

    def __init__(self, board, color, position, canvas, jump_patterns=[], rest=False, sick=False):
        self.board = board
        self.color = color
        self.positions = [position]
        self.canvas = canvas
        self.jump_patterns = jump_patterns
        self.jump_num = 1
        self.rest = rest
        self.sick = sick
        self.life = 5

        self._draw2()

    def add_jump_pattern(self, pattern):
        self.jump_patterns.append(pattern)

    def do_jump(self):
        new_x, new_y = self.positions[-1]
        if not self.rest:
            hit_border = ''

            last_x, last_y = self.positions[-1]
            x, y = self.jump_patterns[self.jump_num % len(self.jump_patterns) - 1]
            new_x = (last_x + x) % len(self.board[0])
            new_y = (last_y + y) % len(self.board)
            self.positions.append((new_x, new_y))

            # hit the border
            if last_y + y < 0:
                hit_border += 'n'
            if last_y + y >= len(self.board):
                hit_border += 's'
            if last_x + x < 0:
                hit_border += 'w'
            if last_x + x >= len(self.board[0]):
                hit_border += 'e'

            self._draw2()
        self.jump_num += 1
        #self.rest = False
        if self.sick:
            self.life -= 1
        return new_x, new_y

    def get_position(self):
        return self.positions[-1]

    def _draw(self, hit_border):
        if not hit_border:
            space = int(self.canvas['width']) / (len(self.board) + 2)

            x1, y1 = self.positions[-1]
            x2, y2 = self.positions[-2]

            self.canvas.create_line((1.5 + x1) * space, (1.5 + y1) * space, (1.5 + x2) * space, (1.5 + y2) * space,
                                    fill=self.color, width=4)

    def _draw2(self):
        space = int(self.canvas['width']) / (len(self.board) + 2)

        x1, y1 = self.positions[-1]
        r = 5
        self.canvas.create_oval((1.5 + x1) * space - r, (1.5 + y1) * space - r,
                                (1.5 + x1) * space + r, (1.5 + y1) * space + r,
                                fill=self.color, width=0)
