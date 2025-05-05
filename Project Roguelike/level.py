import pygame as pg



class Level:
    def __init__(self):

        self.display_surface = pg.display.get_surface()



        self.visible_sprites = pg.sprite.Group()
        self.obstacles_sprites = pg.sprite.Group()

    def run(self):
        pass