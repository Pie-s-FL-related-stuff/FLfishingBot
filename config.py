from enum import Enum


class BUTTON(Enum):
    A = "w"
    B = "x"
    X = "c"
    Y = "v"

    UP = "z"
    LEFT = "q"
    DOWN = "s"
    RIGHT = "d"

    D_UP = "t"
    D_LEFT = "f"
    D_DOWN = "g"
    D_RIGHT = "h"


EMULATION_SPEED = 1


class TOUCH_SCREEN(Enum):
    MAP = (679 - 180, 720 - 180)    # IDK why but the mouse.move function is off by 180 on my laptop screen, so this is temporary
