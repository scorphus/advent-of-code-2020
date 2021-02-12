#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from sympy.ntheory.modular import crt


def part1(lines):
    depart = int(next(lines))
    bus = float("inf"), float("inf")
    for bid in next(lines).split(","):
        if bid != "x":
            bid = int(bid)
            some_bus = bid - depart % bid, bid
            if some_bus < bus:
                bus = some_bus
    return bus[0] * bus[1]


def part2(lines):
    next(lines)
    buses, diffs = [], []
    for i, bid in enumerate(next(lines).split(",")):
        if bid != "x":
            bid = int(bid)
            buses.append(bid)
            diffs.append(bid - i)
    return crt(buses, diffs)[0]
