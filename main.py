from turtle import *
import turtle

HALF_SHREK = [
    [0, 0],
    [100, -10],
    [85, 30],
    [110, 60],
    [60, 200],
    [30, 240],
    [25, 280],
    [55, 290],
    [60, 310], # tip of shreks ear
    [30, 290],
    [0, 290],
]

HALF_FARQUAAD = [
    [60, 310],
    [140, 290],
    [170, 310],
    [200, 310],
    [200, -20],
] + HALF_SHREK[1:-3]

FARQUAAD_HAIR = [
    [60, 310], # tip of shreks ear
    [140, 290],
    [80, 270],
    [110, 60],  # tip of shreks hand
    [60, 200],
    [30, 240],
    [25, 280],
    [55, 290],
]

FARQUAAD_HAT = [
    [100, -10], # tip of shreks foot
    [200, -20], # tip of hat
    [200, 70],
    [110, 60],
    [85, 30],
]

def draw_a_set(x_offset, y_offset, flip_horizontal, flip_vertical):
    y_offset += 290 if flip_vertical else 0
    x_offset += 200 if flip_vertical else 0

    up()
    goto(x_offset, y_offset)
    down()

    turtle.fillcolor('#7bb626')
    turtle.begin_fill()
    draw_zs(HALF_SHREK, x_offset, y_offset, flip_horizontal, flip_vertical)
    turtle.end_fill()

    up()
    draw_zs(HALF_FARQUAAD[:1], x_offset, y_offset, flip_horizontal, flip_vertical)
    down()

    turtle.fillcolor('#dfb1a9')
    turtle.begin_fill()
    draw_zs(HALF_FARQUAAD, x_offset, y_offset, flip_horizontal, flip_vertical)
    turtle.end_fill()

    up()
    draw_zs(FARQUAAD_HAIR[:1], x_offset, y_offset, flip_horizontal, flip_vertical)
    down()

    turtle.fillcolor('black')
    turtle.begin_fill()
    draw_zs(FARQUAAD_HAIR, x_offset, y_offset, flip_horizontal, flip_vertical)
    turtle.end_fill()


    up()
    draw_zs(FARQUAAD_HAT[:1], x_offset, y_offset, flip_horizontal, flip_vertical)
    down()

    turtle.fillcolor('#d60b23')
    turtle.begin_fill()
    draw_zs(FARQUAAD_HAT, x_offset, y_offset, flip_horizontal, flip_vertical)
    turtle.end_fill()






def draw_zs(zs, x_offset, y_offset, flip_horizontal, flip_vertical):
    x_multiplier = -1 if flip_horizontal else 1
    y_multiplier = -1 if flip_vertical else 1
    for x, y in zs:
        goto(x_offset + x_multiplier * x, y_offset + y_multiplier * y)

BEGIN_X = -200
BEGIN_Y = 300

start_x = BEGIN_X
start_y = BEGIN_Y

# FARQUAAD TEST
#draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=False, flip_vertical=True)
#draw_a_set(x_offset=start_x + 400, y_offset=start_y, flip_horizontal=True, flip_vertical=True)


for row in range(1):
    should_flip_vertical = row % 2 == 1
    for col in range(1):
        draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=False, flip_vertical=should_flip_vertical)
        draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=True, flip_vertical=should_flip_vertical)
        start_x += 400
    start_y -= 310 # height of farquaad
    start_x = BEGIN_X

ts = turtle.getscreen()
mainloop()
#ts.getcanvas().postscript(file="duck.eps")