def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


def merge_sort_dict(dict, key, descending):
    if len(dict) <= 1:
        return
    mid = len(dict) // 2
    left = dict[:mid]
    right = dict[mid:]

    merge_sort_dict(left, key, descending)
    merge_sort_dict(right, key, descending)

    merge_two_sorted_dicts(left, right, dict, key, descending)


def merge_two_sorted_dicts(a, b, arr, key, descending):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0
    while i < len_a and j < len_b:
        if descending:
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        else:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(arr)
    print(arr)
    elements = [
        {"name": "vedanth", "age": 17, "time_hours": 1},
        {"name": "rajab", "age": 12, "time_hours": 3},
        {"name": "vignesh", "age": 21, "time_hours": 2.5},
        {"name": "chinmay", "age": 24, "time_hours": 1.5},
    ]
    merge_sort_dict(elements, "time_hours", False)
    print(elements)
