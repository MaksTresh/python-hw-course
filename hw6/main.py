def is_decimal_palindrome(number: int) -> bool:
    if str(number) == str(number)[::-1]:
        return True
    return False


def is_binary_palindrome(number: int) -> bool:
    binary_number = bin(number)[2:]
    if binary_number == binary_number[::-1]:
        return True
    return False


if __name__ == '__main__':
    total_sum = 0

    for i in range(1000000):
        if is_decimal_palindrome(i) and is_binary_palindrome(i):
            total_sum += i

    print(total_sum)
