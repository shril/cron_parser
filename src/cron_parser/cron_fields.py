from __future__ import annotations
from cron_tokens import WildcardToken, RangeToken, StepRangeToken, CommaToken, ValueToken


class BaseField(object):
    def __init__(self, field, range: tuple[int, int]) -> None:
        self.field = field
        self.range = range

    def get_values(self, field_type) -> list[int] | None:
        if self.field == '*':
            return WildcardToken(self.range, field_type).generate_values()
        elif '/' in self.field:
            return StepRangeToken(self.range, field_type, self.field).generate_values()
        elif '-' in self.field:
            return RangeToken(self.range, field_type, self.field).generate_values()
        elif ',' in self.field:
            return CommaToken(self.range, field_type, self.field).generate_values()
        else:
            return ValueToken(self.range, field_type, self.field).generate_values()

    @staticmethod
    def name_to_digit_mapper(field, mapper):
        has_name = False
        field = field.lower()
        for name, value in mapper.items():
            if name in field:
                field = field.replace(name, value)
                has_name = True
        return field, has_name

    @staticmethod
    def digit_to_name_mapper(result, mapper):
        return [mapper[value].upper() for value in result]


class MinuteField(BaseField):
    RANGE = (0, 59)

    def __init__(self, field) -> None:
        super().__init__(field, range=MinuteField.RANGE)

    def get_values(self, **kwargs) -> list[int] | None:
        return super().get_values(self.__class__.__name__)


class HourField(BaseField):
    RANGE = (0, 23)

    def __init__(self, field) -> None:
        super().__init__(field, range=HourField.RANGE)

    def get_values(self, **kwargs) -> list[int] | None:
        return super().get_values(self.__class__.__name__)


class DayOfMonthField(BaseField):
    RANGE = (1, 31)

    def __init__(self, field) -> None:
        super().__init__(field, DayOfMonthField.RANGE)

    def get_values(self, **kwargs) -> list[int] | None:
        return super().get_values(self.__class__.__name__)


class MonthField(BaseField):
    RANGE = (1, 12)
    MONTHS_MAP = {
        'jan': '1',
        'feb': '2',
        'mar': '3',
        'apr': '4',
        'may': '5',
        'jun': '6',
        'jul': '7',
        'aug': '8',
        'sep': '9',
        'oct': '10',
        'nov': '11',
        'dec': '12',
    }
    INVERTED_MONTHS_MAP = {int(v): k for k, v in MONTHS_MAP.items()}

    def __init__(self, field) -> None:
        processed_field, self.has_name = BaseField.name_to_digit_mapper(field, MonthField.MONTHS_MAP)
        super().__init__(processed_field, MonthField.RANGE)

    def get_values(self, **kwargs) -> list[int | str] | None:
        result = super().get_values(self.__class__.__name__)
        return result if not self.has_name else BaseField.digit_to_name_mapper(result, MonthField.INVERTED_MONTHS_MAP)


class DayOfWeekField(BaseField):
    RANGE = (1, 7)
    DAY_OF_WEEK_MAP = {
        'sun': '1',
        'mon': '2',
        'tue': '3',
        'wed': '4',
        'thu': '5',
        'fri': '6',
        'sat': '7',
    }
    INVERTED_DAY_OF_WEEK_MAP = {int(v): k for k, v in DAY_OF_WEEK_MAP.items()}

    def __init__(self, field) -> None:
        processed_field, self.has_name = BaseField.name_to_digit_mapper(field, DayOfWeekField.DAY_OF_WEEK_MAP)
        super().__init__(processed_field, DayOfWeekField.RANGE)

    def get_values(self, **kwargs) -> list[int | str] | None:
        result = super().get_values(self.__class__.__name__)
        return result if not self.has_name else BaseField.digit_to_name_mapper(
            result, DayOfWeekField.INVERTED_DAY_OF_WEEK_MAP
        )
