import pygame,random
from settings import *
from tile import Tile
from player import Player
from enemy import Enemy
from flag import Flag
from despawner import Despawn


class Level:

    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.flag = pygame.sprite.GroupSingle()
        self.despawns = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.setup_level(level_data)
        self.scrollstatus = ""
        self.count = 0
        self.count2 = 0
        self.worldshift = 0




#needs to rerun when you press respawn
    def setup_level(self,layout):
        pygame.mixer.music.load("sound/music/main_music.mp3")
        pygame.mixer.music.play(-1)
        self.enemy_spawn_list = []
        for row_index,row in enumerate(layout):
            for cell_index,cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                elif cell == "e":
                    enemy = Enemy((x,y))
                    self.enemies.add(enemy)
                    self.enemy_spawn_list.append((x,y))
                elif cell == "f":
                    flag = Flag((x,y))
                    self.flag.add(flag)
                elif cell == "d":
                    despawner = Despawn((x,y))
                    self.despawns.add(despawner)


#faster rate spawner
    def enemy_spawn1(self):

        enemy2 = Enemy((self.enemy_spawn_list[1][0],self.enemy_spawn_list[1][1]))
        enemy3 = Enemy((self.enemy_spawn_list[2][0],self.enemy_spawn_list[2][1]))

        self.enemies.add(enemy2)
        self.enemies.add(enemy3)
#slower spawner
    def enemy_spawn2(self):
        enemy = Enemy((self.enemy_spawn_list[0][0],self.enemy_spawn_list[0][1]))
        self.enemies.add(enemy)

#prototype scrolling
    def scroll_y(self):
        pass
        """
        player = self.player.sprite
        player_y = player.rect.y
        direction_y = player.direction.y

        if player_y < screenheight / 4 and direction_y < 0:
            global scrollstatus
            self.worldshift = 8
            #player.speed = 0
            self.scrollstatus = "scrolling"
        elif player_y > screenheight- 2*tile_size and direction_y > 0:
            self.worldshift = -16
            #player.speed = 0
            self.scrollstatus = "scrolling"
        else:
            self.worldshift = 0
            #player.speed = 8
            self.scrollstatus = "" """
#respawn after death or win
    def restartcheck(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.tiles.empty()
            self.player.empty()
            self.enemies.empty()
            self.flag.empty()
            self.despawns.empty()
            self.count = 0
            self.count2 = 0
            self.setup_level(map)


#rruns 60 times per second
    def run(self):

        self.tiles.update(self.worldshift,self.player.sprite)
        self.tiles.draw(self.display_surface)
        self.scroll_y()
        self.player.update(self.tiles,self.worldshift,self.scrollstatus)
        self.player.draw(self.display_surface)
        self.flag.draw(self.display_surface)
        self.despawns.draw(self.display_surface)
        self.enemies.update(self.worldshift, self.tiles)
        self.enemies.draw(self.display_surface)
        self.restartcheck()

        #enemy spawn
        self.count += 1


        if self.count == 180 * diffculty:
            self.enemy_spawn1()
            self.count = 0

        self.count2 += 1


        if self.count2 == 240 * diffculty:
            self.enemy_spawn2()
            self.count2 = 0


        #collisions between player and enemy
        collided_with = pygame.sprite.spritecollide(self.player.sprite, self.enemies, False)

        for enemy in collided_with:

            print(enemy.rect.x,enemy.rect.y)
            self.player.sprite.destroy()
            break

        #player and flage
        collided_with = pygame.sprite.spritecollide(self.player.sprite, self.flag, False)

        for flag in collided_with:
            print("win")
            self.player.sprite.dub()
            pygame.mixer.music.stop()


            for enemy in self.enemies:
                self.enemies.remove(enemy)



        #despawn enemy
        collided_with = pygame.sprite.spritecollide(self.despawns.sprite, self.enemies, False)
        for enemy in collided_with:
            self.enemies.remove(enemy)
