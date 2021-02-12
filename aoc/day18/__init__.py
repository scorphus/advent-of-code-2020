#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import strip
from ast import *  # NOQA

import ast


def part1(lines):
    total = 0
    for line in strip(lines):
        expr = line.replace("*", "-")
        dump = ast.dump(ast.parse(expr)).replace("Sub", "Mult")
        expr = ast.unparse(eval(dump))
        total += eval(expr)
    return total


def part2(lines):
    total = 0
    for line in strip(lines):
        expr = line.replace("*", "-").replace("+", "*")
        dump = ast.dump(ast.parse(expr)).replace("Mult", "Add").replace("Sub", "Mult")
        expr = ast.unparse(eval(dump))
        total += eval(expr)
    return total
