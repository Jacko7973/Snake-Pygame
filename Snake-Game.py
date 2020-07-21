import sys
import random
import pygame
from pygame.locals import *


class Game(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('Snake')
        self.canvas = pygame.display.set_mode((800, 800))

        self.setUpGame()

        running = True
        while running:
            self.update()
    
    def setUpGame(self):
        self.score = 0
        self.snakePosList = [(40, 40)]
        self.direction = 0

        self.snake_surface = pygame.Surface((10, 10))
        self.snake_surface.fill((0, 240, 0))

        self.apple_surface = pygame.Surface((10, 10))
        self.apple_surface.fill((240, 0, 0))

        self.applePos = self.newApplePos()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_UP and self.direction != 2:
                    self.direction = 0
                elif event.key == K_RIGHT and self.direction != 3:
                    self.direction = 1
                elif event.key == K_DOWN and self.direction != 0:
                    self.direction = 2
                elif event.key == K_LEFT and self.direction != 1:
                    self.direction = 3

        self.canvas.fill((0, 0, 0))


        self.moveSnake()
        snakeHeadPos = self.snakePosList[0]
        self.canvas.blit(self.apple_surface, (self.applePos[0]*10, self.applePos[1]*10))
        for pos in self.snakePosList:
            self.canvas.blit(self.snake_surface, (pos[0]*10, pos[1]*10))

        if snakeHeadPos == self.applePos:
            self.applePos = self.newApplePos()
            self.score += 1

        if snakeHeadPos[0] < 0 or snakeHeadPos[0] >= 80:
            self.setUpGame()
        if snakeHeadPos[1] < 0 or snakeHeadPos[1] >= 80:
            self.setUpGame()
        if snakeHeadPos in self.snakePosList[1:]:
            self.setUpGame()

        
        pygame.display.update()
        pygame.display.flip()
        self.clock.tick(10)

    def newApplePos(self):
        x = random.randint(0, 79)
        y = random.randint(0, 79)
        return (x, y)

    def moveSnake(self):
        x, y = self.snakePosList[0][0], self.snakePosList[0][1]
        if self.direction == 0:
            y -= 1
        elif self.direction == 1:
            x += 1
        elif self.direction == 2:
            y += 1
        elif self.direction == 3:
            x -= 1
        self.snakePosList.insert(0, (x, y))
        if len(self.snakePosList) > self.score + 1:
            del self.snakePosList[-1]




if __name__ == '__main__':
    game = Game()
