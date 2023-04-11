"""
Nothing is more exciting than a bracing bout of typography.

Like most people, I am commonly unable to sleep because of the knowledge that some letters around me are poorly
spaced. Today, this problem will be remedied for the equally-common occurrence of ascii art words. An alphabet
of these words is found in 16_ascii_letters.txt.

Kerning is the process of correctly spacing letter pairs to make use of the white-space surrounding each letter.
For example, if I was joining the letters L and T together from the above alphabet and putting a space between
them, without kerning, it would look like this:

#..... #####
#........#..
#........#..
#........#..
#........#..
######...#..

All that wasted space between the top of the L and the top of the T is frankly offensive. The rule that should
be used to join these together is to move the letters closer together until the nearest horizontal points
between them are separated by a single space (filled with dots in this case to show spacing). For example, the
L and T following this rule would look like:

#....#####
#......#..
#......#..
#......#..
#......#..
######.#..

The T has been moved closer to the L until there is only one space between them at the closest point, and there
is no overlap.

After drawing a box around this resulting combination of letters which just encompasses all the "#", we can see
there are 51 spaces before applying kerning, and 39 after. Subsequent letters would be joined onto this "LT"
combination in exactly the same way, following the single-space rule, and treating the LT as a single character -
for example "LTA" would use some of the space under the right edge of the T, and would end up looking like:

#....#####.##..
#......#..#..#.
#......#.#....#
#......#.######
#......#.#....#
######.#.#....#

Using a total of 53 spaces.

Convert your input string into the appropriate ASCII characters in the above link, and join them together while
applying the kerning rule - what is the total number of empty spaces in the resulting set of strings?
"""
import os
import re
import string
from typing import List, Dict

DOTR_PATTERN = re.compile(r"\.+$")
DOTL_PATTERN = re.compile(r"^\.+")


def get_instructions() -> str:
    with open(r"./data/16_keming.txt", "r") as handle:
        s = handle.read()
    return s.strip()


def character_blocks() -> Dict[str, List[str]]:
    wh = 6
    with open(r"./data/16_ascii_letters.txt", "r") as handle:
        lines = [
            line.replace(" ", ".").strip().ljust(wh, ".") for line in handle.readlines()
        ]
        groups: List[List[str]] = [lines[i : i + wh] for i in range(0, len(lines), wh)]

        for index, group in enumerate(groups):
            longest = 0
            for line in group:
                where = line.rindex("#")
                if where > longest:
                    longest = where
            if longest == wh - 1:
                continue
            else:
                groups[index] = [line[: longest + 1] for line in group]

    return dict(zip(string.ascii_uppercase, groups))


def character_spaces(block: List[str]) -> int:
    return sum(row.count(".") for row in block)


def calculate_space_removal(left, right) -> int:
    col_height = 6
    right_width = how_close(left, DOTR_PATTERN)
    left_width = how_close(right, DOTL_PATTERN)
    for i in range(col_height):
        col_totals = []
        for a, b in zip(right_width, left_width):
            s = sum((a, b - i))
            col_totals.append((a, b - i, s))

        # Exit early if we can
        if any(z == 0 for (x, y, z) in col_totals):
            return -col_height

        # find out if we have a number to work with to squeeze the letters together.
        for l, r, t in col_totals:
            if t == 1:
                return i * col_height
    return -col_height


def how_close(x: List[str], pattern: re.Pattern):
    result = []
    for line in x:
        found = re.findall(pattern, line)
        if found:
            result.append(found[0].count("."))
        else:
            result.append(0)
    return result


def run() -> None:
    blocks = character_blocks()
    instructions = get_instructions()

    # pprint(instructions, blocks)
    total = 0
    c1 = None
    for item in instructions:
        if c1 is None:
            c1 = blocks[item]
            t1 = character_spaces(c1)
            total += t1
        else:
            c2 = blocks[item]
            t2 = character_spaces(c2)
            remove = calculate_space_removal(c1, c2)
            total += t2 - remove
            c1 = c2
    assert total == 246882


if __name__ == "__main__":
    os.chdir("..")
    run()
