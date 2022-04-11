def main():
    import sys # TODO now import only the function that is being used from module
    import time

    start = time.time()

    set = range(100000)
    print(f' The length of set is {len(set)} numbers')

    test_list = list(set)
    test_tuple = tuple(set)
    # TODO: call test_list and test_tuple funcs several times

    print(type(test_list))
    print(type(test_tuple))

    print(f'Size of test_list is {sys.getsizeof(test_list)} bytes')
    print(f'Size of test_tuple is {sys.getsizeof(test_tuple)} bytes')
    # TODO reformat code to fit only 89 positions per line
    print(f'The difference in memory between test_tuple and test_list is {sys.getsizeof(test_list)-sys.getsizeof(test_tuple)} bytes')

    end = time.time()
    print(f'Runtime is {end-start} sec')




if __name__ == '__main__':
    main()