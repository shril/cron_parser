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

    def __init__(self, field) -> None:
        super().__init__(field, MonthField.RANGE)

    def get_values(self, **kwargs) -> list[int] | None:
        return super().get_values(self.__class__.__name__)


class DayOfWeekField(BaseField):
    RANGE = (1, 7)

    def __init__(self, field) -> None:
        super().__init__(field, DayOfWeekField.RANGE)

    def get_values(self, **kwargs) -> list[int] | None:
        return super().get_values(self.__class__.__name__)
