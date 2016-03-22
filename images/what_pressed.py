from microbit import *

shake = False
while True:
    if shake:
        pin0.write_digital(1)
        display.show(Image.SQUARE)
    else:
        pin0.write_digital(0)
        display.clear()
    if accelerometer.was_gesture('shake'):
        shake = not shake
        sleep(500)
# Write your code here :-)