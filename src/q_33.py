"""
After a hard day shopping, in a real shop, openly, on a street, taking this action entirely for
granted, you have decided to visit the local pub. Which you also take for granted.

An indeterminate amount of pints in, you realise you've hit the perfect peak for a spot of darts.
You pick up your arrows, make your way over to the board, and realise that it's staring you down.
Not one to shy away from a challenge, you decide to teach this dartboard a lesson and set yourself
a series of points targets. You realise that, while time outside seems to have stopped and the days
have blended into one, it might be useful to estimate how many darts you'll need to throw, just
in case.

Your game is naturally completely flawless, so what is the minimum number of darts will you need
to hit the exact score in your input, and in a separate game for each, every number on the way
there? You're just aiming to get a total number of points, not paying attention to any other
rules about e.g. finishing on a double.

A single dart can score all the numbers from 1 to 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

as well as the doubles and triples of those numbers on the double score and triple score segments,
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40
3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60

and in the bullseye:
25 50


For example, if your input is 30, you would play a game with point target 1, another with
point target 2, ..., all the way to a game with points target 30. Your answer will be 32 -
one dart for any number except 23 and 29, which require two each, through whatever
combination of available numbers.
"""
from functools import cache
from typing import List, Optional

input = 245701
possibles = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    2,
    4,
    6,
    8,
    10,
    12,
    14,
    16,
    18,
    20,
    22,
    24,
    26,
    28,
    30,
    32,
    34,
    36,
    38,
    40,
    3,
    6,
    9,
    12,
    15,
    18,
    21,
    24,
    27,
    30,
    33,
    36,
    39,
    42,
    45,
    48,
    51,
    54,
    57,
    60,
    25,
    50,
]


@cache
def darts_required(val: int) -> Optional[List[int]]:
    if val == 0:
        return []
    if val < 0:
        return None

    small: List[int] = []
    for v in possibles:
        if len(small) != 1:
            current = val - v
            result = darts_required(current)
            if result is not None:
                new_small = result + [v]
                if not small or len(new_small) < len(small):
                    small = new_small
    return small


def run() -> None:
    t = 0
    for i in range(1, input + 1):
        s = darts_required(i)
        if s:
            # print(i, len(s))
            t += len(s)
    assert t == 503234559


if __name__ == "__main__":
    run()
