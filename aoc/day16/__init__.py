#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers_list

import itertools


def part1(lines):
    total = 0
    fields, _, tickets = read(lines)
    for val in itertools.chain.from_iterable(tickets):
        for lo, hi in itertools.chain.from_iterable(fields.values()):
            if lo <= val <= hi:
                break
        else:
            total += val
    return total


def part2(lines, prefix="departure"):
    fields, my_ticket, tickets = read(lines)
    field_sets = [set(fields) for _ in range(len(my_ticket))]
    solo_i = None
    for ticket in tickets:
        for val in ticket:
            for lo, hi in itertools.chain.from_iterable(fields.values()):
                if lo <= val <= hi:
                    break
            else:
                break
        else:
            for i, val in enumerate(ticket):
                for field, ((lo_a, hi_a), (lo_b, hi_b)) in fields.items():
                    if val < lo_a or val > hi_a and val < lo_b or val > hi_b:
                        field_sets[i].discard(field)
                        if len(field_sets[i]) == 1:
                            solo_i = i
    while solo_i is not None:
        solo, solo_i = field_sets[solo_i], None
        for i, field_set in enumerate(field_sets):
            if len(field_set) == 1:
                continue
            field_set.difference_update(solo)
            if len(field_set) == 1:
                solo_i = i
    prod = 1
    for i, field_set in enumerate(field_sets):
        if field_set.pop().startswith(prefix):
            prod *= my_ticket[i]
    return prod


def read(lines):
    fields_block, my_ticket, tickets = "".join(lines).split("\n\n")
    fields = {}
    for f in fields_block.splitlines():
        name, values = f.split(": ")
        fields[name] = [integers_list(v.split("-")) for v in values.split(" or ")]
    my_ticket = integers_list(my_ticket.splitlines()[1].split(","))
    tickets = [integers_list(t.split(",")) for t in tickets.splitlines()[1:]]
    return fields, my_ticket, tickets
