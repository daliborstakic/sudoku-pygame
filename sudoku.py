""" Importing pygame """
import pygame

# Global parameters
WIDTH = 500
ROWS = 9

# Colors
WHITE = (249, 249, 249)
BLACK = (39, 39, 39)
GRAY = (145, 145, 145)

# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")

def gen_empty_grid(rows):
    """ Method generates an empty matrix """

    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(None)
    
    return grid

def initialize_grid(grid):
    """ Firstly, we will fill a whole grid than
        Then we will remove a random amount of number from the grid
        Ensuring that the grid is solveable """

def find_empty(grid):
    """ Finds an unfilled cell """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j]:
                return i, j

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
