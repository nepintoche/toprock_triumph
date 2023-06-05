import pygame

class Flag(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        #self.image = pygame.Surface((10,25))
        #self.image.fill("green")
        self.image = pygame.image.load("images/flag/flag-pole.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect(topleft=pos)


