from config import BUTTON
from fishing_spots.FishingSpot import FishingSpot, reset_to_home
from game_interface import tap, hold, wait, HOMES


class WestGrassyPlains(FishingSpot):
    @staticmethod
    def refresh():
        hold(BUTTON.UP, 2.2)
        wait(5)
        hold([BUTTON.LEFT, BUTTON.UP], 1.5)
        hold([BUTTON.RIGHT, BUTTON.UP], 5)
        hold(BUTTON.RIGHT, 1.7)
        wait(0.5)
        tap(BUTTON.A)
        wait(5)
        hold(BUTTON.DOWN, 0.5)
        tap(BUTTON.A)
        wait(3)
        hold(BUTTON.LEFT, 5)
        hold(BUTTON.DOWN, 3)
        hold(BUTTON.LEFT, 3)
        wait(5)
        hold([BUTTON.DOWN, BUTTON.RIGHT], 2.15)
        wait(2)

    @staticmethod
    def reposition():
        hold(BUTTON.RIGHT, 0.2)
        wait(3)

    @staticmethod
    def reset():
        reset_to_home(HOMES.CASTELE)
        hold(BUTTON.RIGHT, 2)
        hold(BUTTON.UP, 2)
        hold(BUTTON.RIGHT, 2.2)
        hold([BUTTON.DOWN, BUTTON.RIGHT], 2)
        for _ in range(6):
            tap(BUTTON.A)
            wait(0.2)
        wait(0.3)
        for _ in range(2):
            tap(BUTTON.D_DOWN)
            wait(0.1)
        for _ in range(10):
            tap(BUTTON.A)
            wait(0.1)
        wait(6)
        hold(BUTTON.LEFT, 2)
        wait(5)
        hold([BUTTON.LEFT, BUTTON.DOWN], 6)
        hold(BUTTON.UP, 2)
        hold([BUTTON.UP, BUTTON.RIGHT], 3.5)
        hold([BUTTON.DOWN, BUTTON.RIGHT], 0.3)
        wait(0.2)
