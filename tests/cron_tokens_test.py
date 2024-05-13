import sys
import os
import pytest

currentPath = os.path.dirname(os.path.abspath(__file__))
abspath = currentPath + "/../src/cron_parser"
sys.path.append(abspath)

from cron_expression import CronExpression
from cron_exceptions import ArgumentException, InvalidValueException


def test_default_cron_string():
    cron_string = "*/15 6 1,15 * 1-5 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == [0, 15, 30, 45]
    assert value.get('hour') == [6]
    assert value.get('day of month') == [1, 15]
    assert value.get('month') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert value.get('day of week') == [1, 2, 3, 4, 5]
    assert value.get('command') == '/usr/bin/find'


def test_wildcard():
    cron_string = "* * * * * /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == list(range(0, 60))
    assert value.get('hour') == list(range(0, 24))
    assert value.get('day of month') == list(range(1, 32))
    assert value.get('month') == list(range(1, 13))
    assert value.get('day of week') == list(range(1, 8))
    assert value.get('command') == '/usr/bin/find'


def test_comma():
    cron_string = "1,2,3,4 7,8,9 25,26 1,2 6,7 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == [1, 2, 3, 4]
    assert value.get('hour') == [7, 8, 9]
    assert value.get('day of month') == [25, 26]
    assert value.get('month') == [1, 2]
    assert value.get('day of week') == [6, 7]
    assert value.get('command') == '/usr/bin/find'


def test_range():
    cron_string = "1-5 6-10 15-20 1-12 1-7 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == list(range(1, 6))
    assert value.get('hour') == list(range(6, 11))
    assert value.get('day of month') == list(range(15, 21))
    assert value.get('month') == list(range(1, 13))
    assert value.get('day of week') == list(range(1, 8))
    assert value.get('command') == '/usr/bin/find'


def test_step_range():
    cron_string = "*/5 */2 */3 */4 */2 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == list(range(0, 60, 5))
    assert value.get('hour') == list(range(0, 24, 2))
    assert value.get('day of month') == list(range(1, 32, 3))
    assert value.get('month') == list(range(1, 13, 4))
    assert value.get('day of week') == list(range(1, 8, 2))
    assert value.get('command') == '/usr/bin/find'


def test_step_range_with_with_beginning():
    cron_string = "2/5 5/2 10/3 5/4 3/2 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == list(range(2, 60, 5))
    assert value.get('hour') == list(range(5, 24, 2))
    assert value.get('day of month') == list(range(10, 32, 3))
    assert value.get('month') == list(range(5, 13, 4))
    assert value.get('day of week') == list(range(3, 8, 2))
    assert value.get('command') == '/usr/bin/find'


def test_value():
    cron_string = "1 6 15 11 5 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == [1]
    assert value.get('hour') == [6]
    assert value.get('day of month') == [15]
    assert value.get('month') == [11]
    assert value.get('day of week') == [5]
    assert value.get('command') == '/usr/bin/find'
