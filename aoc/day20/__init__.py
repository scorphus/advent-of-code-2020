#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


SEA_MONSTER = (
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
)


def part1(lines):
    tiles = dict(read(lines))
    img = assemble(tiles)
    return img[0][0][2] * img[0][-1][2] * img[-1][0][2] * img[-1][-1][2]


def part2(lines):
    tiles = dict(read(lines))
    img = assemble(tiles)
    img = concat(img)
    monster = [int(seg.replace(" ", "0").replace("#", "1"), 2) for seg in SEA_MONSTER]
    monster_length = len(SEA_MONSTER[0])
    monster_weight = "".join(SEA_MONSTER).count("#")
    monsters = find_sea_monsters(img, monster, monster_length)
    return "".join("".join(r) for r in img).count("1") - monsters * monster_weight


def read(lines):
    tiles = "".join(lines).split("\n\n")
    for title, tile in (t.rstrip().split("\n", maxsplit=1) for t in tiles):
        tid = int(title.rstrip(":").split(maxsplit=1)[1])
        yield tid, list(parse(tile))


def parse(tile):
    tile = [list(r) for r in tile.replace("#", "1").replace(".", "0").splitlines()]
    for i in range(8):
        yield borders(tile), tile
        tile = list(rotate(tile))
        if i == 3:
            tile = [r[::-1] for r in tile]


def rotate(tile):
    for x in range(len(tile[0])):
        yield [r[-x - 1] for r in tile]


def borders(tile):
    left = int("".join(t[0] for t in tile), 2)
    right = int("".join(t[-1] for t in tile), 2)
    top = int("".join(tile[0]), 2)
    bot = int("".join(tile[-1]), 2)
    return left, right, top, bot


def assemble(tiles):
    size = int(len(tiles) ** 0.5)
    return assemble_dfs(tiles, [[None] * size for _ in range(size)], set())


def assemble_dfs(tiles, img, placed, row=0, col=0):
    rc = row, col + 1
    if col == len(img) - 1:
        rc = row + 1, 0
    for tid, tile in tiles.items():
        if tid not in placed:
            placed.add(tid)
            for i, ((left, right, top, bot), ith_tile) in enumerate(tile):
                if (row > 0 and img[row - 1][col][1] != top) or (
                    col > 0 and img[row][col - 1][0] != left
                ):
                    continue
                img[row][col] = right, bot, tid, i, ith_tile
                assemble_dfs(tiles, img, placed, *rc)
                if len(placed) == len(tiles):
                    return img
            placed.remove(tid)


def concat(img):
    size = len(img) * (len(img[0][0][-1]) - 2)
    final_img = [[] for _ in range(size)]
    r = 0
    for row in img:
        for *_, tile in row:
            for y, line in enumerate(tile[1:-1]):
                final_img[r + y] += line[1:-1]
        r += len(tile) - 2
    return final_img


def find_sea_monsters(img, monster, monster_length):
    for i in range(8):
        count = 0
        img_dec = [int("".join(row), 2) for row in img]
        for r, rows in enumerate(zip(img_dec[:-2], img_dec[1:-1], img_dec[2:]), 1):
            for s in range(len(img[0]) - monster_length):
                count += all(r & m << s == m << s for r, m in zip(rows, monster))
        if count:
            return count
        img = list(rotate(img))  # pragma: no cover (🤷🏻‍♂️)
        if i == 3:  # pragma: no cover (🤷🏻‍♂️)
            img = [r[::-1] for r in img]
