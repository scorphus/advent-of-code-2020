#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers_list
from aoc import strip
from dataclasses import dataclass
from dataclasses import field


VERBOSE = False


def part1(lines, moves=100):
    cups = integers_list(next(strip(lines)))
    n = len(cups)
    for _ in range(moves):
        cur = cups[0]
        trio = cups[1:4]
        del cups[1:4]
        dest = cur - 1
        while dest in trio or dest < 1:
            if dest < 1:
                dest = n
            else:
                dest -= 1
        cups += cups
        dest_i = cups.index(dest)
        cups = cups[1 : dest_i + 1] + trio + cups[dest_i + 1 : n - 3] + [cur]
    one_i = cups.index(1)
    return "".join(map(str, cups[one_i + 1 :] + cups[:one_i]))


def part2(lines, n=1_000_000, moves=10_000_000):
    last = Cup(0)
    cups = {0: last}
    for c in integers_list(next(strip(lines))) + list(range(10, n + 1)):
        last.next = cup = Cup(c)
        last = cups[c] = cup
    cur = last.next = cups[0].next
    for _ in range(moves):
        trio_head, *trio = pick(cur)
        dest = cur.label - 1
        while dest in trio or dest < 1:
            if dest < 1:
                dest = n
            else:
                dest -= 1
        trio_head.next.next.next = cups[dest].next
        cups[dest].next = trio_head
        cur = cur.next
    return cups[1].next.label * cups[1].next.next.label


@dataclass
class Cup:
    label: int
    next: "typing.Any" = field(default=None, repr=VERBOSE)  # NOQA


def pick(cur):
    yield cur.next
    for _ in range(3):
        yield cur.next.label
        cur.next = cur.next.next
