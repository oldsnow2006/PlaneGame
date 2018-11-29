import pygame
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏类"""
    def __init__(self):
        #1.创建游戏主窗口
        self.screen=pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
        #2、创建游戏时钟
        self.clock=pygame.time.Clock()
        #3、调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        #4.设置定时器事件---创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
    def __create_sprites(self):#建立精灵和精灵组
        #这儿用两个BACKGROUND对象是实现背景的交替向下移动，不然会有一段空白
        bg1=BackGround()
        bg2=BackGround(True)
        self.bg_group=pygame.sprite.Group(bg1,bg2)
        #创建敌机的精灵组
        self.enemy_group=pygame.sprite.Group()

    def start_game(self):
        while True:
            #1、设置刷新率
            self.clock.tick(REFRESH_RATE)  #括号内为常量刷新率
            #2、事件监听
            self.__event_handler()
            #3、碰撞检测
            self.__check_collide()
            #4、更新、绘制精灵组
            self.__update_sprites()
            #5、更新屏幕
            pygame.display.update()

    def __event_handler(self):
        #判断是否按了关闭按钮，如果是就退出游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            if event.type==CREATE_ENEMY_EVENT:
                #1.创建敌机精灵
                enemy=Enemy()
                #2.将精灵添加到精灵组
                self.enemy_group.add(enemy)
    def __check_collide(self):
        #检测碰撞
        pass
    def __update_sprites(self):
        #让精灵组执行UPDATE和DRAW方法，以实现动画
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == '__main__':
    #创建游戏对象
    game=PlaneGame()
    game.start_game()
    #启动游戏
