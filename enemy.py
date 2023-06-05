import pygame
import random
#from settings import gravity

class Enemy(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        #self.image = pygame.Surface((10,10))
        #self.image.fill("blue")
        self.image = pygame.image.load("images/enemies/boulder.png")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = random.randint(2,5)
        self.gravity = 0.625
        self.direction.x = -1 #add so it goes in a random direction

    def vertical_movement(self,tiles):
        self.applygravity()

        for tile in tiles.sprites():
             if tile.rect.colliderect(self.rect):
                if self.direction.y > 0: #or worldshift < 0:
                    self.rect.bottom = tile.rect.top
                    self.direction.y = 0
                    self.status = ""
                if self.direction.y < 0:  #or worldshift > 0:
                    self.rect.top = tile.rect.bottom
                    self.direction.y = 0

    def horizontal_movement(self,tiles):
        self.rect.x += self.direction.x * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                    self.direction.x = 1
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left
                    self.direction.x = -1



    def applygravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

#    def destroy(self):


    def update(self, y_shift,tiles):
        self.rect.y += y_shift
        self.vertical_movement(tiles)
        self.horizontal_movement(tiles)
