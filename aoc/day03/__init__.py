#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import strip


def part1(lines, right=3):
    i = trees = 0
    for line in strip(lines):
        if line[i % len(line)] == "#":
            trees += 1
        i += right
    return trees


def part2(lines):
    lines = list(lines)
    total_trees = 1
    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        total_trees *= part1(lines[::down], right)
    return total_trees
