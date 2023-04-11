"""
It's the world cup! National glory is at stake! But who has accrued the most national shame?

We'll define shame as days on a goalless streak - any national team who plays an international game
and finishes without scoring is in a state of shame, starting that day. The shame ends the day they
score a goal in another international game. Your input is a list of international football matches
going back to November 1872, and ending 2018.06.24. Which nation has the longest closed goalless
streak, across which dates? Any goalless streak currently running shouldn't be counted, and the
answer should be presented as:

team start_date end_date
with dates in YYYYMMDD format. The answer is case-sensitive!

For example, slightly reformatted results for three teams are like so:

team       date       score
---------------------------
Somaliland 1900.01.01 1
Formosa    1900.01.01 0
Genoa      1900.01.01 1
Genoa      1900.01.02 0
Somaliland 1900.01.03 0
Genoa      1900.01.03 0
Genoa      1900.01.06 0
Genoa      1901.01.21 1
Somaliland 1902.01.01 1


The longest streak here is Somaliland, so the answer would be
Somaliland 19000103 19020101
"""
import os
from datetime import date
from typing import Tuple, Dict, List, Iterable, Optional


class Team:
    def __init__(self) -> None:
        self.games: List[Tuple[str, int]] = []

    @staticmethod
    def _standardize_date(game_day: str) -> date:
        year, month, day = (int(i) for i in game_day.split("-"))
        return date(year, month, day)

    def add_game(self, game_date: str, score: int) -> None:
        self.games.append((game_date, score))

    def longest_shame(self) -> Tuple[Optional[str], Optional[str], int]:
        shame_days = 0
        old_date = None
        shame_from: Optional[str] = None
        shame_to: Optional[str] = None
        for new_date, score in sorted(self.games):
            if score == 0:
                if old_date is None:
                    old_date = new_date
            else:
                if old_date is not None:
                    # Define two dates
                    date1 = self._standardize_date(old_date)
                    date2 = self._standardize_date(new_date)

                    # Calculate the number of days between the two dates
                    delta = date2 - date1
                    num_days = delta.days

                    if num_days > shame_days:
                        shame_days = num_days
                        shame_from = old_date.replace("-", "")
                        shame_to = new_date.replace("-", "")
                    old_date = None

        return shame_from, shame_to, shame_days


def parse() -> Iterable[str]:
    with open("./data/17_the_beautiful_shame.txt", "r") as handle:
        items = iter(handle.readlines())
    next(items)  # throw away header
    return items


def process(items: Iterable[str]) -> Dict[str, Team]:
    teams: Dict[str, Team] = dict()
    for item in items:

        game_date, home, away, home_score, away_score, *_ = item.strip().split(",")
        if home not in teams:
            teams[home] = Team()
        if away not in teams:
            teams[away] = Team()

        teams[home].add_game(game_date, int(home_score))
        teams[away].add_game(game_date, int(away_score))
    return teams


def run() -> None:
    items = parse()
    teams = process(items)

    score = 0
    final = ""
    for key in teams:
        streak_from, streak_to, shame_days = teams[key].longest_shame()
        if shame_days > score and streak_from and streak_to:
            score = shame_days
            final = " ".join([key, streak_from, streak_to])
    assert final == "Kyrgyzstan 19560803 19920926", final


if __name__ == "__main__":
    os.chdir("..")
    run()
