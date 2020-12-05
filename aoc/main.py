#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc import integers
from importlib import import_module

import subprocess
import sys


def aoc():
    try:
        day, part, *_ = integers(sys.argv[-1].split("."))
    except (IndexError, IOError, ValueError):
        print("Try: `aoc < input/day01 1.1` or `aoc input/day07 7.2`")
        exit(1)
    day_part = import_day_part(day, part)
    if sys.stdin.isatty():
        with open(sys.argv[-2]) as input_file:
            answer = day_part(input_file)
    else:
        answer = day_part(sys.stdin)
    if not answer:
        print("⛔️")
        exit(1)
    copy_to_clipboard(f"{answer}".encode())
    print(f"Your answer is: {answer} (already copied to clipboard)")


def import_day_part(day, part):
    day = import_module(f"aoc.day{day:02d}")
    return getattr(day, f"part{part}", None)


def copy_to_clipboard(text):
    subprocess.run("pbcopy", input=text)
