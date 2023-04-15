"""
Today we hunt the most dangerous game: cellular automata.

Cellular automata are on-off (or living-dead) states in each cell on a grid which iterate
step-by-step depending only on the current state of each cell and its neighbours. Here,
neighbours are considered the cell above, below, left, and right of the current cell -
no diagonals. The rules for iteration in this system are as follows:

If a cell has an even number of surrounding "on" states, it should be set to (or remain) off.
If a cell has an odd number of surrounding "on" states, it should be set to (or remain) on.
Points outside the boundary are considered to be "off".

Your input is multiple sets of run times, square grid widths, and the matrix index pairs of
starting cells (0,0 is the top left corner, etc)

For each input row, after constructing the start state and running for the required number
of steps, you need to find how many are alive.

For example, with input:
350 6 2 2 2 3

First construct a grid with width and height 6, and set points (2,2) and (2,3) as "on":

......
......
..##..
......
......
......

This is the state at time 0. For times 1, 2, and 3 we iterate as below:

......
..##..
.####.
..##..
......
......

..##..
......
##..##
......
..##..
......

.####.
######
######
######
.####.
..##..


After 350 steps, we arrive at this state

.#..#.
......
.#..#.
......
#.##.#
......

For this input, the answer is 8.
What is the sum of the living cells after the required run time for each input?
"""
import os
import sys
from typing import List, Tuple, Dict, Set

Vec2 = Tuple[int, int]


class Automata:
    def __init__(self, run_time: int, width: int, positions: Set[Vec2]) -> None:
        self.run_time = run_time
        self.width = width

        self.keys: List[Vec2] = [
            (y, x) for x in range(self.width) for y in range(self.width)
        ]
        self.values = positions
        self.cache: Dict[tuple[Vec2, ...], Set[Vec2]] = dict()

    def spin(self) -> int:
        """
        If a cell has an even number of surrounding "on" states, it should be set to (or remain) off.
        If a cell has an odd number of surrounding "on" states, it should be set to (or remain) on.
        Points outside the boundary are considered to be "off".
        """

        for index in range(self.run_time):
            temp = tuple(self.values)
            if temp in self.cache:
                self.values = self.cache[temp]
            else:
                self.values = self.get_new_positions()
                self.cache[temp] = self.values

        return len(self.values)

    def new_pos(self, p1: Vec2, p2: Vec2) -> bool:
        y = p1[0] + p2[0]
        x = p1[1] + p2[1]
        return (y, x) in self.values

    def get_new_positions(self) -> Set[Vec2]:
        new_keys = set()
        for p1 in self.keys:
            count = sum(
                self.new_pos(p1, p2) for p2 in ((-1, 0), (1, 0), (0, -1), (0, 1))
            )
            if count % 2 != 0:
                new_keys.add(p1)
        return new_keys


def run() -> None:
    automatas = parse()
    total = sum(automata.spin() for automata in automatas)
    assert total == 2481


def parse() -> List[Automata]:
    automatas = []
    with open(r"./data/19_its_alive.txt", "r") as handle:
        for line in handle.readlines():
            # run times, square grid widths, and the matrix index pairs of
            # starting cells (0,0 is the top left corner, etc)
            run_time, width, *pos = line.strip().split()
            automatas.append(
                Automata(
                    int(run_time),
                    int(width),
                    {(int(pos[i]), int(pos[i + 1])) for i in range(0, len(pos), 2)},
                )
            )
    return automatas


if __name__ == "__main__":
    os.chdir("..")
    run()
