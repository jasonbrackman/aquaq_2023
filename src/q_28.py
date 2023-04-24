"""
In the continuing series of highly practical methods of encrypting information, we're going to use
a hall of rotating "mirrors" to encode basic messages.

The encryption maps used are birds-eye views of a hall of mirrors, like the one below:

 ABCD
A\  /A
B /\ B
C/ \ C
D/ / D
 ABCD


To encrypt, look down the left side for the current letter being encrypted, and start moving right
from that letter. Change direction by reflecting from the slashes as if they were mirrors, e.g:
 /-->
 |
 \-\
   |
->-/


After each individual reflection in your path, change the orientation of the mirror you just bounced off -
forward slashes become backslashes and vice versa. Follow the path until any letter is reached, which is
the encrypted output of the input letter. Then, continue with encryption on the next letter (if any remain)
using the map in its current, altered, state.

For example, encrypting the word "DAD" proceeds as below:
"D"
 Path   Output map
 ABCD      ABCD
A\  /A    A\  /A
B /\ B    B /\ B
C834 C    C/ / C
D765 D    D/ \ D
 ABCD      ABCD

Output: "C" (note position 1 and 7 and position 2 and 8 overlap, before the left turn out of the map)

"A"
 Path   Output map
 ABCD      ABCD
A1  /A    A/  /A
B2/\ B    B /\ B
C3 / C    C\ / C
D/ \ D    D/ \ D
 ABCD      ABCD
Output: "C"

"D"
 Path   Output map
 ABCD      ABCD
A/  /A    A/  /A
B /\ B    B /\ B
C2 / C    C/ / C
D1 \ D    D\ \ D
 ABCD      ABCD
Output: "C"


So the final encrypted string in this example is "CCC".

Your map of mirrors is in the input below, use it to encrypt the word "FISSION_MAILED"

The encrypted output string is the answer to this challenge.
"""
import os
import string
from typing import Tuple, Dict

Pad = Dict[Tuple[int, int], str]

DIRS = {
    "up": (-1, 0),
    "dn": (1, 0),
    "lt": (0, -1),
    "rt": (0, 1),
}


def parse() -> Pad:
    with open(r"./data/28_hall_of_mirrors.txt", "r") as handle:
        pad = dict()
        for i1, line in enumerate(handle.readlines()):
            for i2, c in enumerate(line.strip("\n")):
                pad[(i1, i2)] = c

    return pad


def encode(msg: str, pad: Pad) -> str:
    results = ""
    starts = {pad[(a, b)]: (a, b) for (a, b) in pad if b == 0}

    for m in msg:
        direction = DIRS["rt"]
        s = starts[m]
        q = [(s[0] + direction[0], s[1] + direction[1])]
        while q:
            next_ = q.pop()
            if pad[next_] in string.ascii_uppercase + "_0123456789":
                results += pad[next_]
                q.clear()
                continue
            if pad[next_] in "\/":
                # get direction - can stay the same
                if direction == DIRS["rt"]:
                    direction = DIRS["up"] if pad[next_] == "/" else DIRS["dn"]
                elif direction == DIRS["lt"]:
                    direction = DIRS["dn"] if pad[next_] == "/" else DIRS["up"]
                elif direction == DIRS["up"]:
                    direction = DIRS["rt"] if pad[next_] == "/" else DIRS["lt"]
                elif direction == DIRS["dn"]:
                    direction = DIRS["lt"] if pad[next_] == "/" else DIRS["rt"]

                # Mirror flip
                pad[next_] = "/" if pad[next_] == "\\" else "\\"
            q.append((next_[0] + direction[0], next_[1] + direction[1]))

    return results


def run() -> None:
    pad = parse()
    assert encode("FISSION_MAILED", pad) == "EZ3NHAZGBNOFIB"


if __name__ == "__main__":
    os.chdir("..")
    run()
