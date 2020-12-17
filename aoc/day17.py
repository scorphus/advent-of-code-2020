#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import itertools


def part1(lines):
    space = set()
    for x, line in enumerate(lines):
        for y, cube in enumerate(line):
            if cube == "#":
                space.add((x, y, 0))
    for _ in range(6):
        space = cycle(space)
    return len(space)


def part2(lines):
    space = set()
    for x, line in enumerate(lines):
        for y, cube in enumerate(line):
            if cube == "#":
                space.add((x, y, 0, 0))
    for _ in range(6):
        space = cycle(space, 4)
    return len(space)


def cycle(space, dim=3):
    active, next_space = {}, set()
    for cube in space:
        for deltas in itertools.product((-1, 0, 1), repeat=dim):
            if any(deltas):
                neighbor = tuple(c + d for c, d in zip(cube, deltas))
                active[neighbor] = active.get(neighbor, 0) + 1
    for cube, neighbors in active.items():
        if neighbors == 3 or neighbors == 2 and cube in space:
            next_space.add(cube)
    return next_space
