__author__ = 'Administrator'
import pygame
from pygame.locals import *
from sys import exit
from boxes.vector import Vector

sprite_image_filename = 'img/2.png'
background_image_filename = 'img/1.png'
mouse_image_filename = 'img/2.png'
SCREEN_SIZE = (640, 480)


def hello_world():
    pygame.init()  # 初始化

    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN, 32)  # 创建窗口
    pygame.display.set_caption("Hello world")
    background = pygame.image.load(background_image_filename).convert()  # 加载图片
    mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(background, (0, 0))  # 添加背景图片

        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width()/2
        y -= mouse_cursor.get_width()/2
        screen.blit(mouse_cursor, (x, y))
        pygame.display.update()


def print_func():

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    font = pygame.font.SysFont('arial', 16)
    font_height = font.get_linesize()
    event_text = []

    while True:
        event = pygame.event.wait()
        event_text.append(str(event))
        event_text = event_text[-int(SCREEN_SIZE[1]/font_height):]
        if event.type == pygame.QUIT:
            exit()
        screen.fill((255, 255, 255))
        y = SCREEN_SIZE[1] - font_height
        for text in reversed(event_text):
            screen.blit(font.render(text, True, (0, 255, 0)), (0, y))
            y -= font_height
        pygame.display.update()


def keyboard_listen():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    background = pygame.image.load(background_image_filename).convert()
    x, y = 0, 0
    move_x, move_y = 0, 0
    full = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_x = -1
                elif event.key == pygame.K_RIGHT:
                    move_x = 1
                elif event.key == pygame.K_UP:
                    move_y = 1
                elif event.key == pygame.K_DOWN:
                    move_y = -1
                elif event.key == pygame.K_f:
                    full = not full
                    if full:
                        screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN, 32)
                    else:
                        screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
            elif event.type == pygame.KEYUP:
                move_x = 0
                move_y = 0

            x += move_x
            y += move_y
            screen.fill((0, 0, 0))
            screen.blit(background, (x, y))
            pygame.display.update()


def show_color():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    all_colors = pygame.Surface((4096, 4096), depth=24)
    for r in range(256):
        x = (r & 15) * 256
        y = (r >> 4) * 256
        for g in range(256):
            for b in range(256):
                all_colors.set_at((x + g, y + b), (r, g, b))
    pygame.image.save(all_colors, 'img/allcolors.bmp')


def color_power():
    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)

    def create_scales(height):
        red_scale_surface = pygame.surface.Surface((640, height))
        green_scale_surface = pygame.surface.Surface((640, height))
        blue_scale_surface = pygame.surface.Surface((640, height))
        for x in range(640):
            c = int((x/640.)*255.)
            red = (c, 0, 0)
            green = (0, c, 0)
            blue = (0, 0, c)
            line_rect = pygame.Rect(x, 0, 1, height)
            pygame.draw.rect(red_scale_surface, red, line_rect)
            pygame.draw.rect(green_scale_surface, green, line_rect)
            pygame.draw.rect(blue_scale_surface, blue, line_rect)
        return red_scale_surface, green_scale_surface, blue_scale_surface

    red_scale, green_scale, blue_scale = create_scales(80)

    color = [127, 127, 127]

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill((0, 0, 0))

        screen.blit(red_scale, (0, 00))
        screen.blit(green_scale, (0, 80))
        screen.blit(blue_scale, (0, 160))

        x, y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            for component in range(3):
                if (component+1)*80 > y > component*80:
                    color[component] = int((x/639.)*255.)
            pygame.display.set_caption("PyGame Color Test - "+str(tuple(color)))

        for component in range(3):
            pos = (int((color[component]/255.)*639), component*80+40 )
            pygame.draw.circle(screen, (255, 255, 255), pos, 20)

        pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

        pygame.display.update()


def color_mix():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)

    color1 = (221, 99, 20)
    color2 = (96, 130, 51)
    factor = 0.

    def blend_color(color1, color2, blend_factor):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        r = r1 + (r2 - r1) * blend_factor
        g = g1 + (g2 - g1) * blend_factor
        b = b1 + (b2 - b1) * blend_factor
        return int(r), int(g), int(b)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill((255, 255, 255))

        tri = [(0, 120), (639, 100), (639, 140)]
        pygame.draw.polygon(screen, (0, 255, 0), tri)
        pygame.draw.circle(screen, (0, 0, 0), (int(factor * 639.0), 120), 10)

        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            factor = x / 639.0
            pygame.display.set_caption("Pygame Color Blend Test - %.3f" % factor)

        color = blend_color(color1, color2 , factor)
        pygame.draw.rect(screen, color, (0, 240, 640, 240))

        pygame.display.update()


def line_sport():
    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)

    background = pygame.image.load(background_image_filename).convert()
    sprite = pygame.image.load(sprite_image_filename)

    # sprite的起始x坐标
    x = 0.

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background, (0, 0))
        screen.blit(sprite, (x, 0))
        x += 2.  # 如果你的机器性能太好以至于看不清，可以把这个数字改小一些

        # 如果移动出屏幕了，就搬到开始位置继续
        if x > 640.:
            x = 0.

        pygame.display.update()


def oblique_sport():
    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)

    background = pygame.image.load(background_image_filename).convert()
    sprite = pygame.image.load(sprite_image_filename).convert_alpha()

    clock = pygame.time.Clock()

    x, y = 100., 100.
    speed_x, speed_y = 133., 170.

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background, (0,0))
        screen.blit(sprite, (x, y))

        time_passed = clock.tick(30)
        time_passed_seconds = time_passed / 1000.0

        x += speed_x * time_passed_seconds
        y += speed_y * time_passed_seconds

        # 到达边界则把速度反向
        if x > 640 - sprite.get_width():
            speed_x = -speed_x
            x = 640 - sprite.get_width()
        elif x < 0:
            speed_x = -speed_x
            x = 0.

        if y > 480 - sprite.get_height():
            speed_y = -speed_y
            y = 480 - sprite.get_height()
        elif y < 0:
            speed_y = -speed_y
            y = 0

        pygame.display.update()


def fish_move():
    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)

    background = pygame.image.load(sprite_image_filename).convert()
    sprite = pygame.image.load(sprite_image_filename).convert_alpha()

    clock = pygame.time.Clock()

    position = Vector(100.0, 100.0)
    heading = Vector()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background, (0, 0))
        screen.blit(sprite, position)

        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0

        # 参数前面加*意味着把列表或元组展开
        destination = Vector(*pygame.mouse.get_pos()) - Vector(*sprite.get_size() )/2
        # 计算鱼儿当前位置到鼠标位置的向量
        vector_to_mouse = Vector.from_points(position, destination)
        # 向量规格化
        vector_to_mouse.normalize()

        # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
        # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
        heading += (vector_to_mouse * .6)

        position += heading * time_passed_seconds
        pygame.display.update()
if __name__ == '__main__':
    # hello_world()
    # keyboard_listen()
    # show_color()
    # color_power()
    # color_mix()
    # line_sport()
    oblique_sport()
    # fish_move()
