#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import collections
import graphlib


def part1(lines):
    graph = {}
    for line in lines:
        bag, bags = parse_line(line)
        for _, each_bag in bags:
            graph.setdefault(each_bag, []).append(bag)
    visited = bfs(graph, "shiny gold")
    return len(visited) - 1


def part2(lines):
    graph = {}
    bags_in_bag = {}
    for line in lines:
        bag, bags = parse_line(line)
        graph[bag] = set(b for _, b in bags)
        bags_in_bag[bag] = bags
    qtt_acc = {}
    for bag in graphlib.TopologicalSorter(graph).static_order():
        total = 1
        for qtt, bag_in in bags_in_bag[bag]:
            total += qtt * qtt_acc[bag_in]
        qtt_acc[bag] = total
        if bag == "shiny gold":
            return qtt_acc[bag] - 1


def parse_bags(bags):
    bag_list = []
    for bag in bags.split(", "):
        qtt, shade, color, _ = bag.split(maxsplit=3)
        bag_list.append((int(qtt), f"{shade} {color}"))
    return bag_list


def parse_line(line):
    if " contain no " not in line:
        bag, bags = line.strip().split(" bags contain ")
    else:
        bag, _ = line.strip().split(" bags contain ")
        bags = None
    return bag, parse_bags(bags) if bags else []


def bfs(bags, start):
    visited = {start}
    next_bags = collections.deque([start])
    while next_bags:
        bag = next_bags.popleft()
        if bag not in bags:
            continue
        for next_bag in bags[bag]:
            if next_bag not in visited:
                next_bags.append(next_bag)
                visited.add(next_bag)
    return visited
