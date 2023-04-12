"""
Some people say the best times in life are those among friends or family. The actual best times
however, are palindromic:

11:22:11

Your input is a list of times - for each time, how far away, in seconds, is the nearest
palindromic time, in hh:mm:ss format? The answer is the sum of these differences.
For example, with input time:

13:41:00

The nearest palindromic time is

13:44:31

Which is 211 seconds away. Note that the nearest palindromic time might be in the past - a time in
the past is still a positive number of seconds away.
"""
import os

Seconds = int


def calculate_difference(a: str) -> Seconds:
    h1, m1, s1 = [int(i) for i in a.split(":")]
    up = h1 * 3600 + m1 * 60 + s1
    down = up

    for index in range(86_400):  # 24 hours in seconds
        test_up = recalc(up)
        test_down = recalc(down)
        for item in (test_up, test_down):
            y = item[:4]
            if y[::-1] == item[4:]:
                return index
        up += 1
        down -= 1
    raise ValueError("This should not be reachable.")


def recalc(time_in_seconds: Seconds) -> str:
    hours = time_in_seconds // 3600 % 24
    leftovers = time_in_seconds % 3600
    minutes = leftovers // 60
    seconds = leftovers % 60
    return f"{hours:>02}:{minutes:>02}:{seconds:>02}"


def run() -> None:
    total = 0
    with open(r"./data/18_emit_time.txt", "r") as handle:
        for line in handle.readlines():
            line = line.strip()
            total += calculate_difference(line)

    assert total == 719126


if __name__ == "__main__":
    os.chdir("..")
    run()
