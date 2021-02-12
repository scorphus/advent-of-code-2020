#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers
from aoc import integers_list

import itertools


def part1(lines):
    xps = set(integers(lines))
    for x in xps:
        if 2020 - x in xps:
            return x * (2020 - x)


def part2(lines):
    xps = integers_list(lines)
    for x, y, z in itertools.product(xps, xps, xps):
        if x + y + z == 2020:
            return x * y * z
