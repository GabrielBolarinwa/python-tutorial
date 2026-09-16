def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def hoare_partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    return end


def lomuto_partition(elements, start, end):
    i = start - 1
    j = 0

    pivot_index = end
    pivot = elements[pivot_index]

    while j <= end - 1:
        if elements[j] < pivot:
            i += 1
            swap(i, j, elements)
        j += 1
    swap(i + 1, pivot_index, elements)
    return i + 1


def lomuto_sort(elements, start, end):
    if start < end:
        pi = lomuto_partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


def quick_sort(elements, start, end):
    if start < end:
        pi = hoare_partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    numbers = [3, 7, 1, 9, 2]
    quick_sort(elements, 0, len(elements) - 1)
    lomuto_sort(numbers, 0, len(numbers) - 1)
    print(elements)
    print(numbers)
