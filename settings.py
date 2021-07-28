# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:12:54 2021

@author: betul
"""
import pygame
from pygame import mixer

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('JumpStudent (JumpMan)')

#define game variables
tile_size = 30
game_over = 0
main_menu = True
level = 1
max_levels = 3
score = 0

#colors
darkviolet = (148,0,211)
deeppink = (255,20,147)

#load images
bg_img = pygame.image.load('img/bg.jpg')
restart_img = pygame.image.load('img/restart.png')
start_img = pygame.image.load('img/start.png')
exit_img = pygame.image.load('img/exit.png')

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#load sounds
pygame.mixer.music.load('musics/background-music-jumpman.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
book_fx = pygame.mixer.Sound('musics/book.wav')
book_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('musics/player-jumping-music.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('musics/gameover-music-jumpman.wav')
game_over_fx.set_volume(5)