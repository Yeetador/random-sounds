import winsound
import random
import time


def function():
    button = input()

    while button == "":
        x = random.randint(1, 3)

        if x == 1:
            winsound.PlaySound("bruh", winsound.SND_FILENAME)
            function()

        elif x == 2:
            winsound.PlaySound("rolbloxdeathsound", winsound.SND_FILENAME)
            function()

        elif x == 3:
            winsound.PlaySound("shutdownsound", winsound.SND_FILENAME)
            function()


function()
