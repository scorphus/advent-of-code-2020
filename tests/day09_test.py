#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day09 import part1
from aoc.day09 import part2

import pytest


@pytest.mark.parametrize(
    "lines, pre, output",
    [
        (
            """\
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
49
100
50
""".rstrip().splitlines(),
            25,
            100,
        ),
        (
            """\
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
65
64
66
50
""".rstrip().splitlines(),
            25,
            65,
        ),
        (
            """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".rstrip().splitlines(),
            5,
            127,
        ),
    ],
)
def test_part1(lines, pre, output):
    assert part1(lines, pre) == output


@pytest.mark.parametrize(
    "lines, pre, output",
    [
        (
            """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".rstrip().splitlines(),
            5,
            62,
        )
    ],
)
def test_part2(lines, pre, output):
    assert part2(lines, 5) == output
