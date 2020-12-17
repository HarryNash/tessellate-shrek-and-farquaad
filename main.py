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

def draw_shrek(x_offset, y_offset, upside_down):
    up()
    goto(x_offset, y_offset)
    down()
    turtle.fillcolor('green')
    turtle.begin_fill()
    draw_half_shrek(x_offset, y_offset, False, upside_down)
    turtle.end_fill()
    up()
    goto(x_offset, y_offset)
    down()
    turtle.begin_fill()
    draw_half_shrek(x_offset, y_offset, True, upside_down)
    turtle.end_fill()
    up()

def draw_half_shrek(x_offset, y_offset, reverse, upside_down):
    x_multiplier = -1 if reverse else 1
    y_multiplier = -1 if upside_down else 1
    for x, y in HALF_SHREK:
        goto(x_offset + x * x_multiplier, y_offset + y_multiplier * y)

#turtle.bgcolor("red")
for i in range(3):
    is_upside_down = i % 2 == 0
    extra = 0 if is_upside_down else 55
    for j in range(3):
        draw_shrek(x_offset=-500 + i * 220, y_offset=-500 + j * 650 + extra, upside_down=is_upside_down)


"""
right(10)
forward(100)
left(110)
forward(100)
right(50)
forward(40)
left(50)
forward(200)
left(20)
forward(40)
right(10)
forward(50)
right(90)
forward(60)
left(170)
forward(80)
"""



ts = turtle.getscreen()
mainloop()
#ts.getcanvas().postscript(file="duck.eps")