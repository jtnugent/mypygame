import pygame as pg
from settings import * 
import sys

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        last_key_pressed = ""
        self.last_key_pressed = last_key_pressed
        super().__init__(groups)
        self.image = pg.image.load("Project Roguelike\Sprites\Cat.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pg.math.Vector2()
        self.speed = 5
        dash_ready = True
        self.dash_ready = dash_ready
        
    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.last_key_pressed = "up"
            self.direction.y =  -1
        elif keys[pg.K_DOWN]:
            self.last_key_pressed = "down"
            self.direction.y = 1
        else:
            self.direction.y = 0


        if keys[pg.K_RIGHT]:
            self.last_key_pressed = "right"
            self.direction.x =  1
        elif keys[pg.K_LEFT]:
            self.last_key_pressed = "left"
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pg.K_SPACE]:
            if self.dash_ready == True:
                self.dash()

    def move(self, speed):
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)

    def dash(self):
        self.dash_ready = False
        if self.last_key_pressed == "right":
            for i in range(1):
                self.direction.x += 3
            



