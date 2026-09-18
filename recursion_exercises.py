def sum_of_list(arr, start):
    if start < len(arr):
        return arr[start] + sum_of_list(arr, start + 1)
    return 0


print(sum_of_list([1, 2, 3, 4, 5], 0))


def sum_nested_lists(arr, start):
    total = 0
    for element in arr:
        if type(element) == type([]):
            total += sum_nested_lists(element, start + 1)
        else:
            total += element
    return total


print(sum_nested_lists([1, 2, [3, 4], [5, 6]], 0))


def get_factorial(int):
    if int > 1:
        int *= get_factorial(int - 1)
        return int
    return 1


print(get_factorial(5))


def sum_of_digits(int):
    if int == 0:
        return 0
    return (int % 10) + sum_of_digits(int // 10)


print(sum_of_digits(345))


def sum_of_series(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_series(n - 2)


print(sum_of_series(6))


def sum_of_harmonic_series(n):
    if n <= 0:
        return 0
    else:
        return 1 / n + sum_of_harmonic_series(n - 1)


print(sum_of_harmonic_series(7))


def geometric_sum(n, ratio):
    if n <= 1:
        return 1
    else:
        return n + geometric_sum(n / ratio, ratio)


print(geometric_sum(6, 2))


def power(number, exp):
    if exp == 0:
        return 1
    elif number == 0:
        return 0
    elif exp == 1:
        return number
    else:
        return number * power(number, exp - 1)


power(3, 4)


def get_hcf(a: int, b: int) -> float | int:
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high

    elif low == 1:
        return 1

    else:
        return get_hcf(low, high % low)


print(get_hcf(7, 21))
