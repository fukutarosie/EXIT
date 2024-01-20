import pygame
import button
import images

pygame.init()
#background

BG = pygame.display.set_mode((1536, 864))


#image load
background = pygame.image.load("assets/Background.png").convert_alpha()
exit = pygame.image.load("assets/exit.png").convert_alpha()
word = pygame.image.load("assets/word.png").convert_alpha()

#backgrounds
background_img = images.Images(0, 0, background, 0.8)
word_img = images.Images(200, 40, word, 1.3)

#images
exit_button = button.Button(620, 150, exit, 1.5)

#main
def main():
    run = True
    while run:
        background_img.draw(BG)
        word_img.draw(BG)
        if exit_button.draw(BG):
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
