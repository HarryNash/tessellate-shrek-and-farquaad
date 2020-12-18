from turtle import *
import turtle

HALF_SHREK = [
    [0, 0],
    [90, -15],
    [85, 30],
    [110, 60],
    [80, 200],
    [55, 240],
    [50, 280],
    [100, 310],
    [30, 290],
    [0, 290],
]

HALF_FARQUAAD = [
    [100, 310],
    [100, 290],
    [170, 310],
    [200, 310],
    [200, -25],
] + HALF_SHREK[1:-3]

def draw_a_set(x_offset, y_offset, flip_horizontal, flip_vertical):

    up()
    goto(x_offset, y_offset)
    down()

    turtle.fillcolor('green')
    turtle.begin_fill()
    draw_zs(HALF_SHREK, x_offset, y_offset, flip_horizontal, flip_vertical)
    turtle.end_fill()

    up()
    draw_zs(HALF_FARQUAAD[:1], x_offset, y_offset, flip_horizontal, flip_vertical)
    down()

    turtle.fillcolor('red')
    turtle.begin_fill()
    draw_zs(HALF_FARQUAAD, x_offset, y_offset, flip_horizontal, flip_vertical)
    turtle.end_fill()

def draw_zs(zs, x_offset, y_offset, flip_horizontal, flip_vertical):
    x_multiplier = -1 if flip_horizontal else 1
    y_multiplier = -1 if flip_vertical else 1
    for x, y in zs:
        goto(x_offset + x_multiplier * x, y_offset + y_multiplier * y)

start_x = 0
start_y = 0

#turtle.bgcolor("red")
draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=False, flip_vertical=False)
draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=True, flip_vertical=False)

draw_a_set(x_offset=start_x + 200, y_offset=start_y + 600, flip_horizontal=False, flip_vertical=True)
draw_a_set(x_offset=start_x + 200, y_offset=start_y + 600, flip_horizontal=True, flip_vertical=True)


ts = turtle.getscreen()
mainloop()
#ts.getcanvas().postscript(file="duck.eps")