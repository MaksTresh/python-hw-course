from functools import reduce


def solve_problem_6() -> int:
    return sum([i for i in range(101)])**2 - sum([i**2 for i in range(101)])


def solve_problem_9() -> int:
    return [a * b * c for a in range(1, 500) for b in range(1, 500) for c in range(1, 500)
            if a**2 + b**2 == c**2 and a + b + c == 1000][0]


def solve_problem_40() -> int:
    return reduce(lambda x, y: x * y, [int(''.join([str(i) for i in range(1, 300000)])[10**j - 1]) for j in range(7)])


def solve_problem_48() -> str:
    return str(sum([i**i for i in range(1, 1001)]))[-10:]


if __name__ == '__main__':
    print('Problem 6:', solve_problem_6())
    print('Problem 9:', solve_problem_9())
    print('Problem 40:', solve_problem_40())
    print('Problem 48:', solve_problem_48())
