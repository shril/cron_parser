from __future__ import annotations
from cron_exceptions import InvalidValueException


class Token:
    def __init__(self, range: tuple[int, int], field_type: str, field: str | None) -> None:
        self.field_type = field_type.replace('Field', '')
        self.range_min, self.range_max = range
        self.field = field

    def validate(self, result) -> None:
        for item in result:
            if self.range_min <= item <= self.range_max:
                continue
            else:
                raise InvalidValueException(f'{self.field_type} Value {item} out of range')

    def validate_value(self, value) -> None:
        self.validate([value])


class WildcardToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str) -> None:
        super().__init__(range, field_type, None)

    def generate_values(self) -> list[int] | None:
        return list(range(self.range_min, self.range_max + 1))


class CommaToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str) -> None:
        super().__init__(range, field_type, field)

    def generate_values(self) -> list[int] | None:
        result = [int(value) for value in self.field.split(',')]
        super().validate(result)
        return result


class RangeToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str) -> None:
        super().__init__(range, field_type, field)

    def generate_values(self) -> list[int] | None:
        start, end = self.field.split('-')
        result = list(range(int(start), int(end) + 1))
        super().validate(result)
        return result


class StepRangeToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str) -> None:
        super().__init__(range, field_type, field)

    def generate_values(self) -> list[int] | None:
        begin, step = self.field.split('/')
        start = self.range_min if begin == '*' or begin == '' else int(begin)
        super().validate_value(start)
        result = list(range(start, self.range_max + 1, int(step)))
        super().validate(result)
        return result


class ValueToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str) -> None:
        super().__init__(range, field_type, field)

    def generate_values(self) -> list[int] | None:
        if self.field.isdigit():
            super().validate_value(int(self.field))
            return [int(self.field)]
        else:
            raise InvalidValueException(f'{self.field_type} Value {self.field} is not a number')
