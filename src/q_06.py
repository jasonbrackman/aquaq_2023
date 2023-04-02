"""
It can be useful to know how to break down a number - usually this is done with factors, but instead, let's try
it with summable components. For a number, you can work out the possible combinations of non-negative integers
which sum to that number. For example, these are the combinations of three numbers which sum to 3:

0 0 3
0 1 2
0 2 1
0 3 0
1 0 2
1 1 1
1 2 0
2 0 1
2 1 0
3 0 0


The digit "1" occurs 9 times above. For your input, how many times does the character "1" appear in all combinations
summing to that number?

Note the number "11" would be twice, "21" once, so 1 21 11 would be 4 times.
"""


def run() -> None:
    # 3 numbers which sum to 123
    val = 123
    totals = 0
    for x in range(val + 1):
        for y in range(val - x + 1): # small opt. by removing x to remove calc. of impossible totals
            for z in range(val - (x + y) + 1):  # ^ remove x + y to remove calc. of impossible totals
                group = (x, y, z)
                if sum(group) == val:
                    totals += str(group).count("1")
    assert totals == 6927


if __name__ == "__main__":
    run()
