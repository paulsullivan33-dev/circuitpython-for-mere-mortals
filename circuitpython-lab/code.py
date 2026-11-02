# A first CircuitPython program: blink the board's built-in light.
# Generic example - no specific board is assumed beyond "a board
# with a built-in LED pin named LED or D13 on many boards".
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
