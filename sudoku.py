""" Importing pygame """
import pygame

class Cell():
    def __init__(self, value, color, row, col):
        self._value = value
        self._color = color
        self.row = row
        self.col = col
        self.font = pygame.font.SysFont('Arial', 20)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def draw_number(self, win, width, rows):
        gap = width // rows
        x = self.row * gap
        y = self.col * gap

        text = self.font.render(str(self.value), 1, self.color)
        text.blit(win, (x + text.get_width() / 2, y + text.get_height()))


# Global parameters
WIDTH = 500
ROWS = 9

# Colors
WHITE = (249, 249, 249)
BLACK = (39, 39, 39)
GRAY = (145, 145, 145)
RED = (234, 35, 36)
GREEN = (80, 197, 85)

# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")

def gen_empty_grid(rows):
    """ Generates a grid filled with zeros """
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(0)
    
    return grid

def initialize_grid(grid):
    """ Firstly, we will fill a whole grid than
        Then we will remove a random amount of number from the grid
        Ensuring that the grid is solveable """

def find_empty(grid):
    """ Finds an unfilled cell """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j

def is_valid(grid, num, position):
    """ Checks if a number is valid at the given position """
    row, col = position

    # Checking the horizontal rows
    for i in range(len(grid[0])):
        if grid[row][i] == num and col != i:
            return False

    # Checking the vertical columns
    for i in range(len(grid)):
        if grid[i][col] == num and row != i:
            return False

    # Checking the 3X3 boxes
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != position:
                return False

    return True

def solve(grid, width, rows, draw=None, is_drawn=None):
    """ Solves an empty sudoku board """
    find = find_empty(grid)

    draw()

    if not find: # If it doesn't find an empty cell
        return True
    else:
        row, col = find # Current row and col

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i # Sets value

            if solve(grid): # Recursive call
                return True

            grid[row][col] = 0

def draw_grid(win, width, rows):
    gap = width // rows

    for i in range(rows):
        x = i * gap
        x_color = BLACK if i % 3 == 0 else GRAY
        pygame.draw.line(win, x_color, (x, 0), (x, width))
        for j in range(rows):
            y = j * gap
            y_color = BLACK if j % 3 == 0 else GRAY
            pygame.draw.line(win, y_color, (0, y), (width, y))

def draw(win, width, rows):
    """ Drawing and rendering the screen """
    win.fill(WHITE)
    draw_grid(win, width, rows)
    pygame.display.update()

def main():
    """ Main function """
    run = True

    # Main loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(win, WIDTH, ROWS)

    pygame.quit()

if __name__ == "__main__":
    main()
