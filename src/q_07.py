"""
Elo is a method of tracking historical performance and estimating the chances of future success in
head-to-head matchups - it was made for chess, but can be applied to lots of sports and video games.
We'll use it here to see who's been performing best in a display of god-like athleticism: the AquaQ
table tennis tournament.

The way Elo works is by comparing the expected win rate of two head-to-head competitors, calculated
for player a with:
Ea = 1 / (1 + 10^((Rb-Ra)/400))


Here, Ra and Rb are the ratings of teams a and b - which start at 1200 and are modified with:
Ri' = Ri + 20(1-Ei)


where Ri is the old ranking, and Ri' is the updated ranking for the winning team - 20(1-Ei) is the
amount of points the winner gains and the loser loses. For example, if Ra is 1400 and Rb is 1200,
a has an expected win rate of around 0.75 over b, and if a wins, Ra gains, and Rb loses, about 5
points each. Conversely, if b wins, b gains and a loses 15 points.

This dependency on the point ratings ensures that an expected results doesn't change points
distribution too much, but an unexpected results causes a larger points swing.

To answer this challenge, take the input csv of table tennis games, and find the difference between
the best and worst Elo in the final standings. You'll need to work out who won in each game and
update their rating after every match. When calculating the final value, use only the integer part
of the highest and lowest values, e.g.

1500.89-913.1


becomes

1500-913
"""
from __future__ import annotations

import os
from typing import Dict


class Elo:
    def __init__(self) -> None:
        self.score = 1200.0
        self.constant = 20

    def expected_result(self, other: Elo) -> float:
        return 1 / (1 + 10 ** ((other.score - self.score) / 400))

    def update(self, other: Elo) -> None:
        other_elo = self.expected_result(other)
        # the winning team's score is updated with:
        result = self.constant * (1 - other_elo)
        self.score += result
        other.score -= result


def run() -> None:

    # Parse the data
    with open("./data/07_what_is_best_in_life.txt", "r") as handle:
        lines = iter(handle.readlines())
    _header = next(lines)  # throw away the header

    # keep track of the teams and their Elo
    teams: Dict[str, Elo] = dict()
    for line in lines:
        home, away, original_scores = line.strip().split(",")
        # Add teams if missing
        if home not in teams:
            teams[home] = Elo()
        if away not in teams:
            teams[away] = Elo()

        # Calculate who won
        scores = [int(s) for s in original_scores.split("-")]
        winner = home if scores[0] > scores[1] else away
        # distribute score
        if winner == home:
            teams[home].update(teams[away])
        else:
            teams[away].update(teams[home])

    final_scores = [elo.score for team, elo in teams.items()]
    assert round(max(final_scores)) - round(min(final_scores)) == 77


if __name__ == "__main__":
    os.chdir("..")
    run()
