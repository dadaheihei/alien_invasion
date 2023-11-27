import sys
import pygame
from setting import settings
from ship import Ship

class alienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #窃听鼠标和键盘
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=True
                if event.key==pygame.K_LEFT:
                    self.ship.moving_left=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
                if event.key==pygame.K_LEFT:
                    self.ship.moving_left=False            
    def _update_screen(self):
        """更新屏幕上的图像并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitem()
        pygame.display.flip()
if __name__=='__main__':
    #创造游戏实例并运行游戏
    ai=alienInvasion()
    ai.run_game()


#该文件达到了生成pygame窗口，响应用户输入，并可以控制帧率设置背景色