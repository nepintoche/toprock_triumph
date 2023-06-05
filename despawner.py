import pygame

#class of despawners. in level when impact with enemy it despawns
class Despawn(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((3,25))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
