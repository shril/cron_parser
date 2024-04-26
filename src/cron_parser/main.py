import argparse
from cron_expression import CronExpression
from cron_exceptions import ArgumentException


def main(cron_string):
    if len(cron_string.split()) != 6:
        raise ArgumentException('Cron string should have 6 fields')
    fields_map = CronExpression.get_fields_and_values(cron_string)
    output_data = CronExpression.generate_output(fields_map)
    print(output_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cron Expression Parser.')
    parser.add_argument('cron_string', type=str, help='Cron string to parse')
    args = parser.parse_args()
    main(args.cron_string)
