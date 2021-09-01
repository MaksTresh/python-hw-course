def count_collatz_algorithm_steps(number: int, steps: int = 0) -> int:
    if number == 1:
        return steps

    if number % 2 == 0:
        return count_collatz_algorithm_steps(number // 2, steps=steps+1)
    else:
        return count_collatz_algorithm_steps(number * 3 + 1, steps=steps+1)


if __name__ == '__main__':
    input_number = int(input('> '))
    print(count_collatz_algorithm_steps(input_number))
