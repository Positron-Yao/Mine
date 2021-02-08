# _*_coding:utf-8_*_

# 御用导入模块
# (是的就这)

#加载模块
try:
    import pygame
    from pygame.locals import *
    from sys import exit
    import os
    import getopt
    import random
    import math
    from socket import *
except ImportError as err:
    print("无法加载模块... %s" % err )
    exit()

class Tools:
    '''
    工具类
    里面放着一些工具(字面意思)
    比如加载图片什么的
    '''

    #加载图像并返回图像对象及图像的Rect
    def load_png(name):
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error as message:
            print("无法加载图片:", fullname)
            raise SystemExit(message)
        return image, image.get_rect()


class Player(pygame.sprite.Sprite):
    '''
    玩家类
    用来定义一个玩家对象
    (可不是玩家的对象!)
    '''
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        #加载一个图像
        self.image, self.rect = Tools.load_png(image_path)
        self.pos = (0, 0)
        
    #旋转
    def rotate(self):
        pygame.transform.rotate(self.image)

    #设置位置
    def set_pos(self, pos):
        self.pos = pos

    #根据位置计算drawpos
    def get_drawpos(self):
        return (self.pos[0] - self.rect.w / 2, self.pos[1] - self.rect.h / 2)

    #将对象blit在Surface上
    def blit_on(self, screen):
        screen.blit(self.image, self.get_drawpos())

    #按向量移动
    def move(self, dp):
        dx, dy = dp
        self.set_pos( ( self.pos[0] + dx , self.pos[1] + dy ) )