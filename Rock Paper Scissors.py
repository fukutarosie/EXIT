import pygame
import button

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



#images

start_button = button.Button(1000, 700, paper, 0.8)
exit_button = button.Button(450, 200, rock, 0.8)




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
