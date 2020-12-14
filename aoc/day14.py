#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import strip


def part1(lines):
    mask_or = mask_and = 0
    mem = {}
    for line in strip(lines):
        if line.startswith("mask"):
            mask = line.rsplit(maxsplit=1)[-1]
            mask_or = int(mask.replace("X", "0"), 2)
            mask_and = int(mask.replace("X", "1"), 2)
        else:
            pos, val = map(int, line.lstrip("mem[").split("] = ", 1))
            mem[pos] = val | mask_or & mask_and
    return sum(mem.values())


def part2(lines):
    mask = None
    mask_or = 0
    mem = {}
    for line in strip(lines):
        if line.startswith("mask"):
            mask = line.rsplit(maxsplit=1)[-1]
            mask_or = int(mask.replace("X", "1"), 2)
        else:
            pos, val = map(int, line.lstrip("mem[").split("] = ", 1))
            mem[pos | mask_or] = val
            for pos in apply(mask, pos | mask_or):
                mem[pos] = val
    return sum(mem.values())


def apply(mask, pos, mask_and=2 ** 36 - 1, end=36):
    end = mask.rfind("X", 0, end)
    if end >= 0:
        yield from apply(mask, pos, mask_and, end)
        mask_and -= 2 ** (35 - end)
        yield pos & mask_and
        yield from apply(mask, pos, mask_and, end)
