#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day08 import part1
from aoc.day08 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".rstrip().splitlines(),
            5,
        )
    ],
)
def test_part1(lines, output):
    assert part1(lines) == output


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".rstrip().splitlines(),
            8,
        )
    ],
)
def test_part2(lines, output):
    assert part2(lines) == output
