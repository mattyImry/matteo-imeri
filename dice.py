"""Importing Random module."""
import random


def dice_match_2():
    """
        rolling dice checking two of a kind.
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice5 = random.randint(1, 6)

    print("Dice results are " + str(dice1), str(dice2), str(dice3),
          str(dice4), str(dice5))

    match = (dice1 == 1) + (dice2 == 1) + (dice3 == 1)\
        + (dice4 == 1) + (dice5 == 1)

    if match == 2:
        print("Two of a kind")

    else:
        match = (dice1 == 2) + (dice2 == 2) + (dice3 == 2)\
                + (dice4 == 2) + (dice5 == 2)
        if match >= 2:
            print("Two of a kind")

        else:
            match = (dice1 == 3) + (dice2 == 3) + (dice3 == 3)\
                    + (dice4 == 3) + (dice5 == 3)
            if match >= 2:
                print("Two of a kind")

            else:
                match = (dice1 == 4) + (dice2 == 4) + (dice3 == 4)\
                        + (dice4 == 4) + (dice5 == 4)
                if match >= 2:
                    print("Two of a kind")

                else:
                    match = (dice1 == 5) + (dice2 == 5) + (dice3 == 5)\
                            + (dice4 == 5) + (dice5 == 5)
                    if match >= 2:
                        print("Two of a kind")

                    else:
                        match = (dice1 == 6) + (dice2 == 6) + (dice3 == 6)\
                                + (dice4 == 6) + (dice5 == 6)
                        if match >= 2:
                            print("Two of a kind")

                        else:
                            print("No two of a kind")


def dice_match_3():

    """
        rolling dice checking double mathing triple value
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice5 = random.randint(1, 6)

    print("Dice results are " + str(dice1), str(dice2), str(dice3),
          str(dice4), str(dice5))

    match = (dice1 == 1) + (dice2 == 1) + (dice3 == 1)\
        + (dice4 == 1) + (dice5 == 1)
    if match == 3:
        print("Three of a kind")

    else:
        match = (dice1 == 2) + (dice2 == 2) + (dice3 == 2)\
                + (dice4 == 2) + (dice5 == 2)
        if match >= 3:
            print("Three of a kind")

        else:
            match = (dice1 == 3) + (dice2 == 3) + (dice3 == 3)\
                    + (dice4 == 3) + (dice5 == 3)
            if match >= 3:
                print("Three of a kind")

            else:
                match = (dice1 == 4) + (dice2 == 4) + (dice3 == 4)\
                        + (dice4 == 4) + (dice5 == 4)
                if match >= 3:
                    print("Three of a kind")

                else:
                    match = (dice1 == 5) + (dice2 == 5) + (dice3 == 5)\
                            + (dice4 == 5) + (dice5 == 5)
                    if match >= 3:
                        print("Three of a kind")

                    else:
                        match = (dice1 == 6) + (dice2 == 6) + (dice3 == 6)\
                                + (dice4 == 6) + (dice5 == 6)
                        if match >= 3:
                            print("Three of a kind")

                        else:
                            print("No three of a kind")

"""
    Calling functions
"""
dice_match_2()
dice_match_3()
