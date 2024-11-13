import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        xValue = 0
        yValue = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] >= xValue and event.pos[0] <= xValue + mole_image.get_width()) and (event.pos[1] >= yValue and event.pos[1] <= yValue + mole_image.get_height()):
                            xValue = random.randrange(0, 640-mole_image.get_width(), 32)
                            yValue = random.randrange(0, 512-mole_image.get_height(), 32)

            screen.fill("light pink")
            for i in range(1, 17):
                pygame.draw.line(screen, (0, 0, 0), (0,i*32), (640, i*32))
            for i in range(1,21):
                pygame.draw.line(screen, (0, 0, 0), (i*32, 0), (i*32, 512))
            screen.blit(mole_image, (xValue, yValue))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
