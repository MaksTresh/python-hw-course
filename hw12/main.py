def fibonacchi(n: int) -> int:
    f1 = 0
    f2 = 1

    for _ in range(n):
        f1, f2 = f2, f1 + f2

    return f1


if __name__ == '__main__':
    input_number = int(input('> '))
    print(fibonacchi(input_number))
