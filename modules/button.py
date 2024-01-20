import pygame

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, BG):
		action = False
		pos = pygame.mouse.get_pos()
		finger_cursor = pygame.image.load("assets/finger.png").convert_alpha()

		BG.blit(self.image, (self.rect.x, self.rect.y))

		if self.rect.collidepoint(pos) == False:
			pygame.mouse.set_visible(True)

		if self.rect.collidepoint(pos):
			pygame.mouse.set_visible(False)
			BG.blit(finger_cursor, pos)
			
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action