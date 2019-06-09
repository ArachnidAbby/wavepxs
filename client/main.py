import pygame
import cv2
pygame.init()
global alive,display 
alive,display = True,pygame.display.set_mode((600,600))
def run():
    global alive
    while alive:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                alive=False
        display.fill((255,255,255))
        pygame.display.update()
run()
    
    
