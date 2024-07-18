from enum import Enum
from time import sleep
import keyboard
import mouse

from config import EMULATION_SPEED, BUTTON, TOUCH_SCREEN


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


def click(coords: TOUCH_SCREEN):
    mouse.move(*coords.value, absolute=True)
    wait(0.1)
    mouse.press(mouse.LEFT)
    wait(0.1)
    mouse.release(mouse.LEFT)


class HOMES(Enum):
    CASTELE = []
    PORT_PUERTO = [BUTTON.D_DOWN]
    AL_MAAJIK = [BUTTON.D_UP]
    ELDERWOOD = [BUTTON.D_RIGHT]
    LEVITANIA = [BUTTON.D_RIGHT, BUTTON.D_DOWN]
    ORIGINS = [BUTTON.D_RIGHT, BUTTON.D_UP]


def tp_to(home: HOMES):
    click(TOUCH_SCREEN.MAP)
    wait(2)
    tap(BUTTON.D_UP)
    wait(0.1)
    tap(BUTTON.A)
    wait(0.5)
    for button in home.value:
        tap(button)
        wait(0.1)
    tap(BUTTON.A)
    wait(0.5)
    tap(BUTTON.D_LEFT)
    wait(0.1)
    tap(BUTTON.A)
    wait(5)
