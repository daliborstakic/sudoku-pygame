""" Importing pygame """
from turtle import width
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

# Colors
WHITE = (249, 249, 249)
BLACK = (39, 39, 39)
GRAY = (145, 145, 145)
RED = (234, 35, 36)
GREEN = (80, 197, 85)

# Number font
NUMBER_FONT = pygame.font.SysFont('Arial', 50)

# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")

def gen_empty_grid(rows):
    """ Generates a grid filled with zeros """
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(Cell(0, BLACK, i, j))
    
    return grid

def initialize_grid(grid):
    """ Firstly, we will fill a whole grid than
        Then we will remove a random amount of number from the grid
        Ensuring that the grid is solveable """

def find_empty(grid):
    """ Finds an unfilled cell """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].number == 0:
                return i, j

def is_valid(grid, num, position):
    """ Checks if a number is valid at the given position """
    row, col = position

    # Checking the horizontal rows
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

def solve(grid):
    """ Solves an empty sudoku board """
    find = find_empty(grid)

    if not find: # If it doesn't find an empty cell
        return True
    else:
        row, col = find # Current row and col

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col].number = i # Sets number

            if solve(grid): # Recursive call
                return True

            grid[row][col].number = 0

def draw_grid(win, width, rows):
    """ Draws the grid lines """
    gap = width // rows

    for i in range(rows):
        x = i * gap
        x_color = BLACK if i % 3 == 0 else GRAY
        pygame.draw.line(win, x_color, (x, 0), (x, width))
        for j in range(rows):
            y = j * gap
            y_color = BLACK if j % 3 == 0 else GRAY
            pygame.draw.line(win, y_color, (0, y), (width, y))

def draw(win, grid, width, rows):
    """ Drawing and rendering the screen """
    win.fill(WHITE)
    draw_grid(win, width, rows)
    
    gap = width // rows

    """ Drawing the numbers """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            text = NUMBER_FONT.render(str(grid[i][j].number), 1, grid[i][j].color)
            
            x = i * gap
            y = j * gap

            if grid[i][j].number != 0:
                win.blit(text, (x + 10, y - 3))

    pygame.display.update()

def main():
    """ Main function """
    run = True

    grid = gen_empty_grid(ROWS)
    solve(grid)

    # Main loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(win, grid, WIDTH, ROWS)

    pygame.quit()

if __name__ == "__main__":
    main()
