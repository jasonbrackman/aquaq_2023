"""
The best way to confound would-be snoops is to use cryptography. Nothing fancy though,
they'll be expecting that, so we're using the finest the 1850s has to offer: the
Playfair cipher.

This cipher starts with a keyword, which is reduced to the first distinct occurrence of
each letter of the alphabet within that word (removing any spaces if necessary). Then
all remaining letters of the alphabet (except j) are joined on. The resulting 25 letter
string is cut into a 5x5 grid. For example key word "playfair", this results in:

playf
irbcd
eghkm
noqst
uvwxz

The plain text to be encrypted is prepared for lookup in the grid by removing all
spaces, splitting repeat letters with "x", padding the string length to the nearest
multiple of two (again with "x"), and splitting into two-letter pairs. For example
string, "tree":

tree     //input
trexe    //split double letters
trexex   //pad
tr ex ex //split into bigrams

The position of each component of each letter pair is then found in the grid, and
encrypted according to the following rules:

1. If the two letters are in the same row, the new letters are the letters directly to
the right of the input letters (wrapping around if necessary)
2. If the two letters are in the same column, the new letters are the letters directly
below the input letters (wrapping as above)
3. If the letters are separated diagonally, they form the corners of a "box". The
encrypted letters are the letters on the laterally opposite end of this box to the
input (i.e. look to the far left or right of the input while staying within the box)


For example, if the input text was the word "flawless", this becomes "fl aw le sx sx",
which is encoded in the following way:

"fl" -> "pa"
//on the same row, so the letter to the right
"aw" -> "ba"
//on the same column, so the letter below
"le" -> "pg"
//opposite corners of the square from "l" to "e" in the code square
"sx" -> "xy" (x2)


Your input is text encrypted with this method, using the keyword "power plant" - what
is the prepared plaintext from this ciphertext? (The answer will contain no "j"s, no
spaces, and may be blocks with "x"s).
"""

import re
from string import ascii_lowercase
from typing import List

PATTERN = re.compile(r"(.)\1")


def _create_key_cypher(key: str) -> List[str]:
    cypher = ""
    for c in key.replace(" ", "") + ascii_lowercase:
        if c != "j" and c not in cypher:
            cypher += c
    return [cypher[i : i + 5] for i in range(0, len(cypher), 5)]


def decrypt_playfair(message: str, key: str) -> str:
    cypher = _create_key_cypher(key)

    m4 = ""
    for gram in [message[i : i + 2] for i in range(0, len(message), 2)]:
        x = _in_row(gram, cypher)
        y = _in_col(gram, cypher)
        z = _in_dia(gram, cypher)
        m4 += x or y or z

    return m4


# def _prep_message(message):
#     m0 = message.replace(" ", "")
#     m1 = ''.join(t for t in re.sub(PATTERN, r'\1x\1', m0))
#     m2 = [m1[i:i + 2] for i in range(0, len(m1), 2)]
#     m3 = [m + 'x' if len(m) == 1 else m for m in m2]
#     return m3


def _in_dia(gram: str, cypher: List[str]) -> str:
    results = []
    for c in list(gram):
        for col in range(len(cypher[0])):
            line = [c[col] for c in cypher]
            if c in line:
                results.append((col, line.index(c)))

    if len(results) == 2:
        col1, row1 = results[0]
        col2, row2 = results[1]

        a = cypher[row1][col2]
        b = cypher[row2][col1]
        return a + b
    return ""


def _in_col(gram: str, cypher: List[str]) -> str:
    result = ""
    c1, c2 = list(gram)
    for index in range(5):
        line = [c[index] for c in cypher]
        if c1 in line and c2 in line:
            result += line[(line.index(c1) - 1)]
            result += line[(line.index(c2) - 1)]
    return result


def _in_row(gram: str, cypher: List[str]) -> str:
    result = ""
    c1, c2 = list(gram)
    for line in cypher:
        if c1 in line and c2 in line:
            result += line[(line.index(c1) - 1)]
            result += line[(line.index(c2) - 1)]

    return "".join(result)


def run() -> None:
    msg = "vepcundbyoaeirotivluxnotpstfnbwept"
    key = "power plant"
    decrypt = decrypt_playfair(msg, key)
    assert decrypt == "youlxlhavetospeakupimwearingatowel"


if __name__ == "__main__":
    run()
