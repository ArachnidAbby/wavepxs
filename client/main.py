import pygame
import cv2
import ImageHandling
showish = ImageHandling.base_image()
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
        showish.click()
        display.fill((40,10,8))
        showish.show(display)
        pygame.display.update()
run()
    
    
