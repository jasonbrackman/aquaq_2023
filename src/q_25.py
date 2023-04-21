"""
While looking for biscuits in your colleague's office, you accidentally discover they are a Russian spy.
Also, you remember this is UK or the USA in 1963 and this is a Big Deal.

While wondering if Russian biscuits are nicer than custard creams you hear them approach the door.
Thinking quickly, you dive into a nearby cupboard. After a time you hear the very distinctive click
of a telegraph machine being used to send messages in Morse code. You can't see anything, but you can
use your perfect temporal sense to note the millisecond-precise time you hear the machine click either
on or off.

Several hours later your colleague leaves and you emerge - they sent a number of messages, so you
note the time of each click, in order, with a space between separate messages, and set about decoding
them.

The Morse code alphabet looks like this:
a| .-
b| -...
c| -.-.
d| -..
e| .
f| ..-.
g| --.
h| ....
i| ..
j| .---
k| -.-
l| .-..
m| --
n| -.
o| ---
p| .--.
q| --.-
r| .-.
s| ...
t| -
u| ..-
v| ...-
w| .--
x| -..-
y| -.--
z| --..


A dot is one "unit" long, and
a dash is three units.

Each element of a letter has a single unit between dots and dashes.
The letter "r" (".-.") for example will be 7 elements long - one unit for each dot, one
for the space between the dot and the dash, another for the space between the dash and dot, and three
for the dash.

The space between adjacent letters is three units (with no other additional spacing needed)
and the space between words is seven units.

The message "jam donut" in the above would look like this in Morse code:
.--- .- --   -.. --- -. ..- -


But as a series of clicks, you would hear the start of the first dot as one click, then the click as
it finishes, then the click of the dash starting, then the click of the dash finishing, etc. You can
assume the first click is always clicking the signal on, and that your colleague has robotic accuracy
so click-spacing is constant.

The start of the message then might look like this, marking only the clicks as seconds from the start:
0
1
2
5
6
9
10
13
16
17
18
21
24
27
28
31
38
41
42
43
...


Your colleague sent a number of messages, each represented by their own line of click-times
in the input. Your answer can be obtained from the decoded set of messages.
"""
import os
from datetime import datetime
from typing import List

morse = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
}


def parse() -> List[List[datetime]]:
    times = []
    with open(r"./data/25_smores.txt", "r") as handle:
        message = []
        for time in handle.readlines():
            time = time.strip()
            if time:
                message.append(datetime.strptime(time, "%H:%M:%S.%f"))
            else:
                times.append(message[::])
                message.clear()
    if message:
        times.append(message[::])
    return times


def decode(message) -> str:
    deltas = [(b - a) for a, b in zip(message, message[1:])]
    smallest = min(deltas)
    vals = []
    output = ""
    current_letter: List[str] = []
    for index, delta in enumerate(deltas):
        val = int(delta / smallest)
        vals.append(val)
        if index % 2 == 0:
            if val == 3:
                current_letter += "-"
            elif val == 1:
                current_letter += "."
        else:
            if val == 7:
                output += morse["".join(current_letter)]
                output += " "
                current_letter.clear()
            elif val == 3:
                output += morse["".join(current_letter)]
                current_letter.clear()
    if current_letter:
        output += morse["".join(current_letter)]
        current_letter.clear()
    return output

def run() -> None:
    times = parse()
    expected = [
        "the first letter of the answer is p",
        "the second character is q and the first letter is still p",
        "the third alphanumeric element is r and the second letter is now a",
        "the fourth is i",
        "test line please ignore zxcociquuzeotrwnqyiewmnaxzxcvl",
        "the final glyph is the letter following r in the alphabet",
    ]
    for message, expect in zip(times, expected):
        assert decode(message) == expect


if __name__ == "__main__":
    os.chdir("..")
    run()