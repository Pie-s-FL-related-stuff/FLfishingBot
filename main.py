from PIL import ImageGrab
from statistics import mean
from time import perf_counter
from keyboard import press, release

from config import BUTTON
from game_interface import tap, wait


from fishing_spots.CactoCove import CactoCove
location = CactoCove


class SomethingWentWrong(Exception):
    pass


def is_fish_in_hook():
    img = ImageGrab.grab(bbox=(953, 178, 979, 197))
    average_color = [mean(img.getdata(band)) for band in range(3)]
    return average_color[0] > 150 and average_color[1] < 100 and average_color[2] < 100


def catch_fish():
    tap(BUTTON.A)
    wait(4)
    start_time = perf_counter()
    while not is_fish_in_hook():
        if perf_counter() - start_time > 30:
            raise SomethingWentWrong("No fish in hook")
    press("w")
    start_time = perf_counter()
    while not ImageGrab.grab(bbox=(1321, 480, 1322, 481)).getpixel((0, 0)) == (243, 234, 220):
        if perf_counter() - start_time > 10:
            break
    release("w")
    wait(0.1)
    tap(BUTTON.A)
    wait(1)
    tap(BUTTON.A)


def main():
    location.reset()
    while True:
        i = 0
        while i < 4:
            try:
                catch_fish()
            except SomethingWentWrong:
                print("resetting (something went wrong)")
                location.reset()
                i = -1
            if i != 3:
                location.reposition()
            i += 1
        location.refresh()


if __name__ == "__main__":
    wait(3)
    main()
