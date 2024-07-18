from abc import abstractmethod

from config import BUTTON
from game_interface import tap, hold, wait, tp_to, HOMES


class FishingSpot:
    @staticmethod
    @abstractmethod
    def refresh():
        pass

    @staticmethod
    @abstractmethod
    def reposition():
        pass

    @staticmethod
    @abstractmethod
    def reset():
        pass


def reset_to_home(home: HOMES):
    for _ in range(20):
        tap(BUTTON.B)
        wait(0.1)
    wait(2)
    tp_to(home)
    # get out of home
    hold(BUTTON.DOWN, 1)
    tap(BUTTON.A)
    wait(8)
