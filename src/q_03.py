"""
You're in an oddly shaped room, there are squares on the floor and you move one square at a time.

The room looks like this:

  ##
 ####
######
######
 ####
  ##

This is a six-by-six area defined in indices from 0 to 5 on each axis.
You start in the first # in the top row, or position 0 2 in indices, and receive a series of instructions to step
up (U) left (L) right (R) or down (D) on the map above. You can't step outside the # - if you're given an instruction
to do so, ignore it, and move on to the next instruction.

For example, with input UDRR, you eventually run out of instructions at position 1 4.

After processing all the movements in your input, what is the sum of the indices of each position you finished on
at each step (including steps where you did not move)?

For example, with input UDRR, you would start on 0 2, stay on 0 2 then move through 1 2, 1 3 and 1 4. The sum of
these positions is 14 - the first position is not counted.
"""

from typing import Tuple, List, Set

Vec2 = Tuple[int, int]

compass = {
    # Pos  y, x
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def parse() -> Set[Vec2]:
    grid = [
        list("  ##"),
        list(" ####"),
        list("######"),
        list("######"),
        list(" ####"),
        list("  ##"),
    ]
    valid_positions = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                valid_positions.add((y, x))
    return valid_positions


def add_vec2(v1: Vec2, v2: Vec2) -> Vec2:
    y = v1[0] + v2[0]
    x = v1[1] + v2[1]
    return y, x


def calculate_steps(island: Set[Vec2], moves: List[str], current: Vec2) -> int:
    total = 0
    for move in moves:
        temp = add_vec2(current, compass[move])
        if temp in island:
            current = temp
        total += sum(current)

    return total


def run() -> None:
    island = parse()

    with open(r"./data/03_short_walks.txt", "r") as handle:
        steps = list(handle.read())
    assert calculate_steps(island, steps, (0, 2)) == 2543


if __name__ == "__main__":
    run()
