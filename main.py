import pygame
from plane_sprites import *
pygame.init()
screen=pygame.display.set_mode((480,720))

bg=pygame.image.load("./resource/background.png")
screen.blit(bg,(0,0))
# pygame.display.update()
# ap1=pygame.image.load("./resource/airport.png")
# ap1=pygame.transform.scale(ap1,(50,60))
# screen.blit(ap1,(200,600))

pygame.display.update()
clock=pygame.time.Clock()

#创建英雄飞机的精灵
hero=GameSprite('./resource/airport.png',1)
hero.rect=pygame.Rect(200,600,50,60)
#创建英雄飞机的精灵组
hero_group=pygame.sprite.Group(hero)
#创建敌机的精灵
enemy=GameSprite('./resource/enemy1.png',1)
enemy1=GameSprite('./resource/enemy1.png',2)
#创建敌机的精灵组
enemy_group=pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)
    # if hero.rect.y<=-60:
    #     hero.rect.y=600
    # hero.rect.y-=1
    screen.blit(bg, (0, 0))
    # screen.blit(ap1,hero_rect)
    #扯精灵组调用两个方法
    enemy_group.update('down')
    enemy_group.draw(screen)
    hero_group.update('up')
    hero_group.draw(screen)


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

