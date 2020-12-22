#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day22 import part1
from aoc.day22 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            [
                """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
            ],
            306,
        ),
        (
            [
                """\
Player 1:
5
8
4
7
10

Player 2:
9
2
6
3
1
"""
            ],
            306,
        ),
    ],
)
def test_part1(lines, output):
    assert part1(iter(lines)) == output


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            [
                """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
            ],
            291,
        ),
        (
            [
                """\
Player 1:
5
8
4
7
10

Player 2:
9
2
6
3
1
"""
            ],
            291,
        ),
        (
            [
                """\
Player 1:
43
19

Player 2:
2
29
14
"""
            ],
            105,
        ),
    ],
)
def test_part2(lines, output):
    assert part2(iter(lines)) == output
