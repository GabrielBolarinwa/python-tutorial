import time


def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]
    if mid_number == number_to_find:
        return mid_index
    elif mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursive(
        numbers_list, number_to_find, left_index, right_index
    )


def find_all_occurences(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == "__main__":
    numbers_list = [12, 15, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 45
    t1 = time.perf_counter()

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")
    indices = find_all_occurences(numbers_list, 15)
    print(f"15 is at indices {indices}")
    t2 = time.perf_counter()
    print(t2 - t1)
