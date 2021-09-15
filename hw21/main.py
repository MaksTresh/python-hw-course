def merge(iter1, iter2):
    iter1_finished = False
    iter2_finished = False

    val1 = None  # value of first iterator
    val2 = None  # value of second iterator
    unused_val = None  # number of unused iterator value

    while True:
        if unused_val != 1:
            try:
                val1 = next(iter1)
            except StopIteration:
                iter1_finished = True

        if unused_val != 2:
            try:
                val2 = next(iter2)
            except StopIteration:
                iter2_finished = True

        if iter1_finished and iter2_finished:
            break
        elif iter1_finished:
            yield val2
            unused_val = None
        elif iter2_finished:
            yield val1
            unused_val = None
        else:
            if val1 <= val2:
                yield val1
                unused_val = 2
            else:
                yield val2
                unused_val = 1


if __name__ == '__main__':
    for item in merge((x for x in range(1, 4)), (x for x in range(2, 5))):
        print(item, end=' ')
