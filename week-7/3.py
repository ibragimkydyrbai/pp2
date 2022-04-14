import pygame

pygame.init()
screen = pygame.display.set_mode((1400, 700))
done = False
is_red = True
x = 700
y = 350


speend = 20

run = True
while run:
    screen.fill((255,255,255))
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >=50:
        x -= speend
    if keys[pygame.K_RIGHT] and x <= 1350:
        x +=speend
    if keys[pygame.K_UP] and y >= 50:
        y -= speend
    if keys[pygame.K_DOWN] and y <= 650:
        y += speend

    screen.fill((255,255,255))
    
    pygame.draw.circle(screen,(255,0,0),(x,y),25)
    pygame.display.update()
pygame.quit()