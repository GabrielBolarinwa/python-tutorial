def bubble_sort_array(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break


def bubble_sort_dict(elements, key):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    numbers_list = [38, 9, 39, 7, 2, 15, 28]
    elements = [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-18"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "amir", "transaction_amount": 800, "device": "iphone-8"},
    ]
    bubble_sort_array(numbers_list)
    bubble_sort_dict(elements, "name")

    print(numbers_list)
    print(elements)
