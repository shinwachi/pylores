from blessings import Terminal
import numpy as np

t = Terminal()

LORES_HEIGHT = 40
LORES_WIDTH = 40
lores_matrix = np.random.rand(LORES_HEIGHT, LORES_WIDTH)
print(t.clear+t.move(LORES_HEIGHT-1))


def plot(x: int, y: int, cell_color: int, pixel = '    '):
    with t.location(0, 0):
        content = t.move(y, x * len(pixel))
        content += t.reverse
        content += t.color(cell_color)
        content += pixel
        print(content, end='', flush=True)


def render(lores_matrix):
    for row_idx, row in enumerate(np.array(lores_matrix)):
        for col_idx, cell_value in enumerate(row):
            cell_color = int(cell_value * 16)
            plot(col_idx, row_idx, cell_color)


render(lores_matrix)
print("hi")
while True:
    lores_matrix = np.random.rand(LORES_HEIGHT, LORES_WIDTH)
    render(lores_matrix)
    pass
