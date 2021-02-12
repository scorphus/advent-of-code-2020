#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import strip

import copy


DIR = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]


def part1(lines, shortsight=True, least_occ=4):
    grid = [list(line) for line in strip(lines)]
    total = 0
    while True:
        changed = False
        grid_copy = copy.deepcopy(grid)
        for i, row in enumerate(grid_copy):
            for j, loc in enumerate(row):
                if loc == "L" and occupied(grid_copy, i, j, shortsight) == 0:
                    grid[i][j] = "#"
                    total += 1
                    changed = True
                elif loc == "#" and occupied(grid_copy, i, j, shortsight) >= least_occ:
                    grid[i][j] = "L"
                    total -= 1
                    changed = True
        if not changed:
            return total


def part2(lines):
    # I just couldn't avoid refactoring part1 to accept extra arguments.
    # Meh... seems like a shortage of imagination/creativity from AoC author(s)
    return part1(lines, False, 5)


def occupied(grid, i, j, shortsight=True):
    m = len(grid)
    n = len(grid[0])
    s = 0
    for di, dj in DIR:
        k = 1
        while 0 <= i + k * di < m and 0 <= j + k * dj < n:
            if grid[i + k * di][j + k * dj] == "#":
                s += 1
                break
            if shortsight or grid[i + k * di][j + k * dj] == "L":
                break
            k += 1
    return s
