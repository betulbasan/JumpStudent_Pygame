# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:12:11 2021

@author: betul
"""

import pygame
from settings import*

class Stair(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/stair.png')
        self.image = pygame.transform.scale(img, (tile_size - 10, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y