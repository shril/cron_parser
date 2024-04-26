import argparse
from deliveroo_parser import CronParser


def main(cron_string):
    cron_parser = CronParser(cron_string)
    print(cron_parser.get_output_data())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cron Expression Parser.')
    parser.add_argument('cron_string', type=str, help='Cron string to parse')
    args = parser.parse_args()
    main(args.cron_string)
