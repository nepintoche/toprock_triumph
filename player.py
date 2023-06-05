import pygame
from settings import gravity
from support import import_folder
#player class
class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.distat = "r"
        self.direction = pygame.math.Vector2(0,0)
        self.animations = {}
        self.import_character_assets()
        self.frame_index = 0
        self.animationspeed = 0.1

#        self.image = pygame.Surface((7.8125,15.625))
#        self.image.fill("red")
        self.image = self.animations["idle"][self.frame_index]#pygame.image.load("images/player/idle/idle_0.png")
        self.rect = self.image.get_rect(topleft = pos)

        self.speed = 3.125
        self.horspeed = 8
        self.jump_speed = -10.9375
        self.alive = True
        #sounds
        self.jump_sound = pygame.mixer.Sound("sound/effects/jump.wav")
        self.win_sound = pygame.mixer.Sound("sound/effects/win.wav")
        self.death_sound = pygame.mixer.Sound("sound/effects/death.wav")


        self.status = "idle"
        self.jumpcount = 0
        self.win = False
        self.count = 0

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animationspeed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        if self.distat == "l":
                self.image = pygame.transform.flip(self.image,flip_x= True,flip_y=False)

    def import_character_assets(self):
        player_path = "images/player"

        self.animations = {"idle": [], "jump": [],"walk": [],"death":[]}

        for animation in self.animations.keys():
            full_path = player_path +"/"+ animation
            #print(full_path)
            self.animations[animation] = import_folder(full_path)
#for animation, from support file

#where keyboard keys happenkeyboard
    def get_input(self):
        keys = pygame.key.get_pressed()
        if self.alive:

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.distat = "r"

            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.distat = "l"
            else:
                self.direction.x = 0


            if keys[pygame.K_SPACE]:
                self.jump()

#status for animations
    def get_status(self,tiles):
        if self.alive == False and self.win == False:
            self.status = "death"
        elif self.direction.y < 0:
            self.status= "jump"
        elif self.direction.x == 0 and self.direction.y == 0:
            self.status = "idle"
        else:
            self.status = "walk"



    def horizontal_movement(self,tiles,worldshift,scrollstatus):
        if self.alive:
            self.rect.x += self.direction.x * self.speed

            for tile in tiles.sprites():
                if tile.rect.colliderect(self.rect):
                    if self.direction.x < 0:
                        self.rect.left = tile.rect.right
                    elif self.direction.x > 0:
                        self.rect.right = tile.rect.left



    def jump(self):
        if self.status != "jump" and self.jumpcount == 0:
            self.direction.y = self.jump_speed
            self.jumpcount = 1
            pygame.mixer.Sound.play(self.jump_sound)




    def vertical_movement(self,tiles,worldshift):

        self.apply_gravity()
        for tile in tiles.sprites():
                if tile.rect.colliderect(self.rect):
                    if self.direction.y > 0: #or worldshift < 0:
                        self.rect.bottom = tile.rect.top
                        self.direction.y = 0
                        self.jumpcount = 0
                    if self.direction.y < 0:  #or worldshift > 0:
                        self.rect.top = tile.rect.bottom
                        self.direction.y = 0


    def apply_gravity(self):
        self.direction.y += gravity
        self.rect.y += self.direction.y

    def destroy(self):
        #self.image = pygame.image.load("graphics/player/DinoSprites_doux.gif")
        print("dead")
        if self.alive:
            pygame.mixer.Sound.play(self.death_sound)
        self.alive = False

#dub means win. dub and destroy called in level
    def dub(self):

        if self.win == False:
            pygame.mixer.Sound.play(self.win_sound)
        self.alive = False
        self.win = True



#runs every second
    def update(self,tiles,worldshift,scrollstatus):
        self.get_input()
        self.horizontal_movement(tiles,worldshift,scrollstatus)
        self.vertical_movement(tiles,worldshift)
        self.get_status(tiles)
        self.animate()

        if self.alive == False and self.win == False:
            self.count += 1

        if self.count > 60:
            self.image = pygame.image.load("images/player/tomb/tombstone.png")
            self.image = pygame.transform.scale(self.image,(25,25))


