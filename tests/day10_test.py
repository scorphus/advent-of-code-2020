#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.day10 import part1
from aoc.day10 import part2

import pytest


@pytest.mark.parametrize(
    "lines, output",
    [
        (
            """\
16
10
15
5
1
11
7
19
6
12
4""".rstrip().splitlines(),
            7 * 5,
        ),
        (
            """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".rstrip().splitlines(),
            22 * 10,
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
16
10
15
5
1
11
7
19
6
12
4""".rstrip().splitlines(),
            8,
        ),
        (
            """\
2
5
6
7
8
11
12
13
16
17
20
""".rstrip().splitlines(),
            8,
        ),
        (
            """\
3
6
7
8
9
12
13
14
17
18
21
""".rstrip().splitlines(),
            8,
        ),
        (
            """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".rstrip().splitlines(),
            19208,
        ),
    ],
)
def test_part2(lines, output):
    assert part2(lines) == output
