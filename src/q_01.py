"""
Set the string's non-hexadecimal characters to 0.
Pad the string length to the next multiple of 3.
Split the result into 3 equal sections.
The first two digits of each remaining section are the hex components.

>> body bgcolor="kdb4life" -> 0d40fe

"""


def convert(message: str) -> str:
    s = ""
    for c in message:
        if c not in "0123456789abcdef":
            s += "0"
        else:
            s += c

    extra = 3 - (len(s) % 3)
    s += "0" * extra
    div = len(s) // 3

    return "".join([s[index : index + 2] for index in range(0, len(s), div)])


def run() -> None:
    with open(r"./data/01_rose_by_any_other_name.txt", "r") as handle:
        t = handle.read()
    assert convert(t) == "d0000d"


if __name__ == "__main__":
    run()
