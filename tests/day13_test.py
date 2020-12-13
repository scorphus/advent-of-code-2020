#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day13 import part1
from aoc.day13 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
939
7,13,x,x,59,x,31,19
""".rstrip().splitlines(),
            295,
        ),
    ],
)
def test_part1(lines, output):
    assert part1(iter(lines)) == output


@pytest.mark.parametrize(
    "lines, output",
    [
        ("\n7,13,x,x,59,x,31,19".splitlines(), 1068781),
        ("\n17,x,13,19".splitlines(), 3417),
        ("\n67,7,59,61".splitlines(), 754018),
        ("\n67,x,7,59,61".splitlines(), 779210),
        ("\n67,7,x,59,61".splitlines(), 1261476),
        ("\n1789,37,47,1889".splitlines(), 1202161486),
    ],
)
def test_part2(lines, output):
    assert part2(iter(lines)) == output
