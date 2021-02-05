# import files
import pygame
import config as c
import color as cl
import time
import game_h as game


def main():
    # pygame init function and set window title
    pygame.init()
    pygame.display.set_caption('GK')

    # functions call
    run = True
    while run:
        pygame.time.delay(10)
        c.win.fill(cl.black)

        game.if_close()

        greay_rect = pygame.Surface((500, 100), pygame.SRCALPHA)
        pygame.draw.rect(greay_rect, cl.greay, greay_rect.get_rect())
        c.win.blit(greay_rect, (0, 400))
        pygame.display.update()
    time.sleep(1)
    # close window
    pygame.quit()


if __name__ == "__main__":
    main()
