import pygame, sys, time
from load_noise import *

pygame.init()
pygame.mixer.init()

#vars
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("REPRIEVE")

#flowchart for the game's code:
#run the file for the person's thing
#move into "response" mode
#function 

run = True

font = pygame.font.SysFont("Arial", 40)

surface = font.render("test", True, (255,255,255))
screen.blit(surface, (400,400))

ron_1.play()
current_thing = "ron_1"

def move_to_next(file):
    return (not pygame.mixer.get_busy()) and current_thing == file
    

while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    surface = font.render("test", True, (255,255,255))
    screen.blit(surface, (400,400))

    if move_to_next("ron_1"):
        current_thing = "ron_1_1"
        ron_1_1.play()

pygame.quit()
