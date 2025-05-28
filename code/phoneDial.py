import time
import digitalio
import board
import adafruit_matrixkeypad

from bbs import *

cols = [digitalio.DigitalInOut(x) for x in (board.D9, board.D5, board.D11)]
rows = [digitalio.DigitalInOut(x) for x in (board.D6, board.D13, board.D12, board.D10)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

phone_digits = []
connected = False

while True:
    if not connected:
        while len(phone_digits) < 3:
            keys = keypad.pressed_keys
            if keys:
                if isinstance(keys[0], int):
                    phone_digits.append(keys[0])
            time.sleep(0.2)
        phone_number = phone_digits[0] * 100 + phone_digits[1] * 10 + phone_digits[2]
        phone_digits = []
        print("connected to " + lookup(phone_number) + " on " + str(phone_number))
        connected = True

    keys = keypad.pressed_keys
    if keys:
        if keys[0] == "#":
            connected = False
            print("disconnected")


