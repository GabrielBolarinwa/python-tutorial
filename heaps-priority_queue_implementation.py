import heapq
from collections import Counter


def heapsort(arr: list):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list


if __name__ == "__main__":
    A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

    heapq.heapify(A)
    print(A)
    heapq.heappush(A, 4)
    print(A)
    minn = heapq.heappop(A)
    print(A, minn)
    heapq.heappushpop(A, 4)
    elements = heapsort([11, 9, 29, 2, 15, 28])
    print(elements)

    # Max heap uses the value's its additive inverse
    B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
    n = len(B)
    for i in range(n):
        B[i] = -B[i]

    heapq.heapify(B)
    print(B)

    C = [-5, 4, 2, 1, 7, 0, 3]
    heap = []
    for x in C:
        heapq.heappush(heap, x)
        print(heap)

    D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

    counter = Counter(D)
    heap2 = []
    for k, v in counter.items():
        heapq.heappush(heap2, (v, k))
    print(heap2)
