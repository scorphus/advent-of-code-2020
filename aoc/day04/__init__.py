#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

field_names = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def part1(lines):
    valid = 0
    passports = "".join(lines).split("\n\n")
    for passport in passports:
        fields = passport.count(":")
        if fields < len(field_names) - 1:
            continue
        if fields < len(field_names) and "cid:" in passport:
            continue
        valid += 1
    return valid


def part2(lines):
    valid = 0
    passports = "".join(lines).split("\n\n")
    for passport in passports:
        fields = passport.count(":")
        if fields < len(field_names) - 1:
            continue
        if fields < len(field_names) and "cid:" in passport:
            continue
        if is_valid(passport):
            valid += 1
    return valid


def is_valid(passport):
    valid_hair_colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    fields = dict(p.split(":") for p in passport.strip().split())
    try:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        assert len(fields["byr"]) == 4 and 1920 <= int(fields["byr"]) <= 2002
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        assert len(fields["iyr"]) == 4 and 2010 <= int(fields["iyr"]) <= 2020
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        assert len(fields["eyr"]) == 4 and 2020 <= int(fields["eyr"]) <= 2030
        # hgt (Height) - a number followed by either cm or in:
        assert fields["hgt"].endswith("cm") or fields["hgt"].endswith("in")
        hgt = int(fields["hgt"].replace("cm", "").replace("in", ""))
        # If cm, the number must be at least 150 and at most 193.
        assert not fields["hgt"].endswith("cm") or 150 <= hgt <= 193
        # If in, the number must be at least 59 and at most 76.
        assert not fields["hgt"].endswith("in") or 59 <= hgt <= 76
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        assert len(fields["hcl"]) == 7 and fields["hcl"].startswith("#")
        int(fields["hcl"][1:], 16)
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        assert fields["ecl"] in valid_hair_colors
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        assert len(fields["pid"]) == 9
        int(fields["pid"])
    except:  # NOQA
        return False
    return True
