"""
It's late in the day, and you've just finished a rousing session of AquaQ challenges. Looking at the clock,
you realise it's exactly one minute until your spouse gets home, and you promised them you would vacuum the
floor, which is currently covered in the debris of a week-long problem-solving session.

You note the hallway floor is covered in a grid of square tiles, and is 20 tiles wide and 500 long. Each
tile is covered in a certain amount of dust motes. Quickly you estimate this coverage as relative integers,
and note them as your input. Your vacuum cleaner attachment is 5 tiles wide, and for an effective cleaning
action, you have to run it so it exactly covers whole tiles. You have time for exactly one pass down the
hallway, and can move your vacuum cleaner left or right one tile at a time, or continue straight, as you
move forward one tile at a time.

In your single pass down the hallway, starting from any tile on the first row and moving the whole way down,
how many motes of dust can you collect, assuming you clean all the dust from each tile?

For an example hallway, with a cleaner width of 3 tiles:
3 4 5 1 3
9 3 4 0 9
4 5 4 4 7
3 7 9 8 2

You can sweep the following tile path to maximise collected motes:
[3 4 5] 1 3
[9 3 4] 0 9
4 [5 4 4] 7
3 [7 9 8] 2

total: 65
"""
import os
from queue import PriorityQueue
from typing import List, Tuple, Iterator

WIDTH = 5
ROW_COUNT = 20

def parse() -> List[List[int]]:
    with open(r"./data/21_clean_sweep.txt", "r") as f:
        rows = [[int(r) for r in line.split()] for line in f.readlines()]

    windows = []
    for row in rows:
        windows.append(
            [
                sum(row[i : i + WIDTH])
                for i in range(ROW_COUNT)
                if len(row[i : i + WIDTH]) == WIDTH
            ]
        )

    return windows


def _get_neighbours(
    cost: int, index: int, data: List[int]
) -> Iterator[Tuple[int, int]]:
    for item in (index - 1, index, index + 1):
        if 0 <= item < len(data):
            yield cost - data[item], item


def bfs() -> int:
    lowest = 0
    rows = parse()
    pq: PriorityQueue[Tuple[int, int, int]] = PriorityQueue()
    for index, cost in enumerate(rows[0]):
        pq.put((cost * -1, 0, index))
    v = set()
    while not pq.empty():
        cost, row, index = pq.get()

        if (
            cost - (len(rows) - 1 - row) * 336  # 336 avg of the max value possible per row
        ) > lowest:
            continue

        if row >= len(rows) - 1:
            if cost < lowest:
                lowest = cost

        else:
            for n_cost, n_index in _get_neighbours(cost, index, rows[row + 1]):
                item = n_cost, row + 1, n_index
                if item not in v:
                    v.add(item)
                    pq.put(item)

    return lowest * -1


def run() -> None:
    r = bfs()
    assert r == 143487, r


if __name__ == "__main__":
    os.chdir("..")
    run()
