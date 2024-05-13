import re
from cron_fields import MinuteField, HourField, DayOfWeekField, MonthField, DayOfMonthField


class CronExpression:
    @staticmethod
    def get_fields_and_values(cron_string: str) -> dict:
        minute, hour, day_of_month, month, day_of_week, *command = cron_string.split()
        year = None
        if len(command) > 1 and command[0].isdigit():
            year, *new_command = command[0], command[1:]
        else:
            new_command = command
        return {
            'minute': MinuteField(minute).get_values(),
            'hour': HourField(hour).get_values(),
            'day of month': DayOfMonthField(day_of_month).get_values(),
            'month': MonthField(month).get_values(),
            'day of week': DayOfWeekField(day_of_week).get_values(),
            'year': year,
            'command': new_command
        }

    @staticmethod
    def generate_output(fields_map: dict) -> str:
        lines = []
        for field, values in fields_map.items():
            if field == 'command':
                line = f'{field:<14} {values}'
            elif field == 'year':
                line = f'{field:<14} {values}'
            else:
                line = f'{field:<14} {" ".join(map(str, values))}'
            lines.append(line)
        return '\n'.join(lines)
