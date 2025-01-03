import pygame
import os

BASE_IMAGE_PATH = "game_testing/data/images/"
BASE_SFX_PATH = "game_testing/data/sfx/"
TILE_SIZE = 16

def load_sfx(path):
    return pygame.mixer.Sound(BASE_SFX_PATH + path)

def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_trans_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert_alpha()
    return img

def load_trans_scaled_images(path, scale):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        img=load_trans_image(path + "/" + img_name)
        img=pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale*1.4))
        img=pygame.transform.rotate(img, 100)
        img=pygame.transform.flip(img, False, True)
        images.append(img)
    return images

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images.append(load_image(path + "/" + img_name))
    return images

def load_trans_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images.append(load_trans_image(path + "/" + img_name))
    return images

def load_tile(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images.append(load_image(path + "/" + img_name))
    return images

def load_fix_tile(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images.append(pygame.transform.scale(load_image(path + "/" + img_name), (TILE_SIZE, TILE_SIZE)))
    return images

class Animation:
    def __init__(self,images, duration=5,loop=True):
        self.images = images
        self.duration = duration
        self.loop = loop
        self.current_frame = 0
        self.counter = 0
        self.done = False   
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.duration, self.loop)
    
    def img(self):
        return self.images[int(self.frame/self.duration)]

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (len(self.images)*self.duration)
        else:
            self.frame = min(self.frame + 1, len(self.images)*self.duration-1)  
            if self.frame >= len(self.images)*self.duration-1:
                self.done = True