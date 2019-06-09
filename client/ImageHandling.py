from cv2 import *
class base_image:
    def __init__(self):
        self.image = imread('image\current.png')
        self.w = len(self.image)
        self.h = len(self.image[len(self.image)-1])
        print(self.w," ",self.h)
        self.scale = 1
        