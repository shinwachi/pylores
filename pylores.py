from blessings import Terminal
import numpy as np
import time



class Lores:
    def __init__(self):
        self.t = Terminal()
        self.height = 40
        self.width = 40
        self.clear()
        self.pixel = '    '
        self.color = 0.0
        self.gr_mode()

    def gr_mode(self):
        '''
        moves cursor to text area
        :return:
        '''
        print(self.t.move(self.height - 1))

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
lores.randomize()
lores.render()

print("hi")
i = 0
while True:
    lores.randomize()
    lores.render()
    print(i)
    i += 1
    time.sleep(2)

