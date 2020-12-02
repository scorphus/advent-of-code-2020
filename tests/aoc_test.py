#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers_list
from aoc import strip_list

import pytest


@pytest.mark.parametrize(
    "lines, expected",
    [
        (["1"], [1]),
        (["1", "2", "3"], [1, 2, 3]),
        ("1\n2\n3\n".splitlines(), [1, 2, 3]),
        ([], []),
        ("", []),
        ("1", [1]),
        ("123", [1, 2, 3]),
    ],
)
def test_integers(lines, expected):
    assert integers_list(lines) == expected


@pytest.mark.parametrize(
    "lines, exception",
    [
        (1, TypeError),
        (None, TypeError),
        ("a", ValueError),
        ([""], ValueError),
        ([" "], ValueError),
        (["a"], ValueError),
        (["1.1"], ValueError),
    ],
)
def test_integers_raises(lines, exception):
    with pytest.raises(exception):
        integers_list(lines)


@pytest.mark.parametrize(
    "lines, expected",
    [
        ("", []),
        ("a", ["a"]),
        ("abc", ["a", "b", "c"]),
        ([], []),
        ([""], [""]),
        (["1"], ["1"]),
        (["1\n"], ["1"]),
        (["1", "2", "3"], ["1", "2", "3"]),
        (["1\n", "2\n", "3\n"], ["1", "2", "3"]),
        (["a\n", "b\n", "c\n"], ["a", "b", "c"]),
        (["a ", "b ", "c "], ["a ", "b ", "c "]),
    ],
)
def test_strip(lines, expected):
    assert strip_list(lines) == expected


@pytest.mark.parametrize(
    "lines, exception",
    [
        (1, TypeError),
        (None, TypeError),
        (False, TypeError),
        ([1], AttributeError),
        ([None], AttributeError),
        ([False], AttributeError),
    ],
)
def test_strip_raises(lines, exception):
    with pytest.raises(exception):
        strip_list(lines)
