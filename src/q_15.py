"""
As a child, nothing is more difficult and mysterious than the game which apparently has no name, but goes like this:

You have a starting word, and an ending word - changing one letter at a time and always maintaining a real word,
make a chain of words from the start to the end. For example:
fly
...
try

Results in
fly
fry
try

This results in a chain three words long, including the starting and ending words.

Using the word list here as a list of valid words, find the shortest full chain of each word pair in the input.
The answer is the product of the lengths of each chain - so if the input was
fly,try
try,fly
word,maze

The lengths of each chain would be 3 3 5, and the product of these would be the answer: 45.
"""
import math
import os
import string
from collections import deque
from typing import List, Tuple, Set


def get_word_games() -> List[Tuple[str, ...]]:
    with open(r"./data/15_word_wore_more_mare_maze.txt", "r") as handle:
        word_games = [tuple(line.strip().split(",")) for line in handle.readlines()]
    return word_games


def get_word_set() -> Set[str]:
    with open(r"./data/15_words.txt", "r") as handle:
        word_set = {r.strip().lower() for r in handle.readlines()}
    return word_set


def bfs(start: str, end: str, words: Set[str]):
    visited = set()
    queue = deque([(start, 1)])
    while queue:
        node, depth = queue.popleft()
        if node == end:
            return depth

        for index in range(len(start)):
            temp = list(node)
            for c in string.ascii_lowercase:
                temp[index] = c
                s_temp = "".join(temp)
                if s_temp not in visited and s_temp in words:
                    queue.append((s_temp, depth + 1))
                    visited.add(s_temp)

    return None


def run() -> None:
    word_list = get_word_set()
    word_games = get_word_games()
    scores = []
    for a, b in word_games:
        depth = bfs(a.strip(), b.strip(), word_list)
        scores.append(depth)
    assert math.prod(scores) == 97920000


if __name__ == "__main__":
    os.chdir("..")
    run()
