#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Advent of Code 2020
# https://github.com/scorphus/advent-of-code-2020

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from aoc.main import aoc
from aoc.main import copy_to_clipboard
from aoc.main import import_day_part

import pytest
import sys


def test_aoc(import_day_part_mock, copy_to_clipboard_mock, capsys):
    aoc()
    import_day_part_mock.return_value.assert_called_once_with(sys.stdin)
    import_day_part_mock.assert_called_once_with(1, 1)
    answer = import_day_part_mock.return_value.return_value
    copy_to_clipboard_mock.assert_called_once_with(f"{answer}".encode())
    assert f"{answer}" in capsys.readouterr().out


@pytest.mark.parametrize("argv, isatty", [(["input", "1.1"], True)])
def test_aoc_stdin_isatty(import_day_part_mock, copy_to_clipboard_mock, mocker, capsys):
    open_mock = mocker.patch("aoc.main.open")
    aoc()
    open_mock.assert_called_once_with("input")
    import_day_part_mock.return_value.assert_called_once_with(open_mock().__enter__())
    import_day_part_mock.assert_called_once_with(1, 1)
    answer = import_day_part_mock.return_value.return_value
    copy_to_clipboard_mock.assert_called_once_with(f"{answer}".encode())
    assert f"{answer}" in capsys.readouterr().out


def test_aoc_no_answer(mocker, capsys):
    day_part_mock = mocker.Mock(return_value=None)
    import_day_part_mock = mocker.patch(
        "aoc.main.import_day_part", return_value=day_part_mock
    )
    with pytest.raises(SystemExit):
        aoc()
    import_day_part_mock.assert_called_once_with(1, 1)
    assert capsys.readouterr().out == "⛔️\n"


@pytest.mark.parametrize("argv", [[], [""], ["1"], ["11"], ["1", "1"]])
def test_aoc_bad_args(capsys):
    with pytest.raises(SystemExit):
        aoc()
    assert capsys.readouterr().out.startswith("Try")


@pytest.mark.parametrize("day, part", [(1, 2), (2, 1)])
def test_import_day_part(day, part, mocker):
    mock = mocker.patch("aoc.main.import_module")
    day_part = import_day_part(day, part)
    assert day_part == getattr(mock.return_value, f"part{part}")
    mock.assert_called_once_with(f"aoc.day{day:02d}")


def test_copy_to_clipboard(mocker):
    mock = mocker.patch("aoc.main.subprocess")
    copy_to_clipboard("very wow text")
    mock.run.assert_called_once_with("pbcopy", input="very wow text")


@pytest.fixture
def import_day_part_mock(mocker):
    return mocker.patch("aoc.main.import_day_part")


@pytest.fixture
def copy_to_clipboard_mock(mocker):
    return mocker.patch("aoc.main.copy_to_clipboard")


@pytest.fixture(autouse=True)
def sys_mock(argv, isatty, mocker):
    mocker.patch.object(sys, "argv", ("aoc", *argv))
    mocker.patch.object(sys.stdin, "isatty", lambda: isatty)


@pytest.fixture
def argv():
    return ["1.1"]


@pytest.fixture
def isatty():
    return False
