"""
After watching approximately 15 minutes of daytime television, you're overcome with the
irresistible urge to play bingo. You decide to play alone to hide your shame at being 
seduced by ads on TV, and start with the US standard game, using the 5x5 number grid below:

6  17 34 50 68
10 21 45 53 66
5  25 36 52 69
14 30 33 54 63
15 23 41 51 62

In this game, you win when you get all the numbers in a:
 - row, 
 - column or 
 - diagonal. 
 
 So for example, if the numbers 10 5 21 45 53 70 66 4 were called, your game would be over as 
soon as 66 was called - the game is ended in 7 turns, because you are the only player.
The input attached is a list of called number sequences. What is the sum of the amount 
of numbers it takes in each row to end the game? If the above input was repeated 4 times, 
the answer would be 28.
"""
import os
from typing import List, Set, Dict


class Card:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.nums: Set[int] = set()

    def horizontals(self) -> bool:
        for row in self.grid:
            if all(col in self.nums for col in row):
                return True
        return False

    def verticals(self) -> bool:
        for index in range(len(self.grid)):
            transposed = [row[index] for row in self.grid]
            if all(col in self.nums for col in transposed):
                return True
        return False

    def diagonals(self) -> bool:
        lr = [self.grid[i][i] for i in range(len(self.grid))]
        rl = [self.grid[i][j] for i, j in enumerate(range(len(self.grid) - 1, -1, -1))]
        if all(col in self.nums for col in lr):
            return True
        if all(col in self.nums for col in rl):
            return True
        return False


def parse() -> Dict[int, List[int]]:
    nums: Dict[int, List[int]] = dict()
    with open(r"./data/14_thats_a_bingo.txt", "r") as handle:
        for index, line in enumerate(handle.readlines()):
            nums[index] = [int(i) for i in line.split()]
    return nums


def run() -> None:
    grid = [
        [6, 17, 34, 50, 68],
        [10, 21, 45, 53, 66],
        [5, 25, 36, 52, 69],
        [14, 30, 33, 54, 63],
        [15, 23, 41, 51, 62],
    ]
    t = 0
    card = Card(grid)
    current = -1
    tests = parse()
    for k, values in tests.items():
        if k != current:
            current = k
            card.nums.clear()
        for index, value in enumerate(values, 1):
            card.nums.add(value)
            if card.horizontals() or card.verticals() or card.diagonals():
                t += index
                break
    assert t == 4327


if __name__ == "__main__":
    os.chdir("..")
    run()
