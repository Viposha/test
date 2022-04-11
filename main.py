def main():
    from sys import getsizeof  # DONE now import only the function that is being used from module
    import time
    # start change
    start = time.time()

    test_set = range(100000)
    print(f' The length of set is {len(test_set)} numbers')

    test_list = list(test_set)
    test_tuple = tuple(test_set)
    # TODO: call test_list and test_tuple funcs several times

    print(type(test_list))
    print(type(test_tuple))

    print(f'Size of test_list is {getsizeof(test_list)} bytes')
    print(f'Size of test_tuple is {getsizeof(test_tuple)} bytes')
    # TODO reformat code to fit only 89 positions per line
    print(
        f'The difference in memory between test_tuple and test_list is {getsizeof(test_list) - getsizeof(test_tuple)} bytes')

    end = time.time()
    print(f'Runtime is {end - start} sec')


if __name__ == '__main__':
    main()
