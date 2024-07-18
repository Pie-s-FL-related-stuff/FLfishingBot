from config import BUTTON
from fishing_spots.FishingSpot import FishingSpot
from game_interface import tap, hold, wait, click


class CactoCove(FishingSpot):
    @staticmethod
    def refresh():
        # go 2 zones away
        hold(BUTTON.DOWN, 1.35)                  # get in the cave 1/2
        hold(BUTTON.LEFT, 2)                    # 2/2
        wait(3)                                 # wait loading screen
        hold(BUTTON.UP, 5)                      # go up into the portal
        tap(BUTTON.A)                           # get in the portal
        wait(7)                                 # wait animation + loading screen
        tap(BUTTON.A)                           # get in the portal
        wait(7)                                 # wait animation + loading screen
        hold(BUTTON.DOWN, 5)                    # go back to the beach
        wait(5)                                 # wait loading screen
        # kill mobs and go to the fishing spot
        tap(BUTTON.A)                           # draw weapon
        hold([BUTTON.UP, BUTTON.RIGHT], 0.5)    # get out of the way for allies
        wait(3)
        hold([BUTTON.UP, BUTTON.RIGHT], 5)
        hold(BUTTON.LEFT, 1.05)
        tap(BUTTON.B)                           # undraw weapon
        wait(1)

    @staticmethod
    def reposition():
        hold([BUTTON.UP, BUTTON.LEFT], 0.18)
        hold(BUTTON.UP, 0.1)
        wait(3)

    @staticmethod
    def reset():
        for _ in range(20):
            tap(BUTTON.B)
            wait(0.1)
        wait(2)
        # tp to al maajik
        click(679, 720)
        wait(2)
        tap(BUTTON.D_UP)
        wait(0.1)
        tap(BUTTON.A)
        wait(0.5)
        tap(BUTTON.D_UP)
        wait(0.1)
        tap(BUTTON.A)
        wait(0.5)
        tap(BUTTON.D_LEFT)
        wait(0.1)
        tap(BUTTON.A)
        wait(5)
        # get out of home
        hold(BUTTON.DOWN, 1)
        tap(BUTTON.A)
        wait(8)
        # get to the portal
        hold([BUTTON.UP, BUTTON.RIGHT], 6.3)
        hold(BUTTON.DOWN, 2)
        tap(BUTTON.A)
        wait(8)
        # get to the boat
        hold([BUTTON.UP, BUTTON.LEFT], 2)
        hold([BUTTON.DOWN, BUTTON.LEFT], 2)
        hold(BUTTON.DOWN, 7)
        hold(BUTTON.LEFT, 0.4)
        for _ in range(20):
            tap(BUTTON.A)
            wait(0.1)
        wait(5)
        tap(BUTTON.A)
        hold([BUTTON.DOWN, BUTTON.LEFT], 60)
        hold(BUTTON.UP, 5)
        hold([BUTTON.UP, BUTTON.RIGHT], 1)
        hold(BUTTON.LEFT, 1.05)
        tap(BUTTON.B)  # undraw weapon
        wait(1)
