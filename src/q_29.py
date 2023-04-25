"""
No more rookie numbers - from now on, we're going to pump those numbers up.

We want to find the numbers which have digits which don't decrease when reading the number from left-to-right.
Example good numbers:
1
45
777
1245


Example unwanted numbers:
10
97
2099


How many "good" numbers exist between 0 and your input (inclusive)?
"""

def is_good(index: int) -> bool:
    temp = str(index)
    for a, b in zip(temp, temp[1:]):
        if a > b:
            return False
    return True


def run() -> None:
    max_value = 520185742
    t = sum(is_good(i) for i in range(max_value + 1))
    assert t == 47905


if __name__ == "__main__":
    run()