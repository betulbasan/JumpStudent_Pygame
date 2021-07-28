# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:50:02 2021

@author: ASUS
"""
#Import libraries
import pygame
import pickle
from os import path

#Initialize all imported pygame modules
pygame.init()

clock = pygame.time.Clock()
fps = 60 #Standard fps

#Set game window
tile_Size = 30
cols = 20
margin = 100
screen_width = tile_Size * cols
screen_height = (tile_Size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')


#Load images (background,dirt,grass,phone,platform_x,platform_y,lava,book,exit,save,load,stair)
bg_img = pygame.image.load('img/bg.jpg')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
dirt_img = pygame.image.load('img/dirt.png')
grass_img = pygame.image.load('img/grass.png')
enemy_img = pygame.image.load('img/phone.png')
platform_x_img = pygame.image.load('img/platform_x.png')
platform_y_img = pygame.image.load('img/platform_y.png')
lava_img = pygame.image.load('img/lava.png')
book_img = pygame.image.load('img/book.png')
exit_img = pygame.image.load('img/school.png')
save_img = pygame.image.load('img/save.png')
load_img = pygame.image.load('img/load.png')
stair_img = pygame.image.load('img/stair.png')


#Define game variables
clicked = False
level = 1

#Define colors
darkviolet = (148,0,211)
deeppink = (255,20,147)

#Create a Font object from the system fonts
font = pygame.font.SysFont('ravie', 18)

#Create empty tile list
world_data = []
for row in range(20):
    r = [0] * 20
    world_data.append(r)

#Create boundary using cols
for tile in range(0, 20):
    world_data[19][tile] = 2
    world_data[0][tile] = 1
    world_data[tile][0] = 1
    world_data[tile][19] = 1

#The function to output text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_grid():
    for c in range(21):
        #vertical lines
        pygame.draw.line(screen, darkviolet, (c * tile_Size, 0), (c * tile_Size, screen_height - margin))
        #horizontal lines
        pygame.draw.line(screen, darkviolet, (0, c * tile_Size), (screen_width, c * tile_Size))


def draw_world():
    for row in range(20):
        for col in range(20):
            if world_data[row][col] > 0:
                if world_data[row][col] == 1:
                    #dirt blocks
                    img = pygame.transform.scale(dirt_img, (tile_Size, tile_Size))
                    screen.blit(img, (col * tile_Size, row * tile_Size))
                if world_data[row][col] == 2:
                    #grass blocks
                    img = pygame.transform.scale(grass_img, (tile_Size, tile_Size))
                    screen.blit(img, (col * tile_Size, row * tile_Size))
                if world_data[row][col] == 3:
                    #enemy blocks
                    img = pygame.transform.scale(enemy_img, (tile_Size, int(tile_Size * 0.75)))
                    screen.blit(img, (col * tile_Size, row * tile_Size + (tile_Size * 0.25)))
                if world_data[row][col] == 4:
                    #horizontally moving platform
                    img = pygame.transform.scale(platform_x_img, (tile_Size, tile_Size // 2))
                    screen.blit(img, (col * tile_Size, row * tile_Size))
                if world_data[row][col] == 5:
                    #vertically moving platform
                    img = pygame.transform.scale(platform_y_img, (tile_Size, tile_Size // 2))
                    screen.blit(img, (col * tile_Size, row * tile_Size))
                if world_data[row][col] == 6:
                    #lava
                    img = pygame.transform.scale(lava_img, (tile_Size, tile_Size // 2))
                    screen.blit(img, (col * tile_Size, row * tile_Size + (tile_Size // 2)))
                if world_data[row][col] == 7:
                    #book
                    img = pygame.transform.scale(book_img, (int(tile_Size* 1.5) // 2, tile_Size // 2))
                    screen.blit(img, (col * tile_Size + (tile_Size // 4), row * tile_Size + (tile_Size // 4)))
                if world_data[row][col] == 8:
                    #stair
                    img = pygame.transform.scale(stair_img, (tile_Size, tile_Size // 2))
                    screen.blit(img, (col * tile_Size, row * tile_Size + (tile_Size // 2)))
                if world_data[row][col] == 9:
                    #school
                    img = pygame.transform.scale(exit_img, (int(tile_Size * 2), int(tile_Size * 1.9)))
                    screen.blit(img, (col * tile_Size, row * tile_Size - (tile_Size // 2)))



class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        #Get the mouse cursor position
        position = pygame.mouse.get_pos()

        #Check mouseover and clicked conditions
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#Create load and save buttons to save or load levels
save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

#Main game loop
run = True
while run:

    clock.tick(fps)

    #Draw background
    screen.fill(deeppink)
    screen.blit(bg_img, (0, 0))

    #Load and save levels
    if save_button.draw():
        #save level data
        pickle_out = open(f'level{level}_data', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
    if load_button.draw():
        #load in level data
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)


    #Show the grid and draw the level tiles
    draw_grid()
    draw_world()


    #The text which shows the current level
    draw_text(f'Level: {level}', font, darkviolet, tile_Size, screen_height - 60)
    draw_text('Press UP or DOWN to change level', font, darkviolet, tile_Size, screen_height - 40)

    #Event handler
    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.QUIT:
            run = False
        #Mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            position = pygame.mouse.get_pos()
            x = position[0] // tile_Size
            y = position[1] // tile_Size
            #Check that the coordinates are within the tile area
            if x < 20 and y < 20:
                #Update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] += 1
                    if world_data[y][x] > 9:
                        world_data[y][x] = 0
                elif pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] -= 1
                    if world_data[y][x] < 0:
                        world_data[y][x] = 9
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        #Up and down key presses to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 1:
                level -= 1

    #Update game display window
    pygame.display.update()

pygame.quit()