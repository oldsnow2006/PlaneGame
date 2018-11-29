import pygame
import random
#屏幕大小的常量
SCREEN_RECT=pygame.Rect(0,0,640,800)
#游戏刷新率
REFRESH_RATE=60
#敌机的定时器常量
CREATE_ENEMY_EVENT=pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵类"""
    def __init__(self,image_name,speed):
        #调用父类的初始化方法
        super().__init__()
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed
    def update(self):
        #精灵纵向移动
        self.rect.y+=self.speed

class BackGround(GameSprite):
    """继承自游戏精灵类的背景类，重写update方法，实现背景的交替移动"""
    def __init__(self,is_alt=False):
        #1.调用父类方法实现精灵的创建（image/rect/speed)
        super().__init__("./resource/background.png",1)
        #2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y=-self.rect.height

    def update(self):
        #1.调用父类的方法实现
        super().update()
        #2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-self.rect.height
class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./resource/enemy1.png",1)
        #2.指定敌机的初始随机速度
        self.speed=random.randint(1,3)
        #3.指定敌机的初始随机位置
        self.rect.bottom=0
        self.rect.x=random.randint(0,SCREEN_RECT.width-self.rect.width) #敌机精灵的横向随机位置
    def update(self):
        #1.调用父类方法，保持飞机垂直方向的移动
        super().update()
        #2.判断是否飞出低部，如果是就从精灵组中删除
        if self.rect.y>=SCREEN_RECT.height:
            print("飞出屏幕，从精灵组中删除")
            self.kill()
    def __del__(self):
        print("敌机已从内存销毁")

