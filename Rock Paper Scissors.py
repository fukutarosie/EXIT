import pygame
import button

pygame.init()
#background
screen = pygame.display.Info()
sw, sh = screen.current_w, screen.current_h
screen = pygame.display.set_mode((1000, 800))


#image load
background = pygame.transform.scale(pygame.image.load("assets/background.png"),(sw, sh))
paper = pygame.image.load("assets/paper.png").convert_alpha()
rock = pygame.image.load("assets/rock.png").convert_alpha()
scissors = pygame.image.load("assets/scissors.png").convert_alpha()

#background class



#images

start = button.Button(500, 500, paper, 1)
exit = button.Button(450, 200, rock, 1)


#main
def main():
    run = True
    while run:
        if start.draw(screen):
            print("START")
        if exit.draw(screen):
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
