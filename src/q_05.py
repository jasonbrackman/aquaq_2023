"""
In front of you are two dice. You know the numbers on the front, left, and top faces of each.
Through your exquisite knowledge of dice trivia, you are also aware the numbers on opposite faces of
a die add up to 7.

The faces are like so:

Dice 1:
  Front: 1
  Left:  2
  Top: 3

Dice 2:
  Front: 1
  Left:  3
  Top: 2


You're provided with a series of directions - up (U), down (D), left (L), or right (R), to spin the
current front face of each dice. If you spin the dice in the same direction at each step of the input
\"LRDLU\", the front faces after each of these five instructions would be:

Ins. Dice1 Dice2
0     5     4
1     1     1
2     3     2
3     5     4
4     1     1


Above, it's clear the front faces match after instruction indices 1 and 4 (starting from 0).

After spinning the dice according to your input instructions, what is the sum of the indices where the front
faces match? For the example above the answer would be 5, since the dice show a pair of ones after instruction
1 and instruction 4.
"""
import os
from typing import Literal

Side = Literal[1, 2, 3, 4, 5, 6]


class Die:
    MAGIC_OPPOSITE = 7

    def __init__(self, front: Side, left: Side, top: Side):
        self.front = front
        self.left = left
        self.top = top

    def turn_left(self):
        r_old = Die.MAGIC_OPPOSITE - self.left
        self.left = self.front
        self.front = r_old

    def turn_right(self):
        b_old = Die.MAGIC_OPPOSITE - self.front
        self.front = self.left
        self.left = b_old

    def turn_up(self):
        d_old = Die.MAGIC_OPPOSITE - self.top
        self.top = self.front
        self.front = d_old

    def turn_down(self):
        b_old = Die.MAGIC_OPPOSITE - self.front
        self.front = self.top
        self.top = b_old

    def __repr__(self):
        return f"Die({self.front=}, {self.left=}, {self.top=})"


def run() -> None:
    with open("./data/05_snake_eyes.txt", "r") as handle:
        instructions = handle.read()

    d1 = Die(1, 2, 3)
    d2 = Die(1, 3, 2)
    total = 0
    for index, i in enumerate(instructions):
        if i == "L":
            d1.turn_left()
            d2.turn_left()
        if i == "R":
            d1.turn_right()
            d2.turn_right()
        if i == "D":
            d1.turn_down()
            d2.turn_down()
        if i == "U":
            d1.turn_up()
            d2.turn_up()
        if d1.front == d2.front:
            total += index

    assert total == 10704


if __name__ == "__main__":
    os.chdir("..")
    run()
