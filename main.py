from random import choice
import numpy as np


def dice():
    numbers = np.arange(1, 7, 1)

    dice_1 = choice(numbers)
    dice_2 = choice(numbers)

    print(f"{dice_1} & {dice_2}")
    return dice_1, dice_2


if __name__ == "__main__":
    first_dice, second_dice = dice()
    if first_dice == second_dice == 6:
        print("Winner Winner Chicken Dinner!")
    else:
        print("maybe next time")
