#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers

import collections


def part1(lines):
    val = 0
    for line in lines:
        idx, let, pwd = line.split()
        i, j = integers(idx.split("-"))
        cc = collections.Counter(pwd)
        if i <= cc[let[0]] <= j:
            val += 1
    return val


def part2(lines):
    val = 0
    for line in lines:
        idx, let, pwd = line.split()
        i, j = integers(idx.split("-"))
        i -= 1
        j -= 1
        let = let[0]
        if pwd[i] != pwd[j] and (pwd[i] == let or pwd[j] == let):
            val += 1
    return val
