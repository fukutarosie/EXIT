import pygame

pygame.init()
#background
screen = pygame.display.Info()
sw, sh = screen.current_w, screen.current_h
window = pygame.display.set_mode((sw, sh))


#image load
background = pygame.transform.scale(pygame.image.load("assets/background.png"),(sw, sh))
paper = pygame.image.load("assets/paper.png").convert_alpha()
rock = pygame.image.load("assets/rock.png").convert_alpha()
scissors = pygame.image.load("assets/scissors.png").convert_alpha()

#background class


#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
#images

start_button = Button(100, 200, paper, 0.8)
exit_button = Button(450, 200, rock, 0.8)




#main
def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        

    pygame.quit()

if __name__ == "__main__":
    main()
