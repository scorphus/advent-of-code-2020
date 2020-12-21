#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day21 import part1
from aoc.day21 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".rstrip().splitlines(),
            5,
        ),
    ],
)
def test_part1(lines, output):
    assert part1(iter(lines)) == output


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".rstrip().splitlines(),
            "mxmxvkd,sqjhc,fvjkl",
        ),
    ],
)
def test_part2(lines, output):
    assert part2(iter(lines)) == output
