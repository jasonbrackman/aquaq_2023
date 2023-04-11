"""
Co-primes, while not being the most exciting thing in the world, are extremely useful for cryptography
(among other things). Numbers are co-prime if they don't share any common factors above 1.

For example, 15 and 8 are not prime, but have factors of 3 5 and 2 4 respectively, and so are co-prime.
15 and 9 are not co-prime, since they share a factor of 3.

For your input number, what is the sum of the positive co-primes of that number which are less than that number?

For example, the co-primes of 15 are
1 2 4 7 8 11 13 14


If your input was 15, the answer would be 60.

"""
from typing import Set


def find_factors(num: int) -> Set[int]:
    return {index for index in range(2, (num // 2) + 1) if num % index == 0}


def is_intersecting(index: int, x: Set[int]) -> bool:
    for item in x:
        if item <= index and index % item == 0:
            return True
    return False


def run() -> None:
    puzzle_input = 987_820
    x = find_factors(puzzle_input)
    t = 1  # none of the collection includes 1; just assumed
    for index in range(2, puzzle_input):
        if not is_intersecting(index, x):
            # must be good if we got here
            t += index
    assert t == 195153719200


if __name__ == "__main__":
    run()
