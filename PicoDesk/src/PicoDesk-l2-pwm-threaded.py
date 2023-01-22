""" Pico Planter Desk - PWM Two lights in separate threads.

    Level 2 - Add in PWM control to balance blue output
    
    detail: The Blue LED will put out MUCH more power
    overall. Depending on the particular plant, this
    may exceed optimal usable input within that energy level.
    Lower this.
    
    Blue should be on approx 2/3 the total time
    that red is on. Any lighting (B|R) should be
    on ~2:1 compared to dark. 
"""

from machine import Pin
from time import sleep
import _thread

# TIME
MIN = 60
HOUR = 60 * 60

B_ON = 2/3 * MIN
B_OFF = 1 * MIN

R_ON = 3/3 * MIN
R_OFF = 1 * MIN

# LEDS
B = Pin(0, Pin.OUT)
R = Pin(1, Pin.OUT)
    
def cycle(led: Pin, on: int, off: int):
    """Cycle a GPIO pin on/off for x,y seconds each.

    Args:
      pin: Pi Pico GPIO pin. Must be in 0<pin<34. see Pico Docs. 
      on: time in seconds to keep pin.on
      off: time in seconds to keep pin.off

    Return:
      None
    """
    
    while True:
        led.on()
        sleep(on)
        led.off()
        sleep(off)
    


if __name__ == "__main__":
    # both threads continue indefinitely3333333333333333333333333
    blue_thread = _thread.start_new_thread(cycle, (B,B_ON,B_OFF))
    red_thread = cycle(R,R_ON,R_OFF)
        



