"""
A new bitcoin fork has taken over! In this new system, users can use a modified form of the
lightning network, in which users are connected to some subset of other users, and can freely
transfer money to each other. In this system, transferring money directly between users costs
some small amount of pence - a different amount from user to user.

A set of user source-destination pairs and the cost to transfer between them looks like this:

 s  d  c
 --------
 A  B  8
 B  C  50
 B  D  5
 D  E  10
 E  C  6

Mapped out, with the costs between the users, this would look like:

 A--8--B--50--C
       |      |
       5      6
       |      |
       D--10--E

If user A wants to send money to user C, they can send via route ABC, costing 58p, or ABDEC, costing 29p.

In your input, you have a number of user pairs (listed in both directions) and their costs. Tupac owes
Diddy fifty pounds - what's the smallest extra amount he'll have to spend (in pence) to pay back Diddy
this fiddy?
"""
import os
from collections import defaultdict
from queue import PriorityQueue
from typing import Tuple, Dict, List

Edges = Dict[Tuple[str, str], int]
Nodes = Dict[str, List[str]]


def bfs(nodes: Nodes, edges: Edges, start: str, goal: str):
    q = PriorityQueue()
    q.put((0, start))
    v = {
        start,
    }
    while q.not_empty:
        cost, node = q.get()

        if node == goal:
            return cost

        for neighbour in nodes[node]:
            if neighbour not in v:
                v.add(neighbour)
                q.put((edges[(node, neighbour)] + cost, neighbour))
    return None


def parse() -> Tuple[Nodes, Edges]:
    edges: Edges = dict()
    nodes: Nodes = defaultdict(list)

    with open(r"./data/10_troll_toll.txt", "r") as handle:
        lines = iter(handle.readlines())
        _header = next(lines)
        for line in lines:
            a, b, c = line.strip().split(",")
            edges[(a, b)] = int(c)
            nodes[a].append(b)

    return nodes, edges


def run() -> None:
    nodes, edges = parse()
    r = bfs(nodes, edges, "TUPAC", "DIDDY")
    assert r == 596


if __name__ == "__main__":
    os.chdir("..")
    run()
