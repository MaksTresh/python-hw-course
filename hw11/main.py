def letters_range(start: str, stop: str, step: int = 1) -> str:
    for i in range(ord(start.lower()), ord(stop.lower()), step):
        yield chr(i)


if __name__ == '__main__':
    print(list(letters_range('b', 'w', 2)))
    print(list(letters_range('a', 'g')))
    print(list(letters_range('g', 'p')))
    print(list(letters_range('p', 'g', -2)))
    print(list(letters_range('a','a')))
