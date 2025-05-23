import pygame as pg
import sys
from level import Level
from tile import Tile
from settings import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Game')
        self.clock = pg.time.Clock()

        self.level = Level()


    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

