import pygame
import cv2
import ImageHandling
ImageHandling.base_image()
pygame.init()
global alive,display 
alive,display = True,pygame.display.set_mode((600,600))
viewable = pygame.image.load("image\current.png")
def run():
    global alive
    while alive:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                alive=False
        display.fill((255,255,255))
        display.blit(viewable,(0,0))
        pygame.display.update()
run()
    
    
