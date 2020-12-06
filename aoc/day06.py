#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


def part1(lines):
    count = 0
    ans = "".join(lines).split("\n\n")
    for ans_g in ans:
        ans_g = ans_g.strip().replace("\n", "")
        count += len(set(ans_g))
    return count


def part2(lines):
    count = 0
    ans = "".join(lines).split("\n\n")
    for ans_g in ans:
        count_g = [0] * 26
        for ans_p in ans_g.splitlines():
            for let in ans_p:
                count_g[ord(let) - 97] += 1
        count += sum(c == len(ans_g.splitlines()) for c in count_g)
    return count
