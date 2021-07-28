# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:14:03 2021

@author: betul
"""

import pygame
import random
from settings import*

class NoteF(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/noteF.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,10)
        self.rect.y = random.randrange(0,400)
        self.speedy = random.randrange(1,2)


    def update(self):
        self.rect.x += self.speedy
        if self.rect.x > screen_width - 15:
            self.rect.x = random.randrange(0,10)
            self.rect.y = random.randrange(0, 400)
            self.speedy = random.randrange(1, 2)