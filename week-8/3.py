import random, pygame
from math import*

# draw any shapes
class Shapes:
    def draw(self, screen, color, pos_mouse_0, pos_mouse_1):
        
        global RECT, SQUARE, LINE, CIRCLE, ELLIPSE
        
        self.screen = screen
        self.color = color
        
        # self.booleans = [RECT, SQUARE, LINE, CIRCLE, ELLIPSE]
        self.p0 = pos_mouse_0
        self.p1 = pos_mouse_1
        
        # x0 == x1 and y0 == y1
        if self.p0[0] == self.p1[0] and self.p0[1] == self.p1[1]:
            x0 = self.p0[0]
            y0 = self.p0[0]
            x1 = self.p1[0]
            y1 = self.p1[0]
        # x0 == x1 and y0 < y1
        elif self.p0[0] == self.p1[0] and self.p0[1] < self.p1[1]:
            x0 = self.p0[0]
            y0 = self.p0[1]
            x1 = self.p1[0]
            y1 = self.p1[1]
        # x0 == x1 and y0 > y1
        elif self.p0[0] == self.p1[0] and self.p0[1] > self.p1[1]:
            x0 = self.p1[0]
            y0 = self.p1[1]
            x1 = self.p0[0]
            y1 = self.p0[1]
        # y0 == y1 and x0 < x1
        elif self.p0[0] < self.p1[0] and self.p0[1] == self.p1[1]:
            x0 = self.p0[0]
            y0 = self.p0[1]
            x1 = self.p1[0]
            y1 = self.p1[1]
        # y0 == y1 and x0 > x1
        elif self.p0[0] > self.p1[0] and self.p0[1] == self.p1[1]:
            x0 = self.p1[0]
            y0 = self.p1[1]
            x1 = self.p0[0]
            y1 = self.p0[1]
        # x0 < x1 and y0 < y1
        elif self.p0[0] < self.p1[0] and self.p0[1] < self.p1[1]:
            x0 = self.p0[0]
            y0 = self.p0[1]
            x1 = self.p1[0]
            y1 = self.p1[1]
        # x0 > x1 and y0 < y1
        elif self.p0[0] > self.p1[0] and self.p0[1] < self.p1[1]:
            x0 = self.p1[0]
            y0 = self.p0[1]
            x1 = self.p0[0]
            y1 = self.p1[1]
        # x0 < x1 and y0 > y1
        elif self.p0[0] < self.p1[0] and self.p0[1] > self.p1[1]:
            x0 = self.p0[0]
            y0 = self.p1[1]
            x1 = self.p1[0]
            y1 = self.p0[1]
        # x0 > x1 and y0 > y1
        elif self.p0[0] > self.p1[0] and self.p0[1] > self.p1[1]:
            x0 = self.p1[0]
            y0 = self.p1[1]
            x1 = self.p0[0]
            y1 = self.p0[1]
        
        self.width = abs(x0 - x1)
        self.height = abs(y0 - y1)
        
        
        # draw rectangle
        if RECT:
            pygame.draw.rect(self.screen, self.color, (x0, y0, self.width, self.height), SIZE)
            
        # draw square
        elif SQUARE:
            pygame.draw.rect(self.screen, self.color, (x0, y0, max(self.height, self.width), max(self.height,self.width)), SIZE)
            
        # draw line
        elif LINE:
            pygame.draw.line(self.screen, self.color, min((x0, y0),(x1, y1)), max((x0, y0),(x1, y1)), SIZE)
        
        # draw circle
        elif CIRCLE:
            pygame.draw.circle(self.screen, self.color, (x0, y0), max(self.height, self.width), SIZE)
            
        # draw ellipse
        elif ELLIPSE:
            pygame.draw.ellipse(self.screen, self.color, (x0, y0, self.width, self.height), SIZE)
        
        pygame.display.update()
        clock.tick(FPS)

def draw(screen):
    
    # draw frame
    pygame.draw.rect(screen, (0), (350, 2, 150, 40))
    # draw rect
    pygame.draw.rect(screen, (COLORS[0]), (355, 10, 20, 25), 2)
    # draw square
    pygame.draw.rect(screen, (COLORS[1]), (385, 10, 25, 25), 2)
    # draw line
    pygame.draw.line(screen, (COLORS[2]), (420, 10), (420, 35), 3)
    # draw circle
    pygame.draw.circle(screen, (COLORS[3]), (445, 20), 15, 2)
    # draw ellipse
    pygame.draw.ellipse(screen, (COLORS[4]), (465, 10, 30, 25), 2)
    def pos(pos_mouse_0):
        global cur_color, PENCIL, ERASE, RECT, SQUARE, LINE, CIRCLE, ELLIPSE, SIZE
    # colors
        if 15 <= pos_mouse_0[0] <= 32 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[0] 
        elif 40 <= pos_mouse_0[0] <= 57 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[1] #
        elif 65 <= pos_mouse_0[0] <= 82 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[2]
        elif 90 <= pos_mouse_0[0] <= 107 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[3] #
        elif 115 <= pos_mouse_0[0] <= 132 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[4]
        elif 139 <= pos_mouse_0[0] <= 156 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[5]
        elif 164 <= pos_mouse_0[0] <= 180 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[6]
        elif 188 <= pos_mouse_0[0] <= 205 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[7]
        elif 213 <= pos_mouse_0[0] <= 230 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[8]
        elif 238 <= pos_mouse_0[0] <= 255 and 0 <= pos_mouse_0[1] <= 20:
            cur_color = COLORS[9]
        
        # size
        elif 270 <= pos_mouse_0[0] <= 276 and 0 <= pos_mouse_0[1] <= 20:
            SIZE += 1
            
        elif 284 <= pos_mouse_0[0] <= 299 and 0 <= pos_mouse_0[1] <= 20:
            SIZE -= 1
            
        # shapes
        elif 300 <= pos_mouse_0[0] <= 319 and 0 <= pos_mouse_0[1] <= 20:
            PENCIL = True
            ERASE =False
            RECT = False
            SQUARE = False
            LINE = False
            CIRCLE = False
            ELLIPSE = False
        elif 320 <= pos_mouse_0[0] <= 340 and 0 <= pos_mouse_0[1] <= 20:
            PENCIL = False
            ERASE = True
            RECT = False
            SQUARE = False
            LINE = False
            CIRCLE = False
            ELLIPSE = False
        elif 355 <= pos_mouse_0[0] <= 375 and 10 <= pos_mouse_0[1] <= 35:
            PENCIL = False
            ERASE = False
            RECT = True
            SQUARE = False
            LINE = False
            CIRCLE = False
            ELLIPSE = False
        elif 385 <= pos_mouse_0[0] <= 410 and 10 <= pos_mouse_0[1] <= 35:
            PENCIL = False
            ERASE = False
            RECT = False
            SQUARE = True
            LINE = False
            CIRCLE = False
            ELLIPSE = False
        elif 420 <= pos_mouse_0[0] <= 423 and 10 <= pos_mouse_0[1] <= 35:
            PENCIL = False
            ERASE = False
            RECT = False
            SQUARE = False
            LINE = True
            CIRCLE = False
            ELLIPSE = False
        elif 445 <= pos_mouse_0[0] <= 460 and 10 <= pos_mouse_0[1] <= 35:
            PENCIL = False
            ERASE = False
            RECT = False
            SQUARE = False
            LINE = False
            CIRCLE = True
            ELLIPSE = False
        elif 465 <= pos_mouse_0[0] <= 495 and 20 <= pos_mouse_0[1] <= 35:
            PENCIL = False
            ERASE = False
            RECT = False
            SQUARE = False
            LINE = False
            CIRCLE = False
            ELLIPSE = True
        # main function
    def main():
        global clock, COLORS, SIZE, FPS, cur_color, PENCIL, ERASE, RECT, SQUARE, LINE, CIRCLE, ELLIPSE, SIZE
        
        WIDTH = 600
        HEIGHT = 600
        FPS = 60
        PENCIL = False
        ERASE =False
        RECT = False
        SQUARE = False
        LINE = False
        CIRCLE = False
        ELLIPSE = False
        SIZE = 1
        COLORS = [(178,34,34), (255, 0, 0), (255,185,15), (255, 255, 0), (0, 255, 0), (0, 100, 0), (0,191,255), (0,104,139), (16,78,139), (75,0,130)]
        draw_on = False
        last_pos = (0, 0)
        DRAW_ON = False
        clock = pygame.time.Clock()
        
        # screen
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('simple paint')
        
        # button images
        image_color = pygame.image.load('images/colors.png').convert_alpha()
        image_color = pygame.transform.scale(image_color, (250, 20))
        image_plusANDminus = pygame.image.load('images/plus_minus.png').convert_alpha()
        image_plusANDminus = pygame.transform.scale(image_plusANDminus, (40, 20))
        image_pencil = pygame.image.load('images/pencil.png').convert_alpha()
        image_pencil = pygame.transform.scale(image_pencil, (20, 20))
        image_eraser = pygame.image.load('images/eraser.png').convert_alpha()
        image_eraser = pygame.transform.scale(image_eraser, (20, 20))
        
        # set of all images
        # current color
        cur_color = (0)
        images = [image_color, image_plusANDminus, image_pencil, image_eraser]
        
        
        # color_button = Button(COLORS, images, (0, 0))

        # mouse positions
        pos_mouse_0 = (0, 0)
        pos_mouse_1 = (0, 0)
        
        shapes = Shapes()
        
        font = pygame.font.SysFont('georgia', 30, True)
        text = font.render(f'Size: {SIZE}', True, (0))
        
        screen.fill((255, 255, 255))
        
        # blit color button image
        screen.blit(images[0], (10, 0))
        # blit plus and minus button image
        screen.blit(images[1], (260, 0))
        # blit pencil
        screen.blit(images[2], (300, 0))
        # blit eraser
        screen.blit(images[3], (320, 0))
        # main cycle
        done = False
        while not done:
            pressed = pygame.key.get_pressed()
            alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
            ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and ctrl_held or event.key == pygame.K_F4 and alt_held:
                        pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse_0 = event.pos
                    DRAW_ON = True
                    

                if event.type == pygame.MOUSEBUTTONUP:
                    
                    pos_mouse_1 = event.pos
                    if DRAW_ON:
                        pos(pos_mouse_0)
                        pos_mouse_1 = event.pos
                        shapes.draw(screen, cur_color, pos_mouse_0, pos_mouse_1)
                    DRAW_ON = False
                    
                    # draw_on = False
                    
                if event.type == pygame.MOUSEMOTION:
                    if PENCIL and DRAW_ON and event.pos[1] > 25:
                        pygame.draw.line(screen, cur_color, last_pos, event.pos, SIZE)
                    elif ERASE and DRAW_ON and event.pos[1] > 25:
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(event.pos[0] - SIZE // 2, event.pos[1] - SIZE// 2, SIZE * 3, 3 * SIZE),SIZE * 3)
                    last_pos = event.pos
                
                if pygame.mouse.get_pos()[1] > 25:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    
            text = font.render(f'Size: {SIZE}', True, (0))
            screen.fill((255, 255, 255), pygame.Rect(WIDTH - 100, 5, 100, 30))
            screen.blit(text, (WIDTH - 100, 5))

            pygame.display.flip()
            
            # draw all shapes at screen
            draw(screen)
            
            clock.tick(FPS)
        if __name__ == 'main':
            pygame.init()
            main()
            pygame.quit()