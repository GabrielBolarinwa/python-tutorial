def selection_sort_arr(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def selection_sort_names(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j]["First Name"] < arr[min_index]["First Name"] or (
                arr[j]["First Name"] == arr[min_index]["First Name"]
                and arr[j]["Last Name"] < arr[min_index]["Last Name"]
            ):
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    elements = [78, 12, 15, 8, 611, 53, 23, 27]
    selection_sort_arr(elements)
    print(elements)
    names = [
        {"First Name": "Raj", "Last Name": "Nayyar"},
        {"First Name": "Suraj", "Last Name": "Sharma"},
        {"First Name": "Karan", "Last Name": "Kumar"},
        {"First Name": "Jade", "Last Name": "Canary"},
        {"First Name": "Raj", "Last Name": "Thakur"},
        {"First Name": "Raj", "Last Name": "Sharma"},
        {"First Name": "Kiran", "Last Name": "Kamla"},
        {"First Name": "Armaan", "Last Name": "Kumar"},
        {"First Name": "Jaya", "Last Name": "Sharma"},
        {"First Name": "Ingrid", "Last Name": "Galore"},
        {"First Name": "Jaya", "Last Name": "Seth"},
        {"First Name": "Armaan", "Last Name": "Dadra"},
        {"First Name": "Ingrid", "Last Name": "Maverick"},
        {"First Name": "Aahana", "Last Name": "Arora"},
    ]
    selection_sort_names(names)
    print(names)
