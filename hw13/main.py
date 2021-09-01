from typing import Optional


def convert_temperature(*, celsius_value: Optional[float] = None, fahrenheit_value: Optional[float] = None) -> float:
    if celsius_value and fahrenheit_value:
        raise ValueError('two temperature parameters cannot be set at the same time')

    if celsius_value:
        return celsius_value * 1.8 + 32
    elif fahrenheit_value:
        return (fahrenheit_value - 32) / 1.8
    else:
        raise ValueError('one of the temperature value parameters must be set')


if __name__ == '__main__':
    print(convert_temperature(celsius_value=12))
    print(convert_temperature(fahrenheit_value=23))
