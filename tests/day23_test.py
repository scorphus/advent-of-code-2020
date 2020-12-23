#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day23 import part1
from aoc.day23 import part2

import pytest


@pytest.mark.parametrize(
    "lines, moves, output",
    [
        (["389125467"], 10, "92658374"),
        (["389125467"], 100, "67384529"),
    ],
)
def test_part1(lines, moves, output):
    assert part1(iter(lines), moves) == output


@pytest.mark.parametrize(
    "lines, n, moves, output",
    [
        (["389125467"], 9, 10, 18),
        (["389125467"], 9, 100, 42),
    ],
)
def test_part2(lines, n, moves, output):
    assert part2(iter(lines), n, moves) == output
