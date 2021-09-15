from copy import deepcopy


def n_arr(sizes):
    if len(sizes) == 0:
        return []

    current_size = sizes[-1]

    if len(sizes) == 1:
        return ['""'] * current_size
    else:
        sizes = sizes[:-1]
        nested_arr = n_arr(sizes)
        return [deepcopy(nested_arr) for _ in range(current_size)]


if __name__ == '__main__':
    print(n_arr([2, 2, 2]))
