# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:34:31 2021

@author: betul
"""

import pygame
from settings import*
#School building is used as our destination point.
class School(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/school.png')
		self.image = pygame.transform.scale(img, (int(tile_size * 2.2), int(tile_size * 2 + 5)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y