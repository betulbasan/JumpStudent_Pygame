# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:22:40 2021

@author: betul
"""
import pygame
#Phone is used as our enemy
class Phone(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/phone.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 3:
			self.move_direction *= -1
			self.move_counter *= -1