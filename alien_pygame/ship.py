import pygame
from setting import settings

class Ship:
    """管理飞船"""
    def __init__(self,ai_game):
        self.settings=settings()
        """初始化飞船并设置其初始位置"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #加载飞船并获取其外接矩形
        self.image=pygame.image.load('photos/ship.png')
        self.rect=self.image.get_rect()
        #每艘飞船放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom
        #在飞船的移动属性中存储一个浮点数
        self.x=float(self.rect.x)
        #移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新飞船而不是移动对象的X值
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
            #根据self.x更新rect对象
        self.rect.x=self.x
    def blitem(self):
        self.screen.blit(self.image,self.rect)
