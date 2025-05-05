import pygame as pg
import sys
from level import Level

#SETTINGS AND GAMELOOP/PAUSESTATE

pg.init()
WIDTH, HEIGHT = 800,400
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('BossBattle')
clock = pg.time.Clock()

class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
  
class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'
    def cleanup(self):
        print('cleaning up Menu state stuff')
    def startup(self):
        print('starting Menu state stuff')
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, win, dt):
        self.draw(win)
    def draw(self, win):
        win.fill((255,0,0))

class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
    def cleanup(self):
        print('cleaning up Game state stuff')
    def startup(self):
        print('starting Game state stuff')
        Level.run(self)
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Game State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, win, dt):
        self.draw(win)
    def draw(self, win):
        win.fill((0,0,255))

class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.win = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.win, dt)
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()

class Player():
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 32, 32)
        self.x = x
        self.y = y
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    def draw(self,win):
        pg.draw.rect(win, (self.color, self.rect))

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
            if self.down_pressed and not self.up_pressed:
                self.Y = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pg.Rect(self.x, self.y, 32, 32)

player = Player(200, 200)

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.left_pressed = True
            if event.key == pg.K_RIGHT:
                player.right_pressed = True
            if event.key == pg.K_UP:
                player.up_pressed = True
            if event.key == pg.K_DOWN:
                player.down_pressed = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.left_pressed = False
            if event.key == pg.K_RIGHT:
                player.right_pressed = False
            if event.key == pg.K_UP:
                player.up_pressed = False
            if event.key == pg.K_DOWN:
                player.down_pressed = False


win.fill((12, 24, 36))
player.draw(win)

player.update()
pg.display.flip()
  

settings = {
    'size':(600,400),
    'fps' :60
}

app = Control(**settings)
state_dict = {
    'menu': Menu(),
    'game': Game()
}
app.setup_states(state_dict, 'menu')
app.main_game_loop()
pg.quit()
sys.exit()