import pygame

class Button():
	def __init__(self, x, y, image, width,screen):
		scale = width/(image.get_width())
		self.image = pygame.transform.scale(image, (width, image.get_height()*scale))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False
		screen.blit(self.image, (self.rect.x, self.rect.y))

	def down(self, screen):
		action = False
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# screen.blit(self.image, (self.rect.x, self.rect.y))

		return action