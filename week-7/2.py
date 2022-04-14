import pygame 
pygame.init()

l = [r"Khalid_Billie_Eilish_-_lovely_55441014.mp3",r"ACRAZE_Cherish_-_Do_It_To_It_73392500.mp3",r"EQRIC_Bottle_Flip_-_Love_You_Like_A_Love_Song_70360113.mp3"]

screen = pygame.display.set_mode((360, 360))

screen2 = pygame.image.load('og_image.jpg')

run = True
pos = 0


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if pos <= 2:
                pos+=1
            else:
                pos = 0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if pos >= 1:
                pos-=1
            else:
                pos = 3
            pygame.mixer.music.stop()
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
    screen.blit(screen2,(0,0))

    pygame.display.flip()
pygame.quit()