"""
Run Length Encoding is a basic form of lossless compression - an array of data, or a
subset of the array, can be converted into a smaller subset (a run) which repeats some
number of times (a length). For example:

"ABCABCABCABCABC"

could become:

5 "ABC"

Here, 15 characters have been converted into an integer and 3 characters.

Your input contains a list of strings - they each contain a repeated sequence like the
one above, however there are some extra characters on the beginning and end. Once these
characters have been removed, what is the sum of the counts of the most repeated blocks
in each string?

For example:
"AAAAAAB"

could be broken down into 2 counts of "AAA", 3 counts of "AA" or 6 counts of "A" - thus
"A" is the most-repeated block and the answer for this string is 6. If your entire input
consisted of two copies of this string, the challenge answer would be 12.
"""
import os
import re
from collections import defaultdict, deque
from typing import List, Tuple, Dict



def parse() -> List[str]:
    lines = []
    with open(r'./data/13_o_rle.txt', 'r') as handle:
        for line in handle.readlines():
            lines.append(line.strip())
    return lines

pat01 = re.compile(r'^0{1,}|0{1,}$')
def foo(s: str) -> int:
    count = 0

    possible = ''
    # check from start of queue
    stack = deque(list(s[:len(s)//2]))
    while stack:
        possible += stack.popleft()
        new = s.replace(possible, '0')
        m = re.findall(pat01, new)
        if m:
            len_m = len(m[0])
            if len_m > count:
                count = len_m

    # check from end of queue
    possible = ''
    stack = deque(list(s[len(s)//2:]))

    while stack:
        possible = stack.pop() + possible
        new = s.replace(possible, '0')
        m = re.findall(pat01, new)
        if m:
            len_m = len(m[0])
            if len_m > count:
                count = len_m
    return count


def run() -> None:
    items = parse()
    r = sum(foo(x) for x in items)
    assert r == 1462

if __name__ == "__main__":
    os.chdir("..")
    run()
