import pygame as pg 
from random import randint, randrange
pg.init()

w, h, fps, level, step = 800, 800, 6, 0, 40
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Snake Game')
is_running, lose = True, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 20)
surf = pg.Surface((390, 390), pg.SRCALPHA)
bg = pg.image.load("images/background.jpg")
bg = pg.transform.scale(bg, (w, h))
gameover = pg.image.load("images/game_over.jpg")
gameover = pg.transform.scale(gameover, (390, 390))

class Food:
    def __init__(self):
        # Set random coordinates for food within the game window with a step of 40
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.pic = pg.image.load("images/cherry.png")

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

    def draw2(self):
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)

class Snake:
    def __init__(self):
        self.speed = step
        self.body = [[360, 360]]
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = (0, 255, 0)  # Green color

    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a and self.dx == 0:
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_d and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_w and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_s and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))
    
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.score += 1
            self.body.append([1000, 1000]) 
    
    def self_collide(self):
        global is_running
        if self.body[0] in self.body[1:]:
            lose = True 

    def check_food(self, f:Food): 
        if [f.x, f.y] in self.body:
            f.draw2() 

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pic = pg.image.load("images/wall.png")

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

s = Snake()
f = Food()

while is_running:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            is_running = False
        
    screen.blit(bg, (0, 0))

    my_walls = open(f'wall txt files/wall{level}.txt', 'r').readlines()
    walls = []
    for i, line in enumerate(my_walls):
        for j, each in enumerate(line):
            if each == "+":
                walls.append(Wall(j * step, i * step))

    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.self_collide()
    s.check_food(f)

    counter = score.render(f'Score: {s.score}', True, 'black')
    screen.blit(counter, (50, 50))
    l = score.render(f'Level: {level}', True, 'black')
    screen.blit(l, (50, 80))

    if s.score == 3:
        level += 1
        level %= 4 
        fps += 2
        s.score = 0

    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y:
            f.draw2()

        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
            lose = True

    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False   
        surf.blit(gameover, (0, 0))
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (320, 405))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (322, 435))
        pg.display.flip()

    pg.display.flip()
pg.quit()