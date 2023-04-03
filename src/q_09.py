"""
It's 2022 and, due to a hiring mishap, the 2007 head of the Zimbabwean central bank is now running the entire UK economy, and inflation has been stuck at 1000000% for the last 4 years. AquaQ is still the best kdb consultancy in the land, but this year we're going to need to start regularly handling numbers greater than nine quintillion pounds.

To help prepare your mind (and body), enter the product of all numbers in your input (while keeping full precision!) in the box below.

For example input:
2
4
8

A function and answer would look like:
f[(2;4;8)]
64
"""
import math


def run() -> None:
    x = (
    203217,
    151018,
    482359,
    782486,
    281651,
    721924,
    945710,
    131962,
    78308,
    661224,
    )

    assert math.prod(x) == 15219490042476673293856415300433634433293774002195671040

if __name__ == "__main__":
    run()