#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import re


def part1(lines):
    rules, msg = read(lines)
    regex = re.compile(regexify(rules))
    return sum(1 for m in msg if regex.fullmatch(m))


def part2(lines):
    rules, msg = read(lines)
    rules["8"] = [r.split() for r in "42 | 42 8".split(" | ")]
    rules["11"] = [r.split() for r in "42 31 | 42 11 31".split(" | ")]
    regex = re.compile(regexify(rules))
    return sum(1 for m in msg if regex.fullmatch(m))


def read(lines):
    rules_str, msg = "".join(lines).split("\n\n")
    rules = {}
    for n, rule in (rb.split(": ", 1) for rb in rules_str.splitlines()):
        if rule[0] != '"':
            rule = [r.split() for r in rule.split(" | ")]
        rules[n] = rule
    return rules, msg.splitlines()


def regexify(rules, n="0", depth=0):
    rule = rules[n]
    if rule[0] == '"':
        return rule[1]
    if depth > 13:  # first tried 42 and got the star (but 13 is enough ;-)
        return ""
    exp = ("".join(regexify(rules, n, depth + 1) for n in r) for r in rule)
    return "(?:" + "|".join(exp) + ")"
