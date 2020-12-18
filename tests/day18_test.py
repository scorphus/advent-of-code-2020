#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day18 import part1
from aoc.day18 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (["1 + 2 * 3 + 4 * 5 + 6"], 71),
        (["1 + (2 * 3) + (4 * (5 + 6))"], 51),
        (["2 * 3 + (4 * 5)"], 26),
        (["5 + (8 * 3 + 9 + 3 * 4 * 3)"], 437),
        (["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"], 12240),
        (["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"], 13632),
    ],
)
def test_part1(lines, output):
    assert part1(iter(lines)) == output


@pytest.mark.parametrize(
    "lines, output",
    [
        (["1 + (2 * 3) + (4 * (5 + 6))"], 51),
        (["2 * 3 + (4 * 5)"], 46),
        (["5 + (8 * 3 + 9 + 3 * 4 * 3)"], 1445),
        (["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"], 669060),
        (["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"], 23340),
    ],
)
def test_part2(lines, output):
    assert part2(iter(lines)) == output
