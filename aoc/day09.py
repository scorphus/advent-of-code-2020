#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers_list

import itertools


def part1(lines, pre=25):
    lines = integers_list(lines)
    return find(lines, pre)


def part2(lines, pre=25):
    lines = integers_list(lines)
    invalid = find(lines, pre)
    idx = lines.index(invalid)
    psums = prefix_sums(lines[:idx])
    for (i, x), (j, y) in itertools.product(enumerate(psums), enumerate(psums)):
        if y - x == invalid:
            return min(lines[i:j]) + max(lines[i:j])


def find(lines, pre):
    front, back = lines[:pre], lines[pre:]
    sums = sum_all(front)
    for x in back:
        if x not in sums:
            return x
        front.pop(0)
        front.append(x)
        sums = sum_all(front)


def sum_all(front):
    return set(x + y for x, y in itertools.product(front, front))


def prefix_sums(front):
    sums = [0] * (len(front) + 1)
    for i in range(1, len(front) + 1):
        sums[i] = sums[i - 1] + front[i - 1]
    return sums
