import random
import sys
import pygame
from pygame.locals import *

FPS=32
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER='/gallery/sprites/bird.png'
BACKGROUND='/gallery/sprites/background.png'
PIPE='/gallery/sprites/pipe.png'

if __name__ == '__main__':
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')
    GAME_SPRITES['numbers'] =(
        pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load('/gallery/sprites/message.png').convert_alpha(),
    GAME_SPRITES['base'] = pygame.image.load('/gallery/sprites/base.png').convert_alpha(),
    GAME_SPRITES['pipe'] = (
        pygame.image.load('/gallery/sprites/pipe.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/pipe.png').convert_alpha(),
    )
    