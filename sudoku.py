""" Importing pygame """
from random import randint
import pygame

pygame.init()

class Cell():
    def __init__(self, number, color, row, col):
        self._number = number
        self._color = color

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Global parameters
WIDTH = 450
ROWS = 9
GAP = WIDTH // ROWS

# Colors
WHITE = (249, 249, 249)
BLACK = (39, 39, 39)
GRAY = (145, 145, 145)
RED = (234, 35, 36)
GREEN = (80, 197, 85)
BLUE = (0, 170, 251)

# Number font
NUMBER_FONT = pygame.font.SysFont('Arial', 50)

# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")

# FPS Clock
clock = pygame.time.Clock()
FPS = 10

def switcher(argument):
    switcher = {
        pygame.K_1: 1,
        pygame.K_2: 2,
        pygame.K_3: 3,
        pygame.K_4: 4,
        pygame.K_5: 5,
        pygame.K_6: 6,
        pygame.K_7: 7,
        pygame.K_8: 8,
        pygame.K_9: 9
    }
    return switcher.get(argument)

def gen_empty_grid():
    """ Generates a grid filled with zeros """
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            grid[i].append(Cell(0, BLACK, i, j))
    
    return grid

def initialize_grid():
    """ Firstly, we will fill a whole grid than
        Then we will remove a random amount of number from the grid
        Ensuring that the grid is solveable """

    empty_grid = gen_empty_grid()
    solve(draw, False, empty_grid)

    attempt = 50

    while attempt > 0:
        row = randint(0, 8)
        col = randint(0, 8)

        if empty_grid[row][col].number != 0:
            empty_grid[row][col].number = 0
            attempt -= 1

    return empty_grid

def get_clicked_pos(pos):
    """ Returns row and column based on click position """
    x, y = pos

    row = x // GAP
    col = y // GAP

    return row, col

def find_empty(grid):
    """ Finds an unfilled cell """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].number == 0:
                return i, j

def is_valid(grid, num, position):
    """ Checks if a number is valid at the given position """
    row, col = position

    # Checking the horizontal ROWS
    for i in range(len(grid[0])):
        if grid[row][i].number == num and col != i:
            return False

    # Checking the vertical columns
    for i in range(len(grid)):
        if grid[i][col].number == num and row != i:
            return False    

    # Checking the 3X3 boxes
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j].number == num and (i, j) != position:
                return False

    return True

def solve(draw, is_drawn, grid):
    """ Solves an empty sudoku board """
    find = find_empty(grid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if is_drawn == False:
        grid[0][0].number = randint(1, 9)

    """ Just so it doesn't visualize always """
    if is_drawn:
        draw()
        clock.tick(20)

    if not find: # If it doesn't find an empty cell
        return True
    else:
        row, col = find # Current row and col

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col].number = i # Sets number
            grid[row][col].color = GREEN if is_drawn else BLACK

            if solve(draw, is_drawn, grid): # Recursive call
                return True

            grid[row][col].number = 0
            grid[row][col].color = RED if is_drawn else BLACK

def draw_grid(win):
    """ Draws the grid lines """
    for i in range(ROWS):
        x = i * GAP
        x_color = BLACK if i % 3 == 0 else GRAY
        pygame.draw.line(win, x_color, (x, 0), (x, WIDTH))
        for j in range(ROWS):
            y = j * GAP
            y_color = BLACK if j % 3 == 0 else GRAY
            pygame.draw.line(win, y_color, (0, y), (WIDTH, y))

def draw(win, grid):
    """ Drawing and rendering the screen """
    win.fill(WHITE)
    draw_grid(win)
    
    """ Drawing the numbers """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            text = NUMBER_FONT.render(str(grid[i][j].number), 1, grid[i][j].color)
            
            x = i * GAP
            y = j * GAP

            if grid[i][j].number != 0:
                win.blit(text, (x + 12, y - 3))

    pygame.display.update()

def main():
    """ Main function """
    run = True

    # The board
    grid = initialize_grid()

    # Selected cell
    sel_row = None
    sel_col = None

    # Main loop
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                sel_row, sel_col = get_clicked_pos(pos)

            if event.type == pygame.KEYDOWN:
                key = event.key

                if key == pygame.K_SPACE:
                    solve(lambda: draw(win, grid), True, grid)

                if sel_row != None and sel_col != None and grid[sel_row][sel_col].number == 0:
                    grid[sel_row][sel_col].number = switcher(key)

                if key == pygame.K_DELETE:
                    if not is_valid(grid, grid[sel_row][sel_col].number, (sel_row, sel_col)):
                        grid[sel_row][sel_col].number = 0

        draw(win, grid)

    pygame.quit()

if __name__ == "__main__":
    main()
