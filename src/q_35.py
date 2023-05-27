"""
Wandering around the train station, waiting for several decades of timetable backlog to clear,
you find some books on a table. The perfect way to pass the time! Picking up the first book
you see what looks like a jumble of letters, instead of a story. In fact, all the books
look like this, and there are no titles on the covers either. Someone has left a note next
to the books, mercifully in plain text:
"These are encrypted with a columnar transposition cipher".

Cryptic but useful. Since you have so much time, you decide to work through decrypting these
books, but you're missing one particular piece of information - the code word. You think back
to what you know on columnar transposition ciphers.

To make a columnar transposition cipher, take a body of text:

WE ARE DISCOVERED FLEE AT ONCE


and a code-word:

GLASS


Chop the text into lengths equal to the length of the code word (5 letters, in this case),
padding the end of the plaintext if necessary:

WE AR
E DIS
COVER
ED FL
EE AT
 ONCE


(Note that usually spaces and punctuation would be removed, but since we want to recover
the original plaintext of the book in full, we won't do that here)

Then use the code word to generate a selection order for the columns. The selection order is
the order the letters in the word would take if they were sorted alphabetically.
For example

G L A S S

becomes

1 2 0 3 4


as A is the first alphabetical letter, G the second, L the third and S is both the fourth and
fifth. Ties are broken by position in the original word, so

L E V E R

becomes

2 0 4 1 3


since both Es can't be 0, the second E becomes 1. A third E would become 2 and all other letters
would increase by one, etc.

Taking this column order, apply to the columns:

12034
WE AR
E DIS
COVER
ED FL
EE AT
 ONCE


And pull the columns out in that order, converting to lines:

 DV  N
WECEE
E ODEO
AIEFAC
RSRLTE


And then collapse into a single string:

 DV  NWECEE E ODEOAIEFACRSRLTE


Your input is a section from one of the books, as a ciphertext (a "#" has been added to the
end of this to note the end position of the ciphertext - feel free to remove it). You have
a handy list of words here, which will contain the code word. What is the code word used
to encrypt the text in your input?

"""
import string
from typing import List


# 1 - take a body of text
# 2 - and a code word
# 3 - split the body into columns matching the length of the key, padding if necessary.

Blocks = List[List[str]]

def pad_blocks(text: str, length: int) -> Blocks:
    """
    Take the string and a key and split it into coloumns matching the length of the key.
    Padding may be added to ensure that all splits are equal length.
    """
    # key_length = len(key)
    results = []
    result: List[str] = []
    for index, character in enumerate(text):
        if index % length == 0:
            if result:
                results.append(result[::])
            result.clear()
        result.append(character)
    if result:
        result += [] * (len(result) - length)
        results.append(result[::])
    return results


def _key_order(key: str) -> List[str]:
    digits = list(key)
    for index, character in enumerate(sorted(key)):
        key_index = key.index(character)
        digits[key_index] = index
        key = key.replace(character, '*', 1)
    return digits


def twist(blocks: Blocks, key_order: List[int]) -> str:
    result = ''
    for index in range(len(key_order)):
        current = key_order.index(index)
        result += ''.join([line[current] for line in blocks])
    return result


def untwist(blocks: Blocks, key_order: List[int]) -> str:
    new_blocks = []
    new = []
    for index in range(len(blocks[0])):
        for new_block in blocks:
            if index >= len(new_block):
                new.append(' ')
            else:
                new.append(new_block[index])
        new_blocks.append(new[::])
        new.clear()

    result = ''
    for new_block in new_blocks:
        result += ''.join([new_block[i] for i in key_order])

    return result

def encryption_test() -> None:
    text = "WE ARE DISCOVERED FLEE AT ONCE"
    key = "GLASS"
    print(f'Original:  [{text}]')
    key_order = _key_order(key)
    blocks = pad_blocks(text, len(key))

    twisted = twist(blocks, key_order)

    print(f'Encrypted: [{twisted}]')
    blocks = pad_blocks(twisted, len(twisted) // len(key))
    untwisted = untwist(blocks, key_order)
    print(f'Decrypted: [{untwisted}]')

def score_text(message: str, words: List[str]) -> int:
    return sum([word in message for word in words])

def run() -> None:
    encryption_test()

    with open('../data/35_problem_input.txt', 'r') as f:
        problem = f.read()
        problem = problem[:-1]

    with open('../data/35_word_list.txt', 'r') as f:
        keys = [key.strip() for key in f.readlines()]
    with open('../data/35_word_score.txt', 'r') as f:
        words = [w.strip() for w in f.readlines()]

    problem_len = len(problem)
    results = []
    visited = set()
    for key in keys:
        key_order = _key_order(key)
        if str(key_order) not in visited:
            visited.add(str(key_order))
            blocks = pad_blocks(problem,  problem_len // len(key))
            untwisted = untwist(blocks, key_order)
            if untwisted[0] in string.ascii_uppercase:
                results.append((score_text(untwisted, words), key))
    results.sort()
    assert results[-1][1] == "nonsense"


if __name__ == "__main__":
    run()