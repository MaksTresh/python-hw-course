if __name__ == '__main__':
    input_str = input('> ')
    numbers = set(map(int, input_str.split()))
    max_number = max(numbers)

    for i in range(1, max_number):
        if i not in numbers:
            print(i)
            break
    else:
        print(max_number + 1)
