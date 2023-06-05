from os import walk
import pygame


def import_folder(path):
    #print("in the folder")
    surface_list = []
    for _, __, img_files in walk(path):
        #print("hello")
        for file in img_files:
            #print(file)
            full_path = path + "/"+ file
            print(full_path)
            image = pygame.image.load(full_path)
            image = pygame.transform.scale(image,(20,20))
            surface_list.append(image)


    return surface_list


