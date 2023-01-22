""" Pico Planter Desk - Two lights on short timer.

    Level 0 - start two leds blinking on and off,
    on a short enough timer to diagnose any wiring issues.
"""

from machine import Pin
import time

b = Pin(0, Pin.OUT)
r = Pin(1, Pin.OUT)

# Can trouble test with onboard LED 
#led = Pin(25, Pin.OUT)


while True:
    #led.on()
    b.on()
    r.on()
    time.sleep(1)
    b.off()
    time.sleep(1)
    r.off()
    #led.off()
    time.sleep(2)
