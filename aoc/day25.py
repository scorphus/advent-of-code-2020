#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers


def part1(lines):
    key1, key2 = integers(lines)
    return loop(key2, size(key1))


def size(key, sbj=7):
    val, size = 1, 0
    while val != key:
        val = val * sbj % 20201227
        size += 1
    return size


def loop(key, size):
    val = 1
    for _ in range(size):
        val = val * key % 20201227
    return val


part2 = part1
