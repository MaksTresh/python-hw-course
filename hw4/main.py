import re


if __name__ == '__main__':
    input_str = input('> ')
    numbers = list(map(int, re.findall(r'-?\d+', input_str)))
    print(sum(numbers))
