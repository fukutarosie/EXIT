import pygame
from modules import button
from modules import images

pygame.init()

#background
BG = pygame.display.set_mode((1536, 864))

#time
countdown = 10000

#image load
background = pygame.image.load("assets/Background.png").convert_alpha()
exit = pygame.image.load("assets/exit.png").convert_alpha()
word = pygame.image.load("assets/word.png").convert_alpha()
lose = pygame.image.load("assets/Lose.png").convert_alpha()
win = pygame.image.load("assets/Win.png").convert_alpha()
restart_lose = pygame.image.load("assets/restart_lose.png").convert_alpha()
replay_win = pygame.image.load("assets/replay_win.png").convert_alpha()

#images
background_img = images.Images(0, 0, background, 0.8)
word_img = images.Images(200, 40, word, 1.3)
win_img = images.Images(0, 0, win, 0.8)
lose_img = images.Images(0, 0, lose, 0.8)

#buttons
exit_button = button.Button(630, 175, exit, 1.5)
replay_win_button = button.Button(600, 550, replay_win, 0.8)
restart_lose_button = button.Button(490, 715, restart_lose, 0.8)

#main
def main():
    run = True
    game_win = False
    while run:
        current_time = pygame.time.get_ticks()
        time_remaining = max(0, countdown - current_time)

        #start
        if game_win == False and time_remaining > 0:
            background_img.draw(BG)
            word_img.draw(BG)
            if exit_button.draw(BG):
                game_win = True

        #win
        if game_win == True:
            win_img.draw(BG)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if replay_win_button.draw(BG):
                game_win = False
                current_time = 1
        
        #lose
        if game_win == False and time_remaining == 0:
            lose_img.draw(BG)
            if restart_lose_button.draw(BG):
                game_win = False
                current_time = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()
