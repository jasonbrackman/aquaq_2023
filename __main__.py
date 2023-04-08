import time

from src import (
    q_00,
    q_01,
    q_02,
    q_03,
    q_04,
    q_05,
    q_06,
    q_07,
    q_08,
    q_09,
    q_10,
    q_11,
    q_12,
    q_14,
)

for challenge in [
    q_00,
    q_01,
    q_02,
    q_03,
    q_04,
    q_05,
    q_06,
    q_07,
    q_08,
    q_09,
    q_10,
    q_11,
    q_12,
    q_14,
]:
    start_time = time.time()
    getattr(challenge, "run")()
    end_time = time.time()
    microsecond_symbol = "\u00b5"
    microseconds = (end_time - start_time) * 1_000_000
    print(
        f"[{challenge.__name__}]: Completed in {microseconds:9.2f}{microsecond_symbol}s"
    )
