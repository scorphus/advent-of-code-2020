#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import strip


# fmt: off
DIRS = {
    "e":  ( 1,  0),  # noqa
    "w":  (-1,  0),  # noqa
    "nw": (-1,  1),  # noqa
    "se": ( 1, -1),  # noqa
    "ne": ( 0,  1),  # noqa
    "sw": ( 0, -1),  # noqa
}
# fmt: on


def part1(lines):
    return sum(read(lines).values())


def part2(lines, days=100):
    tiles = set(p for p, c in read(lines).items() if c)
    for _ in range(days):
        tiles = flip(tiles)
    return len(tiles)


def read(lines):
    tiles = {}
    for line in strip(lines):
        line = line.rstrip("\n")
        x, y = 0, 0
        while line:
            for dir_, (dx, dy) in DIRS.items():
                if line.startswith(dir_):
                    x += dx
                    y += dy
                    line = line[len(dir_) :]
                    continue
        tiles[x, y] = not tiles.get((x, y), False)
    return tiles


def flip(tiles):
    adjacent, next_tiles = {}, set()
    for tile in tiles:
        for deltas in DIRS.values():
            adj = tuple(c + d for c, d in zip(tile, deltas))
            adjacent[adj] = adjacent.get(adj, 0) + 1
    for tile, adj in adjacent.items():
        if tile not in tiles and adj == 2 or tile in tiles and 0 < adj < 3:
            next_tiles.add(tile)
    return next_tiles
