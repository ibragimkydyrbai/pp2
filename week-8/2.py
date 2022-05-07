import pygame, enum, random, time
from pygame.mixer import music

# constants
BLOCK_COLOR = (255, 0, 0)
WIDTH, HEIGHT = 600, 600
FPS = 10
BLOCK_SIZE = 10
COUNTER = 0

# class Block for snake head and body
class Block:
    def init(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        
    def draw(self):
        pygame.draw.rect(self.screen, BLOCK_COLOR, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))
        
        
    def collide(self, other):
        return self.x == other.x and self.y == other.y

class Direction(enum.Enum):
    up = 4
    down = 3
    left = 2
    right = 1

def menu(screen):
    
    # # booleans
    # play = False
    # about = False
    # exit = False
    # play : 185, 170 ; 215, 185
    
    image_menu = pygame.image.load('images/snake_menu.png')#.convert_alpha
    image_menu = pygame.transform.scale(image_menu, (WIDTH, HEIGHT))
    screen.blit(image_menu, (0, 0))
    pygame.display.update()
    
    going = True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 135 * 2 <= event.pos[0] <= 165 * 2 and 120 * 2 <= event.pos[1] <= 135 * 2:
                    going = False
                    return True
                if 130 * 2 <= event.pos[0] <= 170 * 2 and 145 * 2 <= event.pos[1] <= 155 * 2:
                    going = False
                    return False            
                if 185 * 2 <= event.pos[0] <= 215 * 2 and 215 * 2 <= event.pos[1] <= 225 * 2:
                    pygame.quit()

def main():
    
    pygame.init()
    global COUNTER, FPS
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake_game in 1989')
    
    clock = pygame.time.Clock()  
    
    head = Block(screen, 100, 100)
    body = [Block(screen, 100 - BLOCK_SIZE, 100), Block(screen, 100 - 2 * BLOCK_SIZE, 100)]
    food = Block(screen, 250, 250)
    
    direction = Direction.right
    
    FONT = pygame.font.SysFont('Arial', 20)
    FONT1 = pygame.font.SysFont('Arial', 17)
    text_score = FONT.render(f'score: {COUNTER * 5}', True, (0))
    text_speed = FONT.render(f'speed: {FPS}', True, (0))
    
    if menu(screen):
        going = True
        while going:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    going = False

            # events in keyboard buttons
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and direction != Direction.down:
                direction = Direction.up
            elif key[pygame.K_DOWN] and direction != Direction.up:
                direction = Direction.down
            elif key[pygame.K_LEFT] and direction != Direction.right:
                direction = Direction.left
            elif key[pygame.K_RIGHT] and direction != Direction.left:
                direction = Direction.right

            # defined that snake head collisioned with body
            for i in body:
                if head.collide(i):
                    pygame.mixer.music.load('sounds/crush.mp3')
                    pygame.mixer.music.play()
                    time.sleep(2)
                    going = False

            # defined that snakes and foods are collisioned
            if head.collide(food):          

                pygame.mixer.music.load('sounds/eating.mp3')
                pygame.mixer.music.play()


                COUNTER += 1
                if COUNTER % 3 == 0:
                    FPS += 1
                body.append(Block(screen, body[-1].x, body[-1].y))
                search = True
                # food.x = random.randint(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE
                # food.y = random.randint(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE
                while search:
                    food.x = random.randint(0, WIDTH // BLOCK_SIZE - 10) * BLOCK_SIZE
                    food.y = random.randint(0, HEIGHT // BLOCK_SIZE - 10) * BLOCK_SIZE
                    if head.collide(food):
                        continue
                    search = False
                    for i in body:
                        if i.collide(food):
                            search = True
                            break
                        
            # adding head in first position 
            body.insert(0, Block(screen, head.x, head.y))

            # delete last element in the body
            body.pop()

            # define (dx, dy) to snake
            if direction == Direction.up:      head.y -= BLOCK_SIZE         
            elif direction == Direction.down:  head.y += BLOCK_SIZE
            elif direction == Direction.left:  head.x -= BLOCK_SIZE
            elif direction == Direction.right: head.x += BLOCK_SIZE

            # walls
            if head.x - BLOCK_SIZE < 0:        
                going = False 
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()
            if head.x > HEIGHT - BLOCK_SIZE:   
                going = False
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()
            if head.y - BLOCK_SIZE < 0:        
                going = False
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()
            if head.y > WIDTH - BLOCK_SIZE:    
                going = False
                pygame.mixer.music.load('sounds/crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()

            # strings about score and speed
            text_score = FONT.render(f'score: {COUNTER * 5}', True, (0))
            text_speed = FONT.render(f'speed: {FPS}', True, (0))

            # we must fill screen
            screen.fill((255, 255, 255))

            # draw food
            food.draw()

            # draw head of the snake
            head.draw()

            # draw all body except head
            for i in body:
                i.draw()

            # output texts score and speed
            screen.blit(text_score, (5, 5))
            screen.blit(text_speed, (5, 25))

            # update the screen
            pygame.display.update()

            # FramePerSecond
            clock.tick(FPS)
        # close library pygame
        pygame.quit()
    
    else:
        screen.fill((25, 255, 25))
        about_image = pygame.image.load('images/about.png')
        about_image = pygame.transform.scale(about_image, (WIDTH, HEIGHT))
        text0 = 'Snake game'
        text1 = 'Inspired by zetcode.com Java 2D games'
        text2 = 'Snake is a video game that originated during the late 1970s in arcades becoming'
        text3 = 'something of a classic. It became the standard pre-loaded game'
        text4 = 'on Nokia phones in 1998.'
        text5 = 'The player controls a long, thin creature,'
        text6 = 'resembling a snake, which roams around on'
        text7 = 'a bordered plane, picking up food (or some'
        text8 = 'other item), trying to avoid hitting its own tail'
        text9 = 'or the edges of the playing area. Each time'
        text10 = 'the snake eats a piece of food, its tail grows'
        text11 = 'longer, making the game increasingly'
        text12 = 'difficult. The user controls the direction of'
        text13 = "the snake's head (up, down, left, or right),"
        text14 = "and the snake's body follows."
        text = [text0, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14]
    
        # text_about = FONT1.render(f'More Information: \n{text}', True, (255, 0, 0))
    
        text_exit = FONT.render('EXIT', True, (0, 0, 0))
        text_about = FONT.render('More Information:', True, (0, 0, 255))
        screen.blit(about_image, (0, 0))
        screen.blit(text_about, (10, 10))
        
        going = True
        while going:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    going = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 500 <= event.pos[0] <= 520 and 540 <= event.pos[1] <= 560:
                        main()
            
            for i in range(15):
                text_about = FONT1.render(f'{text[i]}', True, (0, 0, 0))
                screen.blit(text_about, (15, 15 + (i + 1) * 30))
            
            screen.blit(text_exit, (500, 540))
            pygame.display.update()
            clock.tick(FPS)
        
    pygame.quit()

if __name__ == 'main':
    main()