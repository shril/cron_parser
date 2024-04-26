from __future__ import annotations


class Token:
    def __init__(self, range: tuple[int, int], field_type: str, field: str | None):
        self.field_type = field_type.replace('Field', '')
        self.range_min, self.range_max = range
        self.field = field


class WildcardToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str):
        super().__init__(range, field_type, None)

    def generate_values(self):
        return list(range(self.range_min, self.range_max + 1))


class CommaToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str):
        super().__init__(range, field_type, field)

    def generate_values(self):
        result = [int(value) for value in self.field.split(',')]
        for item in result:
            if self.range_min <= item <= self.range_max:
                continue
            else:
                raise ValueError(f'{self.field_type} Value {item} out of range')
        return result


class RangeToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str):
        super().__init__(range, field_type, field)

    def generate_values(self):
        start, end = self.field.split('-')
        result = list(range(int(start), int(end) + 1))
        for item in result:
            if self.range_min <= item <= self.range_max:
                continue
            else:
                raise ValueError(f'{self.field_type} Value {item} out of range')
        return result


class StepRangeToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str):
        super().__init__(range, field_type, field)

    def generate_values(self):
        _, step = self.field.split('/')
        result = list(range(self.range_min, self.range_max + 1, int(step)))
        for item in result:
            if self.range_min <= item <= self.range_max:
                continue
            else:
                raise ValueError(f'{self.field_type} Value {item} out of range')
        return result


class ValueToken(Token):
    def __init__(self, range: tuple[int, int], field_type: str, field: str):
        super().__init__(range, field_type, field)

    def generate_values(self):
        if self.field.isdigit():
            if self.range_min <= int(self.field) <= self.range_max:
                return [int(self.field)]
            else:
                raise ValueError(f'{self.field_type} Value {self.field} out of range')
        else:
            raise ValueError(f'{self.field_type} Value {self.field} is not a number')
