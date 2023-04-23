"""
Word snakes, while not as cool as their reptilian counterparts, are still undoubtedly the coolest way
to represent a string of words, right?

They look like this:

                roulette
                e      l
                v      e
                e      c
                netulg t
    invalidly        n i
            a        i o
            c        y n
            h        r sharpness
            t        r
            i        u
            n        c
            grumpiness

In case you disagree re: the aforementioned coolness, the words used in this word snake are:


invalidly
yachting
grumpiness
scurrying
gluten
never
roulette
elections
sharpness


To find the answer to this challenge, take this disagreement to the next level and find all the
words in the snakes in your challenge input. Once the words have been found, your answer is the
sum of the value of each of the words. The value of a word is found by getting the letter values
of that word (a=1, b=2, etc), summing them, and multiplying by the count of letters in the word.

For the above snake, the answer would be 7995. There is more than one snake in your input - the answer
is the sum of all values of all words.
"""
import os
import string
from typing import List, Tuple, Dict, Set


def parse() -> List[List[str]]:
    lines = []
    with open(r"./data/27_snake_eater.txt", "r") as handle:
        for line in handle.readlines():
            lines.append(list(line))
    return lines


def positions(lines: List[List[str]]) -> Dict[Tuple[int, int], str]:
    ps = dict()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] not in (" ", "\n"):
                ps[(row, col)] = lines[row][col]
    return ps


def neighbours(
    k: Tuple[int, int], poss: Dict[Tuple[int, int], str]
) -> List[Tuple[int, int]]:
    ns = []
    for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        row = k[0] + n[0]
        col = k[1] + n[1]
        if (row, col) in poss:
            ns.append((row, col))

    return ns


def word_cost(word: str) -> int:
    return sum(string.ascii_lowercase.find(c) + 1 for c in word) * len(word)


def run() -> None:
    lines = parse()
    poss = positions(lines)

    tips = [k for k, v in poss.items() if len(neighbours(k, poss)) == 1]
    visited: Set[Tuple[int, int]] = set()

    results: List[str] = []
    snakes = []
    while tips:
        snakes.append("".join(results).split())
        results.clear()
        key = tips.pop()
        if key in visited:
            continue
        direction = key
        new = neighbours(key, poss)
        results.append(poss[key])
        visited.add(key)

        vrow_ = False
        hcol_ = False
        while new:
            new_key = new.pop()
            if new_key not in visited:
                visited.add(new_key)
                switch, vrow_, hcol_ = direction_control(
                    direction, new_key, vrow_, hcol_
                )
                if switch:
                    last_letter = results[-1]
                    results.append(" ")
                    results.append(last_letter)
                    direction = new_key

                results.append(poss[new_key])
                new = neighbours(new_key, poss)

    t = 0
    for snake in snakes:
        t += sum(word_cost(word) for word in snake)
    assert t == 500135


def direction_control(
    direction: Tuple[int, int], new_key: Tuple[int, int], vrow_: bool, hcol_: bool
) -> Tuple[bool, bool, bool]:
    vrow, hcol = abs(direction[0] - new_key[0]), abs(direction[1] - new_key[1])
    switch = False
    if vrow == 1 and not vrow_:
        switch = True if True in (vrow_, hcol_) else False
        vrow_ = True
        hcol_ = False

    elif hcol == 1 and not hcol_:
        switch = True if True in (vrow_, hcol_) else False
        hcol_ = True
        vrow_ = False
    return switch, vrow_, hcol_


if __name__ == "__main__":
    os.chdir("..")
    run()
