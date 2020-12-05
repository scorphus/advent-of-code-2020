#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day05 import get_seat_id
from aoc.day05 import part1
from aoc.day05 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
""".rstrip().splitlines(),
            820,
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
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
""".rstrip().splitlines(),
            120,
        ),
    ],
)
def test_part2(lines, output):
    assert part2(lines) == output


@pytest.mark.parametrize(
    "seat_address, seat_id",
    [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_get_seat_id(seat_address, seat_id):
    print()
    assert get_seat_id(seat_address) == seat_id
