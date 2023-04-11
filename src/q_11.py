"""
You've been presented with the plans for an avant-garde method of tiling floors.

You have a list of values which represent the lower-left and upper-right corner co-ordinates
of a series of rectangular tiled areas, where one tile is equal to one square unit.
The designer then specifies that he doesn't want any areas that don't overlap others included
in the final plan - if an area doesn't directly overlap with another, disregard it entirely. In
the resulting set of areas, some tiles overlap - since there's no point in placing more than one
tile per spot, so how many tiles do you need total to complete the plan?

For example, if you were provided with these three tiled areas:
lx,ly,ux,uy
0,0,3,3
2,2,4,5
6,3,8,7

The direct map would look like this, with (0,0) in the bottom left corner:
      ##
      ##
  ##  ##
  ##  ##
##@#
###
###


There is an overlap of two tiles in the square bounded by (2,2) and (3,3), and the tiles at the top right
 are not connected to any other tiles. In this case the total number of required tiles is 14.
"""
import os
from collections import defaultdict
from typing import Dict, Tuple, List

Points = List[Tuple[int, int, int, int]]
PointsCached = Dict[Tuple[int, int], int]


def iter_parse() -> Points:
    with open(r"./data/11_boxed_in.txt", "r") as handle:
        lines = iter(handle.readlines())
        _header = next(lines)

    points = []
    for line in lines:
        x1, y1, x2, y2 = line.strip().split(",")
        points.append((int(x1), int(y1), int(x2), int(y2)))

    return points


def cached_used(points: Points) -> PointsCached:
    used: Dict[Tuple[int, int], int] = defaultdict(int)
    for x1, y1, x2, y2 in points:
        for y in range(y1, y2):
            for x in range(x1, x2):
                used[(y, x)] += 1
    return used


def remove_islands(points: Points, points_cached: PointsCached) -> int:
    t = 0
    for x1, y1, x2, y2 in points:
        r = 0
        keep = False
        for y in range(y1, y2):
            for x in range(x1, x2):
                r += 1
                if points_cached[(y, x)] > 1:
                    keep = True

        if keep is False:
            t += r
    return t


def run() -> None:
    points = iter_parse()
    all_points = cached_used(points)
    unused = remove_islands(points, all_points)
    assert len(all_points) - unused == 216


if __name__ == "__main__":
    os.chdir("..")
    run()
