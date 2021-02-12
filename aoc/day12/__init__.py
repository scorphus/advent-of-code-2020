#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import strip


DIRS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
}

NEW_DIRS = {
    DIRS["N"]: {"L": (-1, 0), "R": (1, 0)},
    DIRS["S"]: {"L": (1, 0), "R": (-1, 0)},
    DIRS["E"]: {"L": (0, 1), "R": (0, -1)},
    DIRS["W"]: {"L": (0, -1), "R": (0, 1)},
}


def part1(lines):
    pos = 0, 0
    dir = 1, 0
    for line in strip(lines):
        act, val = line[0], int(line[1:])
        if act == "F":
            pos = pos[0] + val * dir[0], pos[1] + val * dir[1]
        elif act in DIRS:
            pos = pos[0] + val * DIRS[act][0], pos[1] + val * DIRS[act][1]
        else:
            dir = steer(dir, act, val)
    return abs(pos[0]) + abs(pos[1])


def part2(lines):
    pos = 0, 0
    way = 10, 1
    for line in strip(lines):
        act, val = line[0], int(line[1:])
        if act == "F":
            pos = pos[0] + val * way[0], pos[1] + val * way[1]
        elif act in DIRS:
            way = way[0] + val * DIRS[act][0], way[1] + val * DIRS[act][1]
        else:
            dir = steer(DIRS["E"], act, val)
            way = way[0] * dir[0] - way[1] * dir[1], way[0] * dir[1] + way[1] * dir[0]
    return abs(pos[0]) + abs(pos[1])


def steer(dir, act, val):
    for _ in range(val // 90):
        dir = NEW_DIRS[dir][act]
    return dir
