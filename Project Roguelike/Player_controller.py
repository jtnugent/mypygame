import pygame as pg
import sys
import time


pg.init()
WIDTH, HEIGHT = 400 , 400
TITLE = "Meh"
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()



class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        velX = 0
        velY = 0
        self.rect = pg.Rect(x, y, 32, 32)
        self.x = int(x)
        self.y = int(y)
        self.color = (250, 120, 60)
        self.velX = velX
        self.velY = velY
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.dash_pressed = False
        self.speed = 3
    
    def draw(self,win):
        pg.draw.rect(win, self.color, self.rect)

    def update(self):
        if self.dash_pressed == False:
            self.velX = 0
            self.velY = 0
            if self.left_pressed and not self.right_pressed:
                self.velX = -self.speed
            if self.right_pressed and not self.left_pressed:
                self.velX = self.speed
            if self.up_pressed and not self.down_pressed:
                self.velY = -self.speed
            if self.down_pressed and not self.up_pressed:
                self.velY = self.speed



            self.x += self.velX
            self.y += self.velY

            self.rect = pg.Rect(int(self.x), int(self.y), 32, 32)

    def dash(self):
        print("dash detected")
        dash_pressed = True
        self.velX = 0
        self.dash_pressed = dash_pressed
        for i in range(50):
            #Draw
            win.fill((12, 24, 36))
            player.draw(win)

            #update
            player.update()
            pg.display.flip()
            clock.tick(400)
        self.dash_pressed = False
        self.velX = 0
        self.velY = 0


player = Player(WIDTH/2, HEIGHT/2)

dash_timer = 2
start_time = 0
last_key_pressed = ""
p = Player(0,0)

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit( )
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.left_pressed = True
                last_key_pressed = "left"
            if event.key == pg.K_RIGHT:
                player.right_pressed = True
                last_key_pressed = "right"
            if event.key == pg.K_UP:
                player.up_pressed = True
                last_key_pressed = "up"
            if event.key == pg.K_DOWN:
                player.down_pressed = True
                last_key_pressed = "down"
            if event.key == pg.K_w:
                p.dash()

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.left_pressed = False
            if event.key == pg.K_RIGHT:
                player.right_pressed = False
            if event.key == pg.K_UP:
                player.up_pressed = False
            if event.key == pg.K_DOWN:
                player.down_pressed = False
            
        

    #Draw
    win.fill((12, 24, 36))
    player.draw(win)

    #update
    player.update()
    pg.display.flip()
    clock.tick(120)
