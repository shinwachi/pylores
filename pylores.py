from blessings import Terminal
import numpy as np
import time



class Lores:
    def __init__(self):
        self.t = Terminal()
        self.height = 40
        self.width = 40
        self.clear()
        self.pixel = '   '
        self._color = 0.0
        self.gr_mode()

    def gr_mode(self):
        '''
        moves cursor to text area
        :return:
        '''
        print(self.t.move(self.height - 1))

    def color(self, color: int):
        self._color = float(color)

    def plot(self, x: int, y: int):
        self.matrix[x,y] = self._color

    def hlin(self, x1: int, x2: int, y: int):
        '''
        Equivalent of HLIN x1,x2 at y.  Draws a horizontal line
        :param x1:
        :param x2:
        :param y:
        :return:
        '''
        self.matrix[x1:x2,y] = self._color

    def vlin(self, y1: int, y2: int, x: int):
        self.matrix[x, y1:y2] = self._color

    def scrn(self, x: int, y: int):
        return int(self.matrix[x,y])

    def randomize(self):
        '''
        randomizes pixel matrix
        :return:
        '''
        self.matrix = np.random.rand(self.width, self.height) * 16

    def clear(self):
        '''
        resets pixel matrix
        :return:
        '''
        self.matrix = np.zeros((self.width, self.height))

    def render_pixel(self, x: int, y: int, cell_color: int):
        with self.t.location(0,0):
            content = self.t.move(y, x * len(self.pixel))
            content += self.t.reverse
            content += self.t.color(cell_color)
            content += self.pixel
            print(content, end='', flush=True)

    def render(self):
        for row_idx, row in enumerate(np.array(self.matrix)):
            for col_idx, cell_value in enumerate(row):
                cell_color = int(cell_value)
                self.render_pixel(col_idx, row_idx, cell_color)


lores = Lores()
# lores.randomize()
lores.color(1)
lores.plot(5,10)
lores.hlin(0, 40, 3)
lores.vlin(0, 40, 2)
lores.render()

print("hi")
i = 0
while True:

    time.sleep(2)
    print(i)
    i += 1
    # lores.randomize()
    lores.render()

