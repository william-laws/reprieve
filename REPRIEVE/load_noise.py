import pygame, os
pygame.mixer.init()

#time to cook
clock_tick = pygame.mixer.Sound(os.path.join('SFX/clock_tick.mp3'))
rewind = pygame.mixer.Sound(os.path.join('SFX/rewind.mp3'))

#no responses
brittany_2 = 0
jay = 0
elaine_1 = 0
elaine_2 = 0
moss_end = 0


ron_1 = pygame.mixer.Sound(os.path.join('VOICES/ron/ron_1.mp3'))
ron_1_1 = pygame.mixer.Sound(os.path.join('VOICES/ron/ron_1_1.mp3'))
ron_1_2 = pygame.mixer.Sound(os.path.join('VOICES/ron/ron_1_2.mp3'))
ron_1_3 = pygame.mixer.Sound(os.path.join('VOICES/ron/ron_1_3.mp3'))
ron_1_4 = pygame.mixer.Sound(os.path.join('VOICES/ron/ron_1_4.mp3'))
ron_1_1_bad = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_1_-1.mp3'))
ron_1_1_neut = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_1_0.mp3'))
ron_1_1_good = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_1_+1.mp3'))
ron_1_2_bad = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_2_-1.mp3'))
ron_1_2_neut = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_2_0.mp3'))
ron_1_2_good = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_2_+1.mp3'))
ron_1_3_bad = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_3_-1.mp3'))
ron_1_3_neut = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_3_0.mp3'))
ron_1_3_good = pygame.mixer.Sound(os.path.join('VOICES/ron/responses/1_3_+1.mp3'))