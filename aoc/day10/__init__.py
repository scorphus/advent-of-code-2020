#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers_list

import collections
import math


def part1(lines):
    adaps = integers_list(lines)
    adaps = sorted([0, *adaps, max(adaps) + 3])
    counter = collections.Counter(b - a for a, b in zip(adaps[:-1], adaps[1:]))
    return counter[1] * counter[3]


def part2(lines):
    adaps = integers_list(lines)
    adaps = sorted([0, *adaps, max(adaps) + 3])
    last_diff = 0
    ones = comb = 1
    for diff in (b - a for a, b in zip(adaps[:-1], adaps[1:])):
        if diff == last_diff == 1:
            ones += 1
        elif ones > 1:
            comb *= math.comb(ones, 2) + 1
            ones = 1
        last_diff = diff
    return comb
