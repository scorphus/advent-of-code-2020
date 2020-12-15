#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day15 import part1
from aoc.day15 import part2
from unittest.mock import Mock
from unittest.mock import patch

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (["0,3,6"], 436),
        (["1,3,2"], 1),
        (["2,1,3"], 10),
        (["1,2,3"], 27),
        (["2,3,1"], 78),
        (["3,2,1"], 438),
        (["3,1,2"], 1836),
    ],
)
def test_part1(lines, output):
    assert part1(iter(lines)) == output


@patch("aoc.day15.part1")
def test_part2(part1_mock):
    lines = Mock()
    assert part2(lines) == part1_mock.return_value
    part1_mock.assert_called_once_with(lines, 30_000_000)
