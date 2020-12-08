#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


def part1(lines):
    inst = read(lines)
    return run(inst)[0]


def part2(lines):
    orig_inst = read(lines)
    acc = 0
    for ii, (ik, iv, _) in enumerate(orig_inst):
        if ik == "acc":
            continue
        inst = orig_inst.copy()
        if ik == "jmp":
            inst[ii] = "nop", iv, False
        else:
            inst[ii] = "jmp", iv, False
        acc, ok = run(inst)
        if ok:
            return acc


def read(lines):
    inst = []
    for line in lines:
        ik, iv = line.rstrip("\n").split(" ")
        inst.append((ik, int(iv), False))
    return inst


def run(inst):
    ii = acc = 0
    ik, iv, ib = inst[ii]
    while not ib:
        if ik == "jmp":
            ii += iv
        else:
            ii += 1
            if ik == "acc":
                acc += iv
        try:
            ik, iv, ib = inst[ii]
        except IndexError:
            return acc, True
        inst[ii] = ik, iv, True
    return acc, False
