# Binary Search is an algorithm to search a sorted dataset
# Each time the sorting is run , the n of elements to be searched gets halved
# So, it is much faster than linear search.

# Code snippet below shows the implementation of binary search and comparison with linear search
from utils import time_it


@time_it
def linear_search(array_list, n):
    for i, element in enumerate(array_list):
        if element == n:
            return i
    return -1


@time_it
def binary_search(array_list, n):
    left_index = 0
    right_index = len(array_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = array_list[mid_index]

        if mid_number == n:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursive(array_list, n, left, right):
    if right < left:
        return -1

    mid_index = (left + right) // 2
    mid_number = array_list[mid_index]

    if mid_number == n:
        return mid_index

    if mid_number < n:
        left = mid_index + 1
    else:
        right = mid_index - 1

    return binary_search_recursive(array_list, n, left, right)


if __name__ == "__main__":
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 45

    # numbers_list = [i for i in range(1000001)]
    # number_to_find = 1000000

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number Found at index {index} using linear search.")
