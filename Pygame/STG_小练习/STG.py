# _*_coding:utf-8_*_

# 《 节 操 巫 女 》
# 算是一个小成品了


#加载模块
from pyhelper import *

#主程序
def main():
    #初始化
    pygame.init()
    init_clock = pygame.time.Clock()
    screen_size = (720, 480)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Test")

    #背景
    background = pygame.Surface(screen.get_size())
    backgroung = background.convert()
    background.fill((233, 233, 233))

    #玩家
    player = Player("博丽灵梦.png")
    player.set_pos((100, 100))

    #移动操作变量
    x_left = x_right = y_down = y_up = 0
    speed_xy = 4

    #blit
    screen.blit(background, (0, 0))
    player.blit_on(screen)
    pygame.display.flip()

    #主循环
    while True:
        #event
        for event in pygame.event.get():
            if event.type == QUIT:    #退出
                exit()
            elif event.type == KEYDOWN:
                if event.key == 27:
                    exit()
                if event.key == K_LEFT:    #方向操作检测
                    x_left = speed_xy
                elif event.key == K_RIGHT:
                    x_right = speed_xy
                elif event.key == K_DOWN:
                    y_down = speed_xy
                elif event.key == K_UP:
                    y_up = speed_xy
            elif event.type == KEYUP:    #方向操作复位
                if event.key == K_LEFT:
                    x_left = 0
                elif event.key == K_RIGHT:
                    x_right = 0
                elif event.key == K_DOWN:
                    y_down = 0
                elif event.key == K_UP:
                    y_up = 0


        #update
        dx, dy = x_right - x_left, y_down - y_up
        if player.pos[0] <= speed_xy and dx < 0: dx = 0
        if player.pos[0] >= screen_size[0] - speed_xy and dx > 0: dx = 0
        if player.pos[1] <= speed_xy and dy < 0: dy = 0
        if player.pos[1] >= screen_size[1] - speed_xy and dy > 0: dy = 0
        
        player.move( (dx, dy) )    #移动

        #System
        screen.blit(background, (0, 0))
        player.blit_on(screen)
        pygame.display.flip()
        init_clock.tick_busy_loop(60)


if __name__ == '__main__':
    main()
