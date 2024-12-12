import pygame, sys, time, math
from load_noise import *
from noise_groups import *
from itertools import cycle

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
clock_tick.set_volume(0.1)

#vars
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("REPRIEVE")

#flowchart for the game's code:
#run the file for the person's thing
#if file done, go to response mode

#function 

run = True

font = pygame.font.SysFont("Arial", 40)

current_thing = ron_1_1
mode = 1
playing = False
answer_index = 0
answer_total = 0
answer_log = []
answer_deviation = 0

pygame.mixer.Channel(1).play(current_thing)

def move_to_next(file):
    return (not pygame.mixer.get_busy()) and current_thing == file

while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    surface = font.render(str(playing), True, (255,255,255))
    screen.blit(surface, (200,400))

    if mode == 1:
        # Voicecall is already playing. When it ends, it switches to the next portion of the game, where tobey responds.
        if (not pygame.mixer.get_busy()):
            mode = 2
    elif mode == 2:
        # the cycle-through function for the responses. The file goes to each individual response in sequential order.
        # play the ticking sound in the background. loop it
        # If the audio isn't finished yet and the spacebar is pressed, cycle to the next response
        # if the audio does finish, add the appropriate value and go to the next "step" in the response
        
        cycle_list = []
        if current_thing == ron_1_1:
            if answer_total == 0:
                cycle_list = ron_1_1_g
            elif answer_total == 1:
                cycle_list = ron_1_2_g
            elif answer_total == 2:
                cycle_list = ron_1_3_g

        if not pygame.mixer.get_busy():
            pygame.mixer.Channel(0).play(cycle_list[answer_index])
            pygame.mixer.Channel(1).play(clock_tick, 5)
        
        if pygame.mixer.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print("stinky2")
                    if event.key == pygame.K_SPACE:
                        print("stinky")
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.Channel(1).stop()
                        current_thing = rewind
                        pygame.mixer.Channel(0).play(current_thing)
                        answer_index += 1

    elif mode == 3:
        # run the responses based off of the value from before
        # load/play the next thing
        run = False
        pass

    pygame.display.flip()

pygame.quit()
