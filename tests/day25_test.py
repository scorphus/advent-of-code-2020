#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day25 import part1
from aoc.day25 import part2

import pytest


@pytest.mark.parametrize("lines, output", [(["5764801", "17807724"], 14897079)])
def test_part1(lines, output):
    assert part1(iter(lines)) == output
    assert part1 is part2
