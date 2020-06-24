"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def findSame(dice: list):
    s = sorted(dice.copy())
    count_left = s.count(s[0])
    count_right = s.count(s[-1])
    return s, count_left, count_right


def score(dice, category):
    result = 0
    sorted_dice, r1, r2 = findSame(dice)
    for i in dice:
        if category == "ONES":
            if i == 1:
                result += 1
        elif category == "TWOS":
            if i == 2:
                result += 2
        elif category == "THREES":
            if i == 3:
                result += 3
        elif category == "FOURS":
            if i == 4:
                result += 4
        elif category == "FIVES":
            if i == 5:
                result += 5
        elif category == "SIXES":
            if i == 6:
                result += 6
    if category == "FULL_HOUSE":
        if r1 == 3 and r2 == 2 or r1 == 2 and r2 == 3:
            result = sum(dice)
        else:
            result = 0

    elif category == "FOUR_OF_A_KIND":
        if r1 >= 4:
            result = 4 * sorted_dice[0]
        elif r2 >= 4:
            result = 4 * sorted_dice[-1]
        else:
            result = 0

    elif category == "LITTLE_STRAIGHT":
        if sorted_dice == [1, 2, 3, 4, 5]:
            result = 30
        else:
            result = 0

    elif category == "BIG_STRAIGHT":
        if sorted_dice == [2, 3, 4, 5, 6]:
            result = 30
        else:
            result = 0

    elif category == "CHOICE":
        result = sum(dice)

    elif category == "YACHT":
        if r1 == 5:
            result = 50
        else:
            result = 0

    return result
