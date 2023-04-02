import os
import re

NUM_PATTERN = re.compile(r"\d+")

T9 = {
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}


def run() -> None:
    result = ""
    with open("./data/0_num_pad.txt", "r") as handle:
        for line in handle.readlines():
            val, count = re.findall(NUM_PATTERN, line)
            result += T9[int(val)][int(count) - 1]
    assert result == "oh so they have internet on computers now"


if __name__ == "__main__":
    os.chdir('..')
    run()
