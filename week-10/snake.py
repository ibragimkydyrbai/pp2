# Importing libraries
import pygame as pg
from random import *
from functions import *

# Setting up dimensions
KLETKA = 20
N, M = 30, 20
dim = W, H = KLETKA * N, KLETKA * M
bcg = pg.image.load('levels/Level 1.jpg')


# Dictionary that stores data corresponding to each level
levels = {
    # level and cooresponding speed and score
    1: (200, 10),
    2: (175, 15),
    3: (150, 20),
    4: (125, 25),
    5: (100, 30),
    6: (75, 35),
    7: (50, 40)    
}

# Create walls consisting levels
def check_walls(screen):
    walls = []
    for i in range(N):
        for j in range(M):
            a = screen.get_at((i * KLETKA + 2, j * KLETKA + 2))
            if a[0] < 20 and a[1] < 20 and a[2] < 20:
                walls.append([i, j])    
    return walls


walls_pos = check_walls(bcg)

# Generate random position for food
def random_pos(snake_pos: list):
    x, y = randint(0, N - 1), randint(0, M - 1)
    
    # Check if food position is in snake list
    if snake_pos.count([x, y]) or walls_pos.count([x, y]):
        return random_pos(snake_pos)
    return [x, y]
    
# Class for food
class Food(pg.sprite.Sprite):
    # Initialize food image, score and position
    def init(self, image, score, snake_pos):
        super().init()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = random_pos(snake_pos)
        self.score = score
    
    # Draw our food
    def draw(self, sc):
        self.rect.topleft = (self.pos[0] * KLETKA, self.pos[1] * KLETKA)
        sc.blit(self.image, self.rect)

# Class for snake 
class Snake:
    # Inintialize snake position
    def init(self):
        self.pos = [[1, 1]]
        self.dir = 0
        self.size = 1
       
        
    # Move snake position
    def move(self):
        # Rewrite snake positions
        if len(self.pos) > 1:
            for i in range(self.size - 1, 0, -1):

                self.pos[i][0] = self.pos[i -1][0]
                self.pos[i][1] = self.pos[i -1][1]
        
        # Dir 1 for UP, Dir 2 for RIGHT, Dir 3 for DOWN, Dir 4 for LEFT
        if self.dir == 1: self.pos[0][1] -= 1  
        if self.dir == 2: self.pos[0][0] += 1 
        if self.dir == 3: self.pos[0][1] += 1 
        if self.dir == 4: self.pos[0][0] -= 1

        # Travel to another side
        if self.pos[0][0] > N: self.pos[0][0] = 0
        if self.pos[0][0] < 0: self.pos[0][0] = N
        if self.pos[0][1] > M: self.pos[0][1] = 0
        if self.pos[0][1] < 0: self.pos[0][1] = M
    
    # Check if food
    def check_food(self, Foods):
        for f in Foods:
            if f.pos[0] == self.pos[0][0] and f.pos[1] == self.pos[0][1]:
                self.size += f.score
                for i in range(f.score): self.pos.append([-1, -1])
                f.pos = random_pos(self.pos)
                f.image = choice(images)
                return f.score
            return 0
        
    def draw(self, scr):
        for i in range(self.size):
            x, y = self.pos[i][0] * KLETKA, self.pos[i][1] * KLETKA
            pg.draw.rect(scr, (255, 0, 0), pg.Rect(x, y, KLETKA, KLETKA))
    
    def collide(self, walls):
        # for i in walls:
        #     if self.pos.count(i) > 0:
        #         return True
        # return False
        if walls.count(self.pos[0]) or self.pos[1:].count(self.pos[0]):
            return True
        return False
        
# Driver code
def main():
    # Setting up dimensions and screen
    scr = pg.display.set_mode(dim)
    
    # Initialize snake, SPEED
    def init(lvl):
        global snake, SPEED, food, Foods, max_score, bcg, walls_pos, images
        bcg = pg.image.load(f'levels/Level {lvl}.jpg')
        walls_pos = check_walls(bcg)
        # Creating snake
        snake = Snake()
        
        ld = lambda name: pg.transform.scale((pg.image.load(f"images/{name}.png").convert_alpha()), (KLETKA, KLETKA))
        images = [ld('apple'), ld('ananas'), ld('banana'), ld('orik'), ld('zhusim')]
        food = Food(choice(images), 1, [1 ,1])
        Foods = pg.sprite.Group([food])
        SPEED = pg.USEREVENT + 1
        pg.time.set_timer(SPEED, levels[lvl][0])
        max_score = levels[lvl][1]
        
        
    # Making colors
    WHITE = (255, 255, 255)
    
    # Setting up fonts
    font = pg.font.SysFont('georgia', 15, True)
    
    # Variables
    initialize = False
    MENU = True
    LOGIN = False
    SCORE = 0
    level = 1
    name = ''
    
    image_login = pg.image.load('images/login.jpg').convert()
    image_menu = pg.image.load('images/snake_menu.jpg').convert()
    image_login = pg.transform.scale(image_login, dim)    
    image_menu = pg.transform.scale(image_menu, dim)    
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    
    while going:
        if MENU:
            scr.blit(image_menu, (0, 0))
            p = lambda pos: 264 < pos[0] < 315 and 169 < pos[1] < 183
            exit = lambda pos: 272 < pos[0] < 307 and 217 < pos[1] < 229
            l = lambda pos: 265 < pos[0] < 314 and 244 < pos[1] < 254
            
            for e in pg.event.get():
                # Quit
                if e.type == pg.QUIT:
                    going = False
                if e.type == pg.MOUSEBUTTONDOWN:
                    
                    if p(e.pos):
                        MENU = False
                        initialize = True
                    elif l(e.pos):
                        LOGIN = True
                        MENU = False
                        name = ''
                    elif exit(e.pos):
                        going = False
                        
            
        elif LOGIN:
            scr.blit(image_login, (0, 0))
            
            for e in pg.event.get():
                # Quit
                if e.type == pg.QUIT:
                    going = False
                    
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_RETURN:
                        LOGIN = False
                        MENU = True
                        a = view(name)
                        if len(a):
                            SCORE = a[0][1]
                            level = a[0][2]
                        else:
                            InsertData(name)
                    elif e.key == pg.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 20:
                        name += e.unicode
            text = font.render(name, True, 0)    
            scr.blit(text, (212, 186))
        else:
            pg.display.set_caption(f'level: {level}')
        
            # Initialize the game objects
            if initialize:
                initialize = False
                init(level)
            # Fill screen with white color
            scr.blit(bcg, (0, 0))
            
            if SCORE == levels[level][1]:
                SCORE = 0
                level += 1
                init(level)
            
            # Loop through the events
            for e in pg.event.get():
                # Quit
                if e.type == pg.QUIT:
                    going = False
                    
                # Move snake after some time
                if e.type == SPEED:
                    snake.move()
                    
                # Change directon only if snake located in the screen
                if (e.type == pg.KEYDOWN and
                    snake.pos[0][0] < N and snake.pos[0][0] >= 0 and snake.pos[0][1] < M and snake.pos[0][1] >= 0
                    ):
                    if e.key == pg.K_ESCAPE: MENU =True
                    if e.key == pg.K_UP and snake.dir != 3:    snake.dir = 1
                    if e.key == pg.K_RIGHT and snake.dir != 4: snake.dir = 2
                    if e.key == pg.K_DOWN and snake.dir != 1:  snake.dir = 3
                    if e.key == pg.K_LEFT and snake.dir != 2:  snake.dir = 4
                    
            
            
            # Check if the snake eated our food
            SCORE += snake.check_food(Foods)
            
            if snake.collide(walls_pos):
                going = False
            
            # Creating score text
            text_score = f'{SCORE} \ {max_score}'
            text_score = font.render(text_score, True, 0)
            
            # Draw the snake and food
            snake.draw(scr)
            
            for f in Foods: f.draw(scr)      
            scr.blit(text_score, (10, 10))

            
        # Tick and flip
        pg.display.flip()
        fps.tick(60)
            
    if len(name): ChangeData(name, SCORE, level)

# Launcher code
if name == 'main':
    pg.init()
    main()
    pg.quit()