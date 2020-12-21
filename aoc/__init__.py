#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from functools import partial


def integers(lines):
    return map(int, lines)


def integers_list(lines):
    return list(integers(lines))


def strip(lines, chars="\n"):
    return map(partial(strip_chars, chars=chars), lines)


def strip_list(lines, chars="\n"):
    return list(strip(lines, chars))


def strip_chars(string, chars="\n"):
    return string.strip(chars)
