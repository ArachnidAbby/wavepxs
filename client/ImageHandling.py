from cv2 import *
import pygame
pygame.init()

class base_image:
    def __init__(self):
        self.image = imread('image\current.png')
        self.w = len(self.image)
        self.h = len(self.image[len(self.image)-1])
        self.x = 100
        self.y = 0
        print(self.w," ",self.h)
        self.scale = 1
        self.color = (0,0,0)
    def show(self,display):
        viewable = pygame.image.load("image\current.png")
        display.blit(viewable,(self.x,self.y))
    def click(self):
        mpos = pygame.mouse.get_pos()
        mclick = pygame.mouse.get_pressed()
        if mclick[0]==True:
            AMP = ( int((mpos[1]-self.y)/self.scale), int((mpos[0]-self.x)/self.scale))#Adjusted Mouse Possition        
            self.image.itemset((AMP[0],AMP[1],0),self.color[0])
            self.image.itemset((AMP[0],AMP[1],1),self.color[1])
            self.image.itemset((AMP[0],AMP[1],2),self.color[2])
            imwrite('image\current.png',self.image) 