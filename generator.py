from typing import Callable
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    matches = re.findall(r'\ \d+(?:\.\d+)?\ ', text)
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable):
    sum_numbers = sum(func(text))
    return sum_numbers


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
