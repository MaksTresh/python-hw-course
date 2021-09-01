def main():
    input_str = input('> ')

    if input_str.isdecimal():
        number = int(input_str)
        if number % 2 == 0:
            print(number // 2)
        else:
            print(number * 3 + 1)
    elif input_str == 'cancel':
        return
    else:
        print('Не удалось преобразовать введенный текст в число.')

    main()


if __name__ == '__main__':
    main()
