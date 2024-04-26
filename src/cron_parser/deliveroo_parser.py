import os
from cron_expression import CronExpression


class CronParser:
    def __init__(self, cron_string):
        self.cron_string = cron_string
        self.fields_map = CronExpression.get_fields_and_values(cron_string)
        self.output_data = CronExpression.generate_output(self.fields_map)

    def get_output_data(self):
        return self.output_data

    def find_next_n_occurrences(self, n):
        CronExpression.find_next_n_occurrences(self.fields_map, n)
