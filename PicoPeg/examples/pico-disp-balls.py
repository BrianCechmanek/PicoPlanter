""" Pico Display Ball Generator and Destroyer
"""

from random import randint
import utime

import picodisplay as display


# GLOBALS
## BUTTONS
X = display.BUTTON_X
Y = display.BUTTON_Y
A = display.BUTTON_A
B = display.BUTTON_B

## DISPLAY
WIDTH = display.get_width()
HEIGHT = display.get_height()

# METHODS
def clear():
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()

# x, y pos, radius, delta x, delta y, Pen (picodisplay)e
class Ball:
    def __init__(self, x, y, r, dx, dy, pen):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.pen = pen


def make_ball(r) -> Ball:
    ball = Ball(
            randint(r, r + (WIDTH - 2 * r)),
            randint(r, r + (HEIGHT - 2 * r)),
            r,
            (14 - r) / 2,
            (14 - r) / 2,
            display.create_pen(randint(0, 255), randint(0, 255), randint(0, 255)),
        )
    return ball

def del_obj(objs: List) -> None:
    try:
        _ = objs.pop(0)
    except IndexError:
        pass

def update_objs(objs: List, width=WIDTH, height=HEIGHT) -> None:
    display.set_pen(40, 40, 40)
    display.clear()

    for ball in objs:
        ball.x += ball.dx
        ball.y += ball.dy

        xmax = width - ball.r
        xmin = ball.r
        ymax = height - ball.r
        ymin = ball.r

        if ball.x < xmin or ball.x > xmax:
            ball.dx *= -1

        if ball.y < ymin or ball.y > ymax:
            ball.dy *= -1

        display.set_pen(ball.pen)
        display.circle(int(ball.x), int(ball.y), int(ball.r))    



# MAIN LOOP
## Initialise display with a bytearray display buffer
buf = bytearray(WIDTH * HEIGHT * 2)
display.init(buf)
display.set_backlight(0.5)

balls = []
while True:
    if display.is_pressed(A):
        r = randint(0, 10) + 3
        ball = make_ball(r)
        balls.append(ball)
        display.set_led(0, 255, 0)
        utime.sleep(0.05)    # hold for a second to create multiple
        display.set_led(0,0,0)
    elif display.is_pressed(B):
        display.set_led(255,0,0)
        del_obj(balls)
        utime.sleep(0.05)    # hold for a second to create multiple
        display.set_led(0,0,0)
    else:
        display.set_pen(255, 0, 0)
        display.text("A: create ball", 10, 10, 240, 2)
        display.text("B: delete ball", 10, 21, 240, 2)
        display.update()

    update_objs(balls)
    utime.sleep(0.1)  # this number is how frequently the Pico checks for button presses