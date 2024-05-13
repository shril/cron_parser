from cron_fields import MinuteField, HourField, DayOfWeekField, MonthField, DayOfMonthField
from datetime import datetime


class CronExpression:
    @staticmethod
    def get_fields_and_values(cron_string: str) -> dict:
        minute, hour, day_of_month, month, day_of_week, command = cron_string.split()
        return {
            'minute': MinuteField(minute).get_values(),
            'hour': HourField(hour).get_values(),
            'day of month': DayOfMonthField(day_of_month).get_values(),
            'month': MonthField(month).get_values(),
            'day of week': DayOfWeekField(day_of_week).get_values(),
            'command': command
        }

    @staticmethod
    def generate_output(fields_map: dict) -> str:
        lines = []
        for field, values in fields_map.items():
            if field == 'command':
                line = f'{field:<14} {values}'
            else:
                line = f'{field:<14} {" ".join(map(str, values))}'
            lines.append(line)
        return '\n'.join(lines)

    @staticmethod
    def find_next_n_occurrences(parsed_cron, n):
        current_time = datetime.now()
        current_year = current_time.year
        next_occurrences = []

        while len(next_occurrences) < n:
            for month in parsed_cron['month']:
                if current_time.year == current_year and current_time.month < month:
                    continue
                for day_of_month in parsed_cron['day of month']:
                    for hour in parsed_cron['hour']:
                        for minute in parsed_cron['minute']:
                            try:
                                next_time = datetime(current_year, month, day_of_month, hour, minute)
                                if current_time <= next_time and next_time.weekday() + 1 in parsed_cron['day of week']:
                                    next_occurrences.append(next_time.strftime('%Y-%m-%d %H:%M'))
                            except ValueError:
                                continue
            current_year += 1
        print(next_occurrences)
