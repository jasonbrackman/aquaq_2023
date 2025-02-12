import os


def parse(path: str) -> list[int]:
    """Parse input into a list of integers."""
    with open(path, encoding='utf8') as file:
        nums = [int(x) for x in file.read().split()]
    return nums


def get_peaks(nums: list[int]) -> list[bool]:
    """Create a mapping of which indexes are peaks."""
    results = [False] * len(nums)
    high = False
    last = -1
    for idx, num in enumerate(nums):
        if num > last:
            high = True
        elif num < last:
            if high is True:
                # we must be going down from a peak
                results[idx - 1] = True
            high = False

        last = num
    return results


def get_troughs(nums: list[int]) -> list[bool]:
    """Create a mapping of which indexes are troughs."""
    results = [False] * len(nums)
    low = False
    last = -1
    for idx, num in enumerate(nums):
        if num > last:
            # must be going up from a low point
            if low is True:
                results[idx - 1] = True
            low = False
        elif num < last:
            low = True

        last = num
    return results


def puzzle(nums, peaks, troughs):
    """
    Broke out the puzzle into its own function. Its currently very expensive as it repeats
    the work being done for each loop. Need to do the work once for all and just do a look-up.
    """
    values = 0
    for idx, peak_a in enumerate(nums):

        # Do some work to find if there is anywhere else >= in height to run too.
        if peaks[idx] is True:
            results = peak_a
            for d, peak_b in enumerate(nums):
                if d != idx and peaks[d] is True and peak_b >= peak_a:
                    # Found another peak. What is the trough between the two?
                    v1, v2 = (d, idx) if d < idx else (idx, d)

                    t = 0
                    for u in range(v1, v2):
                        if troughs[u]:
                            c = peak_a - nums[u]
                            t = c if c > t else t

                    t = t if t != 0 else peak_a
                    if t < results:
                        results = t

            # print("\t\tTrough:", results)
            values += results
    assert values == 6750


def run() -> None:
    nums = parse(r"./data/40_prominence_promenade.txt")
    peaks = get_peaks(nums)
    troughs = get_troughs(nums)

    puzzle(nums, peaks, troughs)


if __name__ == "__main__":
    os.chdir('..')
    run()
