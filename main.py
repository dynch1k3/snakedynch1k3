# Подключение библиотек
# from turtle import color
import pygame
import time
from random import randint

# Инициализация библиотеки pygame
pygame.init()

# Объявление переменных для цвета
white = (100, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

green = (50, 205, 50)

#
dis_width = 800
dis_height = 400

print(randint(0, dis_width))

min_Width = 500
min_Height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Моя первая игра в змейку')

game_over = False
#  начальное положение
x1 = (dis_width - min_Width) / 4
y1 = dis_height / 2

# Размер змейки
snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30
# Яблоко
x_apple = randint(0, dis_width)
y_apple = randint(0, dis_height)

apple_size = 35

font_style = pygame.font.SysFont(None, 50)

def randomApple():
    x_apple = randint(0, dis_width)
    y_apple = randint(0,dis_height)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2.5, dis_height / 2.5])


while not game_over:
    for event in pygame.event.get():
        randomApple()
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    x_apple = randint(0, dis_width)
    y_apple = randint(0, dis_height)
    #Условия Проигрыша
    if ((x1 > dis_width or x1 < 0) or (y1 > dis_height or y1 < 0)):
        game_over = True
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)

    # Для добавления используем метод draw
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    # Рисуем яблоко
    pygame.draw.rect(dis, green, [x_apple, y_apple, apple_size, apple_size], 100)
    pygame.display.update()

    clock.tick(snake_speed)

message("ТЫ ЛОХ!!", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()