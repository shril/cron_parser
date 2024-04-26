import sys
import os
import pytest

currentPath = os.path.dirname(os.path.abspath(__file__))
abspath = currentPath + "/../src/cron_parser"
sys.path.append(abspath)

from cron_expression import CronExpression
from cron_exceptions import ArgumentException, InvalidValueException


def test_simple():
    cron_string = "/15 6 1,15 * 1-5 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == [0, 15, 30, 45]
    assert value.get('hour') == [6]
    assert value.get('day of month') == [1, 15]
    assert value.get('month') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert value.get('day of week') == [1, 2, 3, 4, 5]
    assert value.get('command') == '/usr/bin/find'


def test_all_wildcard():
    cron_string = "* * * * * /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == list(range(0, 60))
    assert value.get('hour') == list(range(0, 24))
    assert value.get('day of month') == list(range(1, 32))
    assert value.get('month') == list(range(1, 13))
    assert value.get('day of week') == list(range(1, 8))
    assert value.get('command') == '/usr/bin/find'


def test_all_comma():
    cron_string = "1,2,3,4 7,8,9 25,26 1,2 6,7 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == [1, 2, 3, 4]
    assert value.get('hour') == [7, 8, 9]
    assert value.get('day of month') == [25, 26]
    assert value.get('month') == [1, 2]
    assert value.get('day of week') == [6, 7]
    assert value.get('command') == '/usr/bin/find'


def test_minute_value_out_of_range():
    cron_string = "75 6 1,15 * 1-5 /usr/bin/find"
    with pytest.raises(InvalidValueException):
        CronExpression().get_fields_and_values(cron_string)


def test_minute_value_invalid():
    cron_string = "# 6 1,15 * 1-5 /usr/bin/find"
    with pytest.raises(InvalidValueException):
        CronExpression().get_fields_and_values(cron_string)
