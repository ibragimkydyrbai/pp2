# import libraries
import pygame, os, random, time
from pygame.mixer import music


# function that creates menu page
def menu(playb, exitb, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if playb.pressed(event.pos):
            music.stop()
            return 'PLAY'
        elif exitb.pressed(event.pos):
            return 'EXIT'
    else:
        return 'WAIT'

# defined that button is klicked
class Button(pygame.sprite.Sprite):
    def init(self, image, pos):
        super().init()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def pressed(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# creates objects: coin and enemy
class Object(pygame.sprite.Sprite):
    def init(self, x, speed, image, score, group):
        pygame.sprite.Sprite.init(self)
        self.image = image
        self.score = score
        self.rect = self.image.get_rect(center = (x, 0))
        self.speed = speed
        self.add(group) 
        
    def update(self, *args):
        if self.rect.y < args[0]:
            self.rect.y += self.speed
        else:
            self.kill()

# создание случайного монеты
def createCoin(group, coin_surf):
    x = random.randint(30, 370)
    return Object(x, speed, coin_surf, score, group)

# создание случайного приграды
def createPregrades(group, image_pregrada):
    x = random.randint(70, 330)
    return Object(x, speed, image_pregrada, score, group)

# узнать соприкасновение монеты и приграды на машину
def collideCoin(car_rect):  
    global game_score
    for coin in coins:
        if car_rect.collidepoint(coin.rect.bottomleft) or car_rect.collidepoint(coin.rect.bottomright):
            game_score += score
            pygame.mixer.Sound('sounds/coin.mp3').play()
            coin.kill()
            global cnt, speed
            cnt += 1
            if cnt % 5 == 0:
                speed += 1
    for pregrada in pregrades:
        if car_rect.collidepoint(pregrada.rect.bottomleft) or car_rect.collidepoint(pregrada.rect.bottomright) or car_rect.collidepoint(pregrada.rect.center):
            game_score -= score
            pygame.mixer.Sound('sounds/pregrada.mp3').play()
            global play
            play = True
            global life
            life -= 1
            pregrada.kill()

def move(car_pos, speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_pos.x -= speed
    if keys[pygame.K_RIGHT]:
        car_pos.x += speed
    if keys[pygame.K_UP]:
        car_pos.y -= speed
    if keys[pygame.K_DOWN]:
        car_pos.y += speed
    if car_pos.x < 0:
        car_pos.x = 0
    if car_pos.x > w - 44:
        car_pos.x = w - 44
    if car_pos.y < 0:
        car_pos.y = 0
    if car_pos.y > h - 96:
        car_pos.y = h - 96
    return car_pos


def main():
    global w, h
    w, h = 600, 600
    sc = pygame.display.set_mode((w, h))
    
    pygame.time.set_timer(pygame.USEREVENT, 2000)
    pygame.time.set_timer(pygame.USEREVENT_DROPFILE, 5000)
    
    image_play = pygame.image.load('images/play.png')
    image_play = pygame.transform.scale(image_play, (300, 100))
    image_road = pygame.image.load('images/road.png')
    image_road = pygame.transform.scale(image_road, (w, h))
    image_exit = pygame.image.load('images/exit.png')
    image_exit = pygame.transform.scale(image_exit, (300, 100))
    
    # внешний экран
    image_car = pygame.image.load('images/Player.png')
    car_rect = image_car.get_rect(centerx=w//2, bottom = h - 5)
    image_pregrada = pygame.image.load('images/Enemy.png')
    # image_pregrada = pygame.transform.scale(image_pregrada, (50, 50))
    image_coin = pygame.image.load('images/coin.png')
    image_coin = pygame.transform.scale(image_coin, (30, 30))

    playb = Button(image_play, (300, 370))
    exitb = Button(image_exit, (300,480))
    
    # скачать все песни
    global musics
    musics = ['musics/' + x for x in os.listdir('musics')]
    # сохранить пределы всех музыки в наборе

    
    # constants
    global size, curm, life, clock, FPS, cnt, speed, score, game_score, coins, pregrades, play
    size = len(musics)
    curm = 0
    life = 3
    sc = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    FPS = 60
    cnt = 1
    speed = 3
    score = 25
    game_score = 0
    
    # главный экран
    image_page = pygame.image.load('images/first_page.png')
    image_page = pygame.transform.scale(image_page, (w, h))
    image_end = pygame.image.load('images/end.png')
    image_end = pygame.transform.scale(image_end, (w, h))
    
    # создание класса монет и приград
    coins = pygame.sprite.Group()
    pregrades = pygame.sprite.Group()

    # скачать экран дорогиz
    bg = pygame.image.load('images/road.png')
    bg = pygame.transform.scale(bg, (w, h))

    # создать первую монету
    createCoin(coins, image_coin)

    # определить стили текстов
    style = pygame.font.SysFont('serif', 30)
    style1 = pygame.font.SysFont('Arial', 30)
    style2 = pygame.font.SysFont('georgia', 30)
            
    lt = ''
    text_score = style.render(f'score: {game_score}', True, (255, 255, 255))
    text_life = style1.render(f'life: {lt}', True, (255, 255, 255))
    PLAY = False
    EXIT = False
    MENU = True
    Next = False
    
    pygame.display.update()
    going = True
    while going:
        
        if MENU or life == 0:
            f_score = open('RECORD_SCORE')
            h_score = f_score.readline()
            f_score.close()
        
            text_hight = style2.render(h_score, True, (0))
        
            if life == 0:
                sc.blit(image_end, (0, 0))
                pygame.display.flip()
                if not music.get_busy():
                    music.load('sounds/game_over.wav')
                    music.play()
                
                time.sleep(4)
                life = 3
                
            if not music.get_busy():
                music.load('sounds/menu_msc.mp3')
                music.play()
                
            sc.blit(image_page, (0, 0))
            sc.blit(playb.image, playb.rect)
            sc.blit(exitb.image, exitb.rect)
            pygame.display.flip()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if menu(playb, exitb, event) == 'PLAY':
                    PLAY = True
                    MENU = False
                    
                    break
                elif menu(playb, exitb, event) == 'EXIT': EXIT = True
            if PLAY:       
                if not music.get_busy():
                    music.load(musics[curm % size])
                    music.play()
                
            if Next:
                Next = False    
                curm += 1
                music.load(musics[curm % size])
                music.play()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if event.type == pygame.USEREVENT:
                    createCoin(coins, image_coin)
        
                if event.type == pygame.USEREVENT_DROPFILE:
                    createPregrades(pregrades, image_pregrada)
             
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    Next = True
                            
            car_rect = move(car_rect, speed)
            
            collideCoin(car_rect)
            lt = h * life // 600
            text_score = style.render(f'score: {game_score}', True, (255, 255, 255))
            text_life = style1.render(f'life: {lt}', True, (255, 255, 255))
            text_hight = style2.render(f'record_score: {h_score}', True, (0))
            sc.blit(bg, (0, 0))
            coins.draw(sc)
            pregrades.draw(sc)
            sc.blit(image_car, (car_rect.x, car_rect.y))
            sc.blit(text_score, (50, 0))
            sc.blit(text_life, (500, 0))
            sc.blit(text_hight, (225, 0))
            pygame.display.update()
            clock.tick(FPS)
            coins.update(h)
            pregrades.update(h)
            
            if life == 0:
                
                music.stop()
                PLAY = False
                MENU = True
                if game_score > int(h_score):
                    f_score = open('RECORD_SCORE', 'w')
                    f_score.write(str(game_score))
                    f_score.close()
                    
        elif EXIT:
            going = False
        
if __name__ == 'main':
    pygame.init()
    pygame.mixer.init()
    main()
    pygame.quit()