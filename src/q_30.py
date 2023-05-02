"""
In a moment of madness, you have decided coding challenges are not enough, and so you have decided to
play a card game.

This game consists of dealing out a random number of cards (from any number of decks), which have
been mixed to include face-up (1) and face-down (0) cards. A deal from the deck might look like this:
1010010b

Each step of the game involves removing a face-up card and flipping over any cards immediately adjacent
to it. The empty space left behind is never refilled. The game ends when the cards have either been
removed entirely (in which case, you win!) or no valid moves remain.

A simple game could progress like so, with a "." in place of a removed card:
11010
111.1
10..1
.1..1
....1
.....


The game ends in 5 turns, after which there are no cards left. The game could also end in failure:
11010
0.110
0..00


Here, removing the second card leaves the first in a state where it can be neither moved nor flipped.
Of the three starting face-up cards, either the left-most or right-most could be chosen while leaving
the game in a state where it can be won.

Naturally, you have decided to solve this game - or at least the first step. With a set of dealt hands
each represented by a single line of face-up or face-down cards, you can find out how many cards are
valid first moves. For example:
11010        -> 2 (positions 0, 3)
110          -> 0
00101011010  -> 3 (positions 2, 6, 9)


For a total of 5 valid starting positions for the set.
Treating your input as a set of dealt hands, work out how many valid starting positions are in that set.
"""
import os
import re
import sys
from functools import cache
from typing import List

pattern = r"0*(1+)0*"

# set the new recursion depth limit
sys.setrecursionlimit(3000)  # set to the desired limit


def parse() -> List[str]:
    with open(r"./data/30_flip_out.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


@cache
def can_flip(val: str) -> int:
    if "1" == val:
        return 1
    if "1" not in val:
        return 0
    items = re.findall(pattern, val)
    if len(items) == 1 and len(items[0]) <= 2:
        return 0 if len(items[0]) % 2 == 0 else 1
    t = 0
    for index, c in enumerate(val):
        r = 0
        if c == "1":
            s = list(val)
            s[index] = "."

            if index - 1 >= 0:
                current = s[index - 1]
                if current == "1":
                    s[index - 1] = "0"
                elif current == "0":
                    s[index - 1] = "1"

            if index + 1 < len(s):
                current = s[index + 1]
                if current == "1":
                    s[index + 1] = "0"
                elif current == "0":
                    s[index + 1] = "1"

            # very slow for the last 8 numbers :(
            r = all(can_flip(t) for t in "".join(s).split(".") if t)
        if r:
            t += 1

    return t


def run() -> None:
    lines = parse()
    t = 0
    for index, line in enumerate(lines):
        for _ in range(7):
            # first optimization is to remove repeating zeroes.
            line = line.replace("00", "0")
        t += can_flip(line)
        # print(index, t)
    assert t == 8069, t


if __name__ == "__main__":
    os.chdir("..")
    run()
