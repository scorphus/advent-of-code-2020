#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers_list
from pickle import dumps

import sys


sys.setrecursionlimit(9_000)  # 🔥


def part1(lines):
    p1, p2 = read(lines)
    winner = combat(p1, p2)
    return sum(i * c for i, c in enumerate(reversed(winner), 1))


def part2(lines):
    p1, p2 = read(lines)
    winner = next(filter(None, recursive_combat(p1, p2)))
    return sum(i * c for i, c in enumerate(reversed(winner), 1))


def read(lines):
    players = "".join(lines).split("\n\n")
    for _, cards in (p.rstrip().split("\n", maxsplit=1) for p in players):
        yield integers_list(cards.splitlines())


def combat(p1, p2):
    if not p2:
        return p1
    if not p1:
        return p2
    c1, *p1 = p1
    c2, *p2 = p2
    if c1 > c2:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]
    return combat(p1, p2)


def recursive_combat(p1, p2, hist=set()):
    if not p2 or not p1:
        return p1, p2
    decks = dumps((p1, p2))
    if decks in hist:
        return p1, []
    hist.add(decks)
    c1, *p1 = p1
    c2, *p2 = p2
    p1_wins = c1 > c2
    if c1 <= len(p1) and c2 <= len(p2):
        p1_wins, _ = recursive_combat(p1[:c1], p2[:c2], set())
    if p1_wins:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]
    return recursive_combat(p1, p2, hist)
