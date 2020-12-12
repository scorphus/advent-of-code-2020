#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day12 import part1
from aoc.day12 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
F10
N3
F7
R90
F11
""".rstrip().splitlines(),
            25,
        ),
        (
            """\
R180
E1
N1
R90
E4
F84
""".rstrip().splitlines(),
            90,
        ),
    ],
)
def test_part1(lines, output):
    assert part1(lines) == output


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
F10
N3
F7
R90
F11
""".rstrip().splitlines(),
            286,
        ),
        (
            """\
R180
E1
N1
R90
E4
F84
""".rstrip().splitlines(),
            1092,
        ),
    ],
)
def test_part2(lines, output):
    assert part2(lines) == output
