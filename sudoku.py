""" Importing pygame """
import pygame

# Global parameters
WIDTH = 500
ROWS = 9

# Colors
WHITE = (255, 255, 255)

# Screen
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")

def draw(win):
    """ Drawing and rendering the screen """
    win.fill(WHITE)
    pygame.display.update()

def main():
    """ Main function """
    run = True

    # Main loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(win)

    pygame.quit()

if __name__ == "__main__":
    main()
