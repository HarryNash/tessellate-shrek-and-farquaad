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
    [200, -20],

    [100, -10],
    [85, 30],
    [110, 60],
    [60, 200],
    [30, 240],
    [25, 280],
    [55, 290],



    [60, 310],
    [140, 290],
    [170, 310],
    [200, 310],

    ]

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
    [200, 70],
    [110, 60],
    [85, 30],
    [100, -10], # tip of shreks foot
    [200, -20], # tip of hat

]

SHREK_VEST = [
    [45, 220],
    [50, 160],
    [30, 160],
    [15, 165],
    [12, 180],
    [30, 240],
]

SHREK_TROUSERS = [
    [0, 0],
    [100, -10],
    [85, 30],
    [0, 30],
    [0, 0]
]

SHREK_SHIRT = [
    [0, 180],
    [30, 240],
    [60, 200],
    [105, 74],
    [95, 74],
    [50, 160],
    [95, 74],
    [98, 66],
    [0,0],
]

FARQUAAD_EYEBROWS = [
    [120, 90], # overside of brow
    [110, 120],  # rightmost part
    [120, 105], #  underside of brow
    [190, 120],  # leftmost part
]

FARQUAAD_MOUTH = [
    [200, 250],
    [120, 210],
    [200, 220]
]

SHREK_MOUTH = [
    [0, 250],
    [20, 250],
    [23, 240],
    [0, 240]
]

FARQUAAD_NOSE = [
    [200, 210 - 20],

    [180, 180 - 20],
    [200, 220 - 20],

]


def draw_a_set(x_offset, y_offset, flip_horizontal, flip_vertical):
    y_offset += 290 if flip_vertical else 0
    x_offset += 200 if flip_vertical else 0

    draw_shapes(HALF_SHREK, '#7bb626', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(SHREK_SHIRT, '#e8e5c4', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(SHREK_VEST, '#5f4726', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(SHREK_TROUSERS, '#5f4726', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(SHREK_MOUTH, '#d60b23', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_eye(15, 260, 4, 10, x_offset, y_offset, flip_horizontal, flip_vertical)

    draw_shapes(HALF_FARQUAAD, '#dfb1a9', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(FARQUAAD_HAIR, 'black', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(FARQUAAD_HAT, '#d60b23', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(FARQUAAD_EYEBROWS, 'black', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(FARQUAAD_MOUTH, '#d60b23', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_shapes(FARQUAAD_NOSE, '#dfb1a9', x_offset, y_offset, flip_horizontal, flip_vertical)
    draw_eye(150, 140, 10, 40, x_offset, y_offset, flip_horizontal, flip_vertical)

def draw_eye(x, y, min, max, x_offset, y_offset, flip_horizontal, flip_vertical):
    up()
    draw_zs([[x, y]], x_offset, y_offset, flip_horizontal, flip_vertical)
    down()
    dot(max, 'white')
    dot(min, 'black')

def draw_shapes(points, colour, x_offset, y_offset, flip_horizontal, flip_vertical):
    up()
    draw_zs(points[:1], x_offset, y_offset, flip_horizontal, flip_vertical)
    down()

    turtle.fillcolor(colour)
    turtle.begin_fill()
    draw_zs(points, x_offset, y_offset, flip_horizontal, flip_vertical)
    turtle.end_fill()





def draw_zs(zs, x_offset, y_offset, flip_horizontal, flip_vertical):
    x_multiplier = -1 if flip_horizontal else 1
    y_multiplier = -1 if flip_vertical else 1
    for x, y in zs:
        goto(x_offset + x_multiplier * x, y_offset + y_multiplier * y)

BEGIN_X = -400
BEGIN_Y = 300

start_x = BEGIN_X
start_y = BEGIN_Y

# FARQUAAD TEST
# draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=False, flip_vertical=True)
# draw_a_set(x_offset=start_x + 400, y_offset=start_y, flip_horizontal=True, flip_vertical=True)


for row in range(2):
    should_flip_vertical = row % 2 == 1
    for col in range(2):
        draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=False, flip_vertical=should_flip_vertical)
        draw_a_set(x_offset=start_x, y_offset=start_y, flip_horizontal=True, flip_vertical=should_flip_vertical)
        start_x += 400
    start_y -= 310 # height of farquaad
    start_x = BEGIN_X

ts = turtle.getscreen()
mainloop()
#ts.getcanvas().postscript(file="duck.eps")