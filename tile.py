import pygame


#just tiles
class Tile(pygame.sprite.Sprite):

    def __init__(self,pos,size):
        super().__init__()
        #self.image = pygame.Surface((size,size))
        #self.image.fill("grey")
        image = pygame.image.load("images/tiles/tile2.png")
        self.image = pygame.transform.scale(image,(size,size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,y_shift,player):
        self.rect.y += y_shift


#idea for having scrolling
"""
        if player.rect.colliderect(self.rect):
            if y_shift > 0:
                self.rect.top = player.rect.bottom
                y_shift = 0
            if y_shift < 0:
                self.rect.bottom = player.rect.top
                y_shift = 0
"""
