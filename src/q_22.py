import os
from string import ascii_uppercase

def to_roman(num: int) -> str:
    # Define the Roman numeral symbols and their corresponding values
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    # Initialize an empty string to store the Roman numeral representation
    roman_numeral = ''
    # Iterate over the symbols in descending order of their values
    for value, symbol in roman_numerals.items():
        # Repeat the symbol as many times as possible
        while num >= value:
            roman_numeral += symbol
            num -= value
    # Return the Roman numeral representation
    return roman_numeral


def run() -> None:
    lut = {c: v for v, c in enumerate(ascii_uppercase, 1)}
    total = 0
    # Don't understand the puzzle joke of changing the `vici` to `vitavi`
    #                                               `Conquer` vs `Shun`
    with open(r'./data/22_veni_vidi_vitavi.txt', 'r') as f:
        for item in f.read().split():
            result = to_roman(int(item))
            for r in result:
                total += lut[r]

    assert total == 43103


if __name__ == "__main__":
    os.chdir("..")
    run()