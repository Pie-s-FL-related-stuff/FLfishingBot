from time import sleep
import keyboard
import mouse

from config import EMULATION_SPEED, BUTTON


def tap(key: BUTTON):
    key = key.value
    keyboard.press(key)
    sleep(0.1)
    keyboard.release(key)


def hold(key: BUTTON | list[BUTTON], duration: float):
    key = key.value if isinstance(key, BUTTON) else [k.value for k in key]
    keyboard.press(key)
    wait(duration)
    keyboard.release(key)


def wait(duration: float):
    sleep(duration / EMULATION_SPEED)


def click(x: int, y: int):
    mouse.move(x, y, absolute=True)
    wait(0.1)
    mouse.press(mouse.LEFT)
    wait(0.1)
    mouse.release(mouse.LEFT)
