""" Simple bubble creator, destroyer, to test out
    picoDisplay buttons and shapes
"""

from collections import namedtuple
from random import random

import picodisplay as display
    

# Globals
## BUTTONS
X = display.BUTTON_X
Y = display.BUTTON_Y
A = display.BUTTON_A
B = display.BUTTON_B

## DISPLAY
WIDTH = display.get_width()
HEIGHT = display.get_height()

# x, y pos, radius, delta x, delta y, Pen (picodisplay)
Ball = namedtuple('Ball', ['x', 'y', 'r', 'dx', 'dy', 'pen'])
balls = []

def ball_factory(r) -> Ball:
    b = Ball(
            random.randint(r, r + (WIDTH - 2 * r)),
            random.randint(r, r + (HEIGHT - 2 * r)),
            r,
            (14 - r) / 2,
            (14 - r) / 2,
            display.create_pen(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        )
    return b

while True:
    display.set_pen(40, 40, 40)
    display.clear()    

    if display.is_pressed(A):
        r = randint(0, 10) + 3
        b = ball_factory(r)
        balls.append(b)

    for ball in balls:
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
        
    display.update()
    time.sleep(0.01)

        
    