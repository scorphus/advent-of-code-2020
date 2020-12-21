#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import strip

import itertools


def part1(lines):
    foods = list(read(lines))
    alle = set()
    for _, groups in itertools.groupby(sorted(explode(foods)), lambda x: x[0]):
        alle.update(set.intersection(*(g[1] for g in groups)))
    return sum(len(set(ing) - alle) for ing, _ in foods)


def part2(lines):
    foods = list(read(lines))
    danger = {}
    for alle, groups in itertools.groupby(sorted(explode(foods)), lambda x: x[0]):
        danger[alle] = set.intersection(*(g[1] for g in groups))
    uniq(danger)
    return ",".join(map(set.pop, danger.values()))


def read(lines):
    for line in strip(lines, "\n)"):
        ing, alle = line.split(" (contains ", 1)
        yield set(ing.split()), set(alle.split(", "))


def explode(foods):
    for ing, alle in foods:
        for a in alle:
            yield a, ing


def uniq(danger):
    solo_alle = set(k for k, v in danger.items() if len(v) == 1)
    while solo_alle:
        solo_ing = danger[solo_alle.pop()]
        for alle in danger:
            if len(danger[alle]) > 1:
                danger[alle].difference_update(solo_ing)
                if len(danger[alle]) == 1:
                    solo_alle.add(alle)
