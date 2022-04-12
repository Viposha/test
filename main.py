def main():
    print('=' * 79)
    from sys import getsizeof  # DONE now import only the function that is being used from module
    import time
    # start change
    start = time.time()

    test_set = range(100_000)  # separator _ here?
    len_range = len(test_set)

    print(f'The length of set is {len_range:,} numbers')  # separate with comma

    test_list = list(test_set)
    test_tuple = tuple(test_set)
    # calli list and tuple for
    a = 0
    while a < 10:
        callable(test_tuple)
        callable(test_list)
        a = a + 1
    # TODO: call test_list and test_tuple funcs several times

    print(type(test_list))
    print(type(test_tuple))
    list_compreh = [x for x in range(100_000)]  # list comprehention
    tuple_gen = tuple(i for i in range(100_000))  # tuple generator
    print(
        f'Size of test_list is {getsizeof(test_list):,} bytes\n'
        f'Size of list_compreh is {getsizeof(list_compreh):,} bytes\n'
        f'Size of test_tuple is {getsizeof(test_tuple):,} bytes\n'
        f'Size of tuple_gen is {getsizeof(tuple_gen):,} bytes'
    )
    # print(f'Size of test_tuple is {getsizeof(test_tuple):,} bytes')
    # TODO reformat code to fit only 89 positions per line
    print(
        f'The difference in memory between test_tuple and test_list is '
        f'{getsizeof(test_list) - getsizeof(test_tuple)} bytes\n'
        f'The difference in memory between list_compeh and tuple_gen is '
        f'{getsizeof(list_compreh) - getsizeof(tuple_gen)} bytes'
        )

    end = time.time()
    print(f'Runtime is {round((end - start), 4)} sec')  # round to 4 decimal digits
    print('=' * 79)


if __name__ == '__main__':
    main()
