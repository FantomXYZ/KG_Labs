import pygame
import numpy as np
import pygame
import numpy as np
import time


WINDOW_WIDTH = 1560
WINDOW_HEIGHT = 750

BG_COLOR = (255,255,255)
LINE_COLOR = (0,0,0)
BUTTONS_COLOR = (180, 163, 247)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)




def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy

    points = []
    while x0 != x1 or y0 != y1:
        points.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    points.append((x0, y0))
    return points

def step_line(x0,y0,x1,y1):
    points = []
    
    Dx = x1-x0
    Dy = y1-y0
    
    k = Dy/Dx
    
    b = y1 - k*x1
    delta = 0.01
    
    
    if x0<x1:
        i = x0
        while i+delta < x1:
            y = k*i + b
            print(i)
            print(y)
            i += delta
            
            points.append((round(i),round(y)))
    else:
        i = x1
        while i+delta < x0:
            y = k*i + b
            i += delta
            
            points.append((round(i),round(y)))        
    
    return points


def window():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Lines")
    
    clock = pygame.time.Clock()
    global running
    running = True
    
    global SCALE
    
    SCALE = 20
    
    global x0
    global y0
    global x1
    global y1
        
    x0 = 12
    y0 = 8
        
    x1 = -4
    y1 = -10
        
    global points1
    global points2
        
    points1 = []
    points2 = []
    
    global t1
    global t2
    t1 = 0
    t2 = 0
    
    
    while running:
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 20 <= mouse_pos[0] <= 220 and 10 <= mouse_pos[1] <= 60:
                    #print(time.monotonic_ns())
                    start = time.time()
                    points2 = bresenham_line(x0,y0,x1,y1)
                    t2 = time.time() - start
                    
                    start = time.time()
                    points1 = step_line(x0,y0,x1,y1)
                    t1 = time.time() - start
                    #print(time.monotonic_ns())
                    
                    print("Bres points:")
                    for i in points2:
                        print(i)
                    print("=================================")
                    print("Step points:")
                    for i in points1:
                        print(i)
                    print("=================================")
                    
                    
                elif 500 <= mouse_pos[0] <= 530 and 10 <= mouse_pos[1] <= 40:
                    x0 += 1
                elif 500 <= mouse_pos[0] <= 530 and 45 <= mouse_pos[1] <= 75:
                    x0 -= 1
                elif 630 <= mouse_pos[0] <= 660 and 10 <= mouse_pos[1] <= 40:
                    y0 += 1
                elif 630 <= mouse_pos[0] <= 660 and 45 <= mouse_pos[1] <= 75:
                    y0 -= 1
                
                elif 675 <= mouse_pos[0] <= 705 and 10 <= mouse_pos[1] <= 40:
                    x1 += 1
                elif 675 <= mouse_pos[0] <= 705 and 45 <= mouse_pos[1] <= 75:
                    x1 -= 1
                elif 805 <= mouse_pos[0] <= 835 and 10 <= mouse_pos[1] <= 40:
                    y1 += 1
                elif 805 <= mouse_pos[0] <= 835 and 45 <= mouse_pos[1] <= 75:
                    y1 -= 1
                elif 1205 <= mouse_pos[0] <= 1235 and 10 <= mouse_pos[1] <= 40:
                    SCALE += 4
                    
                elif 1205 <= mouse_pos[0] <= 1235 and 45 <= mouse_pos[1] <= 75:
                    if SCALE != 4:
                        SCALE -= 4
    
    
        window.fill(BG_COLOR)
        
        i = 0
        while i <= WINDOW_WIDTH//2:
            pygame.draw.line(window,LINE_COLOR,(i,90),(i,WINDOW_HEIGHT))
            i += SCALE
            
        i = WINDOW_WIDTH//2
        while i <= WINDOW_WIDTH:
            pygame.draw.line(window,LINE_COLOR,(i,90),(i,WINDOW_HEIGHT))
            i += SCALE
            
        i = 90
        while i <= WINDOW_HEIGHT:
            pygame.draw.line(window,LINE_COLOR,(0,i),(WINDOW_WIDTH,i))
            i += SCALE    
        
        x_cells_count = (WINDOW_WIDTH//2)//SCALE
        y_cells_count = (WINDOW_HEIGHT-90)//SCALE
        
        step_center_x = x_cells_count//2*SCALE + SCALE//2
        baze_center_x = step_center_x + WINDOW_WIDTH//2
        center_y = (y_cells_count//2)*SCALE + 90 + SCALE//2
        
        draw_points(window,points1,points2,step_center_x,baze_center_x,center_y,SCALE)
        
        pygame.draw.line(window,LINE_COLOR,(0,90),(WINDOW_WIDTH,90))
        
        
        
        pygame.draw.line(window,BLUE,(step_center_x,90),(step_center_x,WINDOW_HEIGHT),3)
        pygame.draw.line(window,BLUE,(step_center_x,90),(step_center_x-SCALE//2,90+SCALE//2),3)
        pygame.draw.line(window,BLUE,(step_center_x,90),(step_center_x+SCALE//2,90+SCALE//2),3)
        
        pygame.draw.line(window,BLUE,(baze_center_x,90),(baze_center_x,WINDOW_HEIGHT),3)
        pygame.draw.line(window,BLUE,(baze_center_x,90),(baze_center_x-SCALE//2,90+SCALE//2),3)
        pygame.draw.line(window,BLUE,(baze_center_x,90),(baze_center_x+SCALE//2,90+SCALE//2),3)
        
        pygame.draw.line(window,GREEN,(0,center_y),(WINDOW_WIDTH,center_y),3)
        
        pygame.draw.line(window,GREEN,(WINDOW_WIDTH//2-SCALE//2,center_y-SCALE//2),(WINDOW_WIDTH//2,center_y),3)
        pygame.draw.line(window,GREEN,(WINDOW_WIDTH//2-SCALE//2,center_y+SCALE//2),(WINDOW_WIDTH//2,center_y),3)
        pygame.draw.line(window,GREEN,(WINDOW_WIDTH-SCALE//2,center_y-SCALE//2),(WINDOW_WIDTH,center_y),3)
        pygame.draw.line(window,GREEN,(WINDOW_WIDTH-SCALE//2,center_y+SCALE//2),(WINDOW_WIDTH,center_y),3)
        
        pygame.draw.line(window,RED,(WINDOW_WIDTH//2,90),(WINDOW_WIDTH//2,WINDOW_HEIGHT),3)
        
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(window, BG_COLOR, (260,10, 220, 30))
        text1 = font.render("Step time: " + str(t1)[:6], True, (0,0,0))
        text_rect1 = text1.get_rect(center=(260 + 220 // 2, 10 + 30 // 2))
        window.blit(text1, text_rect1)
        
        pygame.draw.rect(window, BG_COLOR, (260,35, 220, 30))
        text2 = font.render("Baze time: " + str(t2)[:6], True, (0,0,0))
        text_rect2 = text2.get_rect(center=(260 + 220 // 2, 35 + 30 // 2))
        window.blit(text2, text_rect2)
        
        pygame.draw.rect(window, BG_COLOR, (535,20, 50, 50))
        text2 = font.render(str(x0), True, (0,0,0))
        text_rect2 = text2.get_rect(center=(535 + 50 // 2, 20 + 50 // 2))
        window.blit(text2, text_rect2)
        
        pygame.draw.rect(window, BG_COLOR, (575,20, 50, 50))
        text2 = font.render(str(y0), True, (0,0,0))
        text_rect2 = text2.get_rect(center=(575 + 50 // 2, 20 + 50 // 2))
        window.blit(text2, text_rect2)
        
        pygame.draw.rect(window, BG_COLOR, (710,20, 50, 50))
        text2 = font.render(str(x1), True, (0,0,0))
        text_rect2 = text2.get_rect(center=(710 + 50 // 2, 20 + 50 // 2))
        window.blit(text2, text_rect2)
        
        pygame.draw.rect(window, BG_COLOR, (750,20, 50, 50))
        text2 = font.render(str(y1), True, (0,0,0))
        text_rect2 = text2.get_rect(center=(750 + 50 // 2, 20 + 50 // 2))
        window.blit(text2, text_rect2)
        
        pygame.draw.rect(window, BG_COLOR, (1250,20, 50, 50))
        text2 = font.render(str(SCALE), True, (0,0,0))
        text_rect2 = text2.get_rect(center=(1250 + 50 // 2, 20 + 50 // 2))
        window.blit(text2, text_rect2)
        
        
        draw_buttons(window)
        pygame.display.flip()
        
        

def draw_points(window,points1,points2,step_center_x,baze_center_x,center_y,SCALE):
    #pygame.draw.rect(window,LINE_COLOR,(0,90,20,20))
    
    
    for x,y in points1:
        if x==0 and y==0:
            pygame.draw.rect(window,LINE_COLOR,(step_center_x-SCALE//2,center_y-SCALE//2,SCALE,SCALE))
        elif x==0:
            pygame.draw.rect(window,LINE_COLOR,(step_center_x-SCALE//2,center_y-SCALE//2-y*SCALE,SCALE,SCALE))
        elif y==0:
            pygame.draw.rect(window,LINE_COLOR,(step_center_x-SCALE//2+x*SCALE,center_y-SCALE//2,SCALE,SCALE))    
        elif x>0 and y>0:
            pygame.draw.rect(window,LINE_COLOR,(step_center_x+SCALE//2+(x-1)*SCALE,center_y-SCALE//2-(y)*SCALE,SCALE,SCALE))     
        elif x<0 and y<0:
            pygame.draw.rect(window,LINE_COLOR,(step_center_x-SCALE//2+(x)*SCALE,center_y+SCALE//2-(y+1)*SCALE,SCALE,SCALE))
        elif x<0 and y>0:
            pygame.draw.rect(window,LINE_COLOR,(step_center_x-SCALE//2+(x)*SCALE,center_y-SCALE//2-(y)*SCALE,SCALE,SCALE))
        elif x>0 and y<0:
            pygame.draw.rect(window,LINE_COLOR,(step_center_x+SCALE//2+(x-1)*SCALE,center_y+SCALE//2-(y+1)*SCALE,SCALE,SCALE))
    
    for x,y in points2:
        if x==0 and y==0:
            pygame.draw.rect(window,LINE_COLOR,(baze_center_x-SCALE//2,center_y-SCALE//2,SCALE,SCALE))
        elif x==0:
            pygame.draw.rect(window,LINE_COLOR,(baze_center_x-SCALE//2,center_y-SCALE//2-y*SCALE,SCALE,SCALE))
        elif y==0:
            pygame.draw.rect(window,LINE_COLOR,(baze_center_x-SCALE//2+x*SCALE,center_y-SCALE//2,SCALE,SCALE))    
        elif x>0 and y>0:
            pygame.draw.rect(window,LINE_COLOR,(baze_center_x+SCALE//2+(x-1)*SCALE,center_y-SCALE//2-(y)*SCALE,SCALE,SCALE))     
        elif x<0 and y<0:
            pygame.draw.rect(window,LINE_COLOR,(baze_center_x-SCALE//2+(x)*SCALE,center_y+SCALE//2-(y+1)*SCALE,SCALE,SCALE))
        elif x<0 and y>0:
            pygame.draw.rect(window,LINE_COLOR,(baze_center_x-SCALE//2+(x)*SCALE,center_y-SCALE//2-(y)*SCALE,SCALE,SCALE))
        elif x>0 and y<0:
            pygame.draw.rect(window,LINE_COLOR,(baze_center_x+SCALE//2+(x-1)*SCALE,center_y+SCALE//2-(y+1)*SCALE,SCALE,SCALE))

def draw_buttons(window):
    pygame.draw.rect(window, BUTTONS_COLOR, (20,10, 220, 65))
    font = pygame.font.Font(None, 36)
    text = font.render("Нарисовать", True, (0,0,0))
    text_rect = text.get_rect(center=(20 + 200 // 2, 10 + 70 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (500,10, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("+", True, (0,0,0))
    text_rect = text.get_rect(center=(500 + 30 // 2, 10 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (500,45, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("-", True, (0,0,0))
    text_rect = text.get_rect(center=(500 + 30 // 2, 45 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (630,10, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("+", True, (0,0,0))
    text_rect = text.get_rect(center=(630 + 30 // 2, 10 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (630,45, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("-", True, (0,0,0))
    text_rect = text.get_rect(center=(630 + 30 // 2, 45 + 30 // 2))
    window.blit(text, text_rect)
    
    
    
    pygame.draw.rect(window, BUTTONS_COLOR, (675,10, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("+", True, (0,0,0))
    text_rect = text.get_rect(center=(675 + 30 // 2, 10 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (675,45, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("-", True, (0,0,0))
    text_rect = text.get_rect(center=(675 + 30 // 2, 45 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (805,10, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("+", True, (0,0,0))
    text_rect = text.get_rect(center=(805 + 30 // 2, 10 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (805,45, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("-", True, (0,0,0))
    text_rect = text.get_rect(center=(805 + 30 // 2, 45 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (1205,10, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("+", True, (0,0,0))
    text_rect = text.get_rect(center=(1205 + 30 // 2, 10 + 30 // 2))
    window.blit(text, text_rect)
    
    pygame.draw.rect(window, BUTTONS_COLOR, (1205,45, 30, 30))
    font = pygame.font.Font(None, 36)
    text = font.render("-", True, (0,0,0))
    text_rect = text.get_rect(center=(1205 + 30 // 2, 45 + 30 // 2))
    window.blit(text, text_rect)
           

if __name__ == "__main__":
    window()