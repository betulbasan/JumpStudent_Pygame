# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:40:51 2021

@author: betul
"""

import pygame 
from settings import*
#Book is used as the thing to be collected like coin.
class Book(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/book.png')
		self.image = pygame.transform.scale(img, (int(tile_size* 1.5) // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)