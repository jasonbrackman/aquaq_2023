"""
You've found a table which is supposed to record only unique values in the order they appeared. Looking closely,
you realise that some of the values occur multiple times. Consulting the documentation, you see the original system
was designed to only have data appended, so there was no way to correct broken inputs.

Instead, a record appearing more than once means that everything between the first instance of that record up to the
latest occurrence was incorrect, and should be discarded. Values after this occurrence are treated as if those records
in between hadn't existed. What is the sum of the values returned from your input after this process has been applied?

For example input:
1 4 3 2 4 7 2 6 3 6

f[1 4 3 2 4 7 2 6 3 6]
1 4 7 2 6


In this case, the summed answer would be 20.

"""
from typing import List


def discard_process(items: List[str]) -> int:
    problem = None

    collected = []
    while items:
        t = items.pop(0)
        if problem is not None:
            if t == problem and t not in items:
                problem = None
                collected.append(int(t))
            # Else do nothing

        elif t in items:
            problem = t

        else:
            if problem is None:
                collected.append(int(t))

    return sum(collected)


def run() -> None:
    with open("./data/2_one_is_all_you_need.txt", "r") as handle:
        items = handle.read().split()
    assert discard_process(items) == 321


if __name__ == "__main__":
    run()
