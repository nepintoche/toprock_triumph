"""
Winners order:
Noha x ∞
***lucas f (prototype)
Alp x2
"""


import pygame,sys
from settings import *
from level import Level


pygame.init()

screen = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()
level = Level(map,screen)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("gray")
    level.run()
    pygame.display.update()
    clock.tick(fps)


