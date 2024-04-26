import sys
import os

currentPath = os.path.dirname(os.path.abspath(__file__))
abspath = currentPath + "/../src/cron_parser"
sys.path.append(abspath)

from cron_expression import CronExpression


def test_cron_expression():
    cron_string = "/15 6 1,15 * 1-5 /usr/bin/find"
    value = CronExpression().get_fields_and_values(cron_string)

    assert value.get('minute') == [0, 15, 30, 45]
    assert value.get('hour') == [6]
    assert value.get('day of month') == [1, 15]
    assert value.get('month') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert value.get('day of week') == [1, 2, 3, 4, 5]
    assert value.get('command') == '/usr/bin/find'
    
