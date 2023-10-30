from turtle import *
from math import *

def draw_hexagon(x, y, side_len, color):
    pu()
    goto(x, y)
    pd()
    fillcolor(color)
    begin_fill()

    angle = 60
    half_d = d/2
    side_len = (3**0.5 / 6) * half_d
    for i in range(6):
        fd(side_len)
        rt(angle)

    end_fill()
    pu()

draw_hexagon(0, 0, 100, 'black')

exitonclick()

'''
x, y = map(int, input('Введите координаты точки, от которой рисуется фигура: ').split())
side_len = int(input('Введите длину стороны шестиугольника: '))
color = input('Введите название цвета для фигуры: ')
draw_hexagon(x, y, side_len, color)
'''