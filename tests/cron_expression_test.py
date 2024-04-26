import pytest

from src.cron_parser.cron_expression import CronExpression


class CronExpressionTest:

    @staticmethod
    def test_cron_expression():
        cron_string = "/15 6 1,15 * 1-5 /usr/bin/find"
        value = CronExpression(cron_string)
        assert value.get('minute') == [0, 15, 30, 45]
        assert value.get('hour') == [6]
        assert value.get('day of month') == [1, 15]
        assert value.get('month') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        assert value.get('day of week') == [1, 2, 3, 4, 5]
        assert value.get('command') == '/usr/bin/find'
