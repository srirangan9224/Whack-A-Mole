import pygame
import sys
import random

ROWS = 20
COLS = 16
HEIGHT = 512
WIDTH = 640
LINE_WIDTH = 1
LINE_COLOR = "dark green"
SQUARE_SIZE = 32


def generate_random_pos(current):
    new = current
    while new == current:
        new = random.randrange(1,ROWS), random.randrange(1,COLS)
    return new


def draw_grid(screen):
    #vertical lines
    for i in range(1,ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (SQUARE_SIZE*i,0),
            (SQUARE_SIZE*i,HEIGHT),
            LINE_WIDTH
        )
    #horizontal lines
    for i in range(1,COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0,SQUARE_SIZE*i),
            (WIDTH,SQUARE_SIZE*i),
            LINE_WIDTH
            )
        
        
def get_topleft(x,y):
    return SQUARE_SIZE*x,SQUARE_SIZE*y


def draw_mole(screen,mole_image,pos):
    screen.blit(mole_image,mole_image.get_rect(topleft=get_topleft(pos[0],pos[1])))
    
    
def main():
    # try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-A-Mole")
        clock = pygame.time.Clock()
        running = True
        
        new_mole = (0,0)
        
            
        
        # game loop 
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x1,y1 = event.pos
                    row,col = x1//SQUARE_SIZE,y1//SQUARE_SIZE
                    if (new_mole == (row,col)):
                        new_mole = generate_random_pos(new_mole)
                        screen.fill("light green")
                        draw_grid(screen)
                        draw_mole(screen,mole_image,new_mole)
            
            
            screen.fill("light green")
            draw_grid(screen)
            draw_mole(screen,mole_image,new_mole)
        
            pygame.display.flip()
            clock.tick(60)
        
    # finally:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()