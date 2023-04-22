"""
What is cooler than fraud? Nothing.*

The best kind of fraud** is subtle - for example, re-writing numbers so they are slightly larger,
but might not appear too dissimilar to the correct numbers at first glance. As well, accomplished
fraudsters*** may want to keep the change numerically subtle.

To help achieve this, re-arrange the numerals in each input number to create the next largest
integer which uses all the same numerals. If the current number is the largest available, leave it as it is.
For example:
1423
-> 1432

121
-> 211

10290
-> 10902


The answer to the challenge is the total of your ill-gotten gains, i.e. the sum of the differences between your
input and the re-arranged next-largest numbers. For the above example set, the total difference is 711.



* This was a test. If you agreed fraud is cool, you have failed. Don't do fraud.
** Please continue to realise this challenge is not actually an endorsement of fraud.
*** These do not exist and if you engage in fraud you will go to a low quality jail.
"""
import os
from itertools import permutations
from typing import List


def round_up(val: int) -> int:
    sl = list(str(val))

    for index in range(len(sl) - 1, -1, -1):
        items = sl[index:]
        current = int("".join(items))
        nums = [int("".join(c)) for c in permutations(items)]
        for num in sorted(nums):
            if num > current:
                return int("".join(sl[:index] + list(str(num))))
    return int(val)


def parse() -> List[int]:
    olds = []
    with open(r"./data/26_typo_theft.txt", "r") as f:
        for item in f.readlines():
            old = int(item.strip())
            olds.append(old)
    return olds


def run() -> None:
    olds = parse()
    news = []
    for old in olds:
        new = round_up(old)
        news.append(new if new > old else old)

    assert sum(news) - sum(olds) == 11923911


if __name__ == "__main__":
    os.chdir("..")
    run()
