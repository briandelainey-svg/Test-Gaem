import pygame
import random

pygame.display.set_mode((332, 528))
#game dimension: 288 x 528
pygame.display.set_caption('TETRIS (garbage version)')
bg = pygame.image.load('tetris')
blocks = [pygame.image.load('Cube-block'), pygame.image.load('left-L-block'), pygame.image.load('right-R-block'), pygame.image.load('Line-block'), 
          pygame.image.load('T-block'), pygame.image.load('left-Wiggle-block'), pygame.image.load('right-Wiggle-block')]
class Block:
    def __init__(self, colors):
        self.height = 10
        self.width = 10
        color
    def drop():
        y -= 24
    def move():
        print('hi')
        
    def spawn():
        print('hi')
        
class left_L_block(Block):
    def __init__(self, blocks):
        self.shape = blocks(1)
        self.color = colors(1)

class right_L_block(Block):
    def __init__(self, blocks):
        self.shape = blocks(2)

class T_block(Block):
    def __init__(self, blocks):
        self.shape = blocks(4)

class Cube_block(Block):
    def __init__(self, blocks):
        self.shape = blocks(0)

class Line_block(Block):
    def __init__(self, blocks):
        self.shape = blocks(3)

class left_Wiggle_block(Block):
    def __init__(self, blocks):
        self.shape = blocks(5)

class right_Wiggle_block(Block):
    def __init__(self, blocks):
        self.shape = blocks(6)
