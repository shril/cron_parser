import sys
import os
import pytest

currentPath = os.path.dirname(os.path.abspath(__file__))
abspath = currentPath + "/../src/cron_parser"
sys.path.append(abspath)

from cron_fields import MinuteField, HourField, DayOfWeekField, MonthField, DayOfMonthField
from cron_exceptions import ArgumentException, InvalidValueException


def test_valid_minute_field():
    assert MinuteField("*").get_values() == list(range(60))
    assert MinuteField("1,2,3,4").get_values() == [1, 2, 3, 4]
    assert MinuteField("20-30").get_values() == list(range(20, 31))
    assert MinuteField("*/5").get_values() == list(range(0, 60, 5))
    assert MinuteField("20/5").get_values() == list(range(20, 60, 5))
    assert MinuteField("0").get_values() == [0]


def test_invalid_minute_field():
    with pytest.raises(InvalidValueException):
        MinuteField("62").get_values()
    with pytest.raises(InvalidValueException):
        MinuteField("61,62").get_values()
    with pytest.raises(InvalidValueException):
        MinuteField("#").get_values()


def test_valid_hour_field():
    assert HourField("*").get_values() == list(range(24))
    assert HourField("1,2,3,4").get_values() == [1, 2, 3, 4]
    assert HourField("2-5").get_values() == list(range(2, 6))
    assert HourField("*/5").get_values() == list(range(0, 24, 5))
    assert HourField("20/5").get_values() == list(range(20, 24, 5))
    assert HourField("7").get_values() == [7]


def test_invalid_hour_field():
    with pytest.raises(InvalidValueException):
        HourField("25").get_values()
    with pytest.raises(InvalidValueException):
        HourField("24,25").get_values()
    with pytest.raises(InvalidValueException):
        HourField("%").get_values()


def test_valid_day_of_month_field():
    assert DayOfMonthField("*").get_values() == list(range(1, 32))
    assert DayOfMonthField("1,2,3,4").get_values() == [1, 2, 3, 4]
    assert DayOfMonthField("12-25").get_values() == list(range(12, 26))
    assert DayOfMonthField("*/5").get_values() == list(range(1, 32, 5))
    assert DayOfMonthField("20/5").get_values() == list(range(20, 32, 5))
    assert DayOfMonthField("7").get_values() == [7]


def test_invalid_day_of_month_field():
    with pytest.raises(InvalidValueException):
        DayOfMonthField("32").get_values()
    with pytest.raises(InvalidValueException):
        DayOfMonthField("31,32").get_values()
    with pytest.raises(InvalidValueException):
        DayOfMonthField("@").get_values()


def test_valid_month_field():
    assert MonthField("*").get_values() == list(range(1, 13))
    assert MonthField("3,4,11,12").get_values() == [3, 4, 11, 12]
    assert MonthField("10-12").get_values() == list(range(10, 13))
    assert MonthField("*/5").get_values() == list(range(1, 13, 5))
    assert MonthField("2/2").get_values() == list(range(2, 13, 2))
    assert MonthField("7").get_values() == [7]


def test_invalid_month_field():
    with pytest.raises(InvalidValueException):
        MonthField("13").get_values()
    with pytest.raises(InvalidValueException):
        MonthField("12,13").get_values()
    with pytest.raises(InvalidValueException):
        MonthField("$").get_values()


def test_valid_day_of_week_field():
    assert DayOfWeekField("*").get_values() == list(range(1, 8))
    assert DayOfWeekField("1,2,3,4").get_values() == [1, 2, 3, 4]
    assert DayOfWeekField("2-5").get_values() == list(range(2, 6))
    assert DayOfWeekField("*/3").get_values() == list(range(1, 8, 3))
    assert DayOfWeekField("2/5").get_values() == list(range(2, 8, 5))
    assert DayOfWeekField("7").get_values() == [7]


def test_invalid_day_of_week_field():
    with pytest.raises(InvalidValueException):
        DayOfWeekField("8").get_values()
    with pytest.raises(InvalidValueException):
        DayOfWeekField("7,8").get_values()
    with pytest.raises(InvalidValueException):
        DayOfWeekField("A").get_values()
