#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


def part1(lines):
    return max(map(get_seat_id, lines))


def part2(lines):
    seats = sorted(map(get_seat_id, lines))
    for i, seat in enumerate(seats, seats[0]):
        if i != seat:
            return i


def get_seat_id(address):
    row, col = address[:7], address[7:]
    row = row.replace("F", "0").replace("B", "1")
    col = col.replace("L", "0").replace("R", "1")
    return int(row, 2) * 8 + int(col, 2)
