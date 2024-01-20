import pygame
import random

pygame.init()

screen = pygame.display.Info()
sw, sh = screen.current_w, screen.current_h
window = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Rock Paper Scissors")


background = pygame.transform.scale(pygame.image.load("assets/background.png"),(sw, sh))
paper = pygame.image.load("assets/paper.png")
rock = pygame.image.load("assets/rock.png")
scissors = pygame.image.load("assets/scissors.png")

def draw():
    window.blit(background, (0,0))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
