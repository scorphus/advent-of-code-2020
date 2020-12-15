#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers


def part1(lines, limit=2020):
    game = {}
    for i, n in enumerate(integers(next(lines).split(","))):
        game[n] = i + 1, 0
    last = list(game)[-1]
    for i in range(len(game) + 1, limit + 1):
        _, last = game[last]
        last_i, _ = game.get(last, (i, 0))
        game[last] = i, i - last_i
    return last


def part2(lines):
    return part1(lines, 30_000_000)
