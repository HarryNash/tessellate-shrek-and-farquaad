from turtle import *

SHREK = [
    [0, 0],
    [100, -10],
    [85, 30],
    [110, 60],
    [60, 200],
    [30, 240],
    [25, 280],
    [55, 290],
    [60, 310],
    [30, 290],
    [0, 290],
]

SHREK_VEST = [
    [45, 220],
    [50, 160],
    [30, 160],
    [15, 165],
    [12, 180],
    [30, 240],
]

SHREK_TROUSERS = [[0, 0], [100, -10], [85, 30], [0, 30], [0, 0]]

SHREK_SHIRT = [
    [0, 180],
    [30, 240],
    [60, 200],
    [105, 74],
    [95, 74],
    [50, 160],
    [95, 74],
    [98, 66],
    [0, 0],
]

SHREK_MOUTH = [[0, 250], [20, 250], [23, 240], [0, 240]]

FARQUAAD = [
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
    [60, 310],
    [140, 290],
    [80, 270],
    [110, 60],
    [60, 200],
    [30, 240],
    [25, 280],
    [55, 290],
]

FARQUAAD_HAT = [
    [200, 70],
    [110, 60],
    [85, 30],
    [100, -10],
    [200, -20],
]

FARQUAAD_EYEBROWS = [
    [120, 90],
    [110, 120],
    [120, 105],
    [190, 120],
]

FARQUAAD_MOUTH = [[200, 250], [120, 210], [200, 220]]

FARQUAAD_NOSE = [[200, 190], [180, 160], [200, 200]]

GREEN = "#7bb626"
CREAM = "#e8e5c4"
BROWN = "#5f4726"
RED = "#d60b23"
PINK = "#dfb1a9"

COMPOSITION = [
    [SHREK, GREEN],
    [SHREK_SHIRT, CREAM],
    [SHREK_VEST, BROWN],
    [SHREK_TROUSERS, BROWN],
    [SHREK_MOUTH, RED],
    [FARQUAAD, PINK],
    [FARQUAAD_HAIR, "black"],
    [FARQUAAD_HAT, RED],
    [FARQUAAD_EYEBROWS, "black"],
    [FARQUAAD_MOUTH, RED],
    [FARQUAAD_NOSE, PINK],
]

BEGIN_X = -400
BEGIN_Y = 300

ROWS = 10
COLUMNS = 10


def draw_atom(x_offset, y_offset, flip_on_y_axis, flip_on_x_axis):
    y_offset += 290 if flip_on_x_axis else 0
    x_offset += 200 if flip_on_x_axis else 0
    x_multiplier = -1 if flip_on_y_axis else 1
    y_multiplier = -1 if flip_on_x_axis else 1

    for shape, colour in COMPOSITION:
        paint_shape(shape, colour, x_offset, y_offset, y_multiplier, x_multiplier)

    paint_eye([15, 260], 4, 10, x_offset, y_offset, y_multiplier, x_multiplier)
    paint_eye([150, 140], 10, 40, x_offset, y_offset, y_multiplier, x_multiplier)


def paint_eye(position, pupil, eyeball, x_offset, y_offset, y_multiplier, x_multiplier):
    jumpto(position, x_offset, y_offset, y_multiplier, x_multiplier)
    dot(eyeball, "white")
    dot(pupil, "black")


def jumpto(position, x_offset, y_offset, y_multiplier, x_multiplier):
    up()
    draw_shape([position], x_offset, y_offset, y_multiplier, x_multiplier)
    down()


def paint_shape(shape, colour, x_offset, y_offset, y_multiplier, x_multiplier):
    jumpto(shape[0], x_offset, y_offset, y_multiplier, x_multiplier)
    fillcolor(colour)
    begin_fill()
    draw_shape(shape, x_offset, y_offset, y_multiplier, x_multiplier)
    end_fill()


def draw_shape(zs, x_offset, y_offset, y_multiplier, x_multiplier):
    for x, y in zs:
        goto(x_offset + x_multiplier * x, y_offset + y_multiplier * y)


def main():
    x = BEGIN_X
    y = BEGIN_Y
    hideturtle()
    for row in range(ROWS):
        flip_on_x_axis = row % 2 == 1
        for col in range(COLUMNS):
            draw_atom(
                x_offset=x,
                y_offset=y,
                flip_on_y_axis=False,
                flip_on_x_axis=flip_on_x_axis,
            )
            x += max([x for x, _ in FARQUAAD]) * 2
        y -= max([y for _, y in FARQUAAD])
        x = BEGIN_X

    ts = getscreen()
    ts.getcanvas().postscript(file="shrek.eps")


if __name__ == "__main__":
    main()
