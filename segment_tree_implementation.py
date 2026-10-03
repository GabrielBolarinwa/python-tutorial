class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, index, low, high):
        if low == high:
            self.tree[index] = self.arr[low]
            return
        mid = (low + high) // 2
        self.build(2 * index + 1, low, mid)
        self.build(2 * index + 2, mid + 1, high)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def query(self, start, end):
        return self.query_helper(0, 0, self.n - 1, start, end)

    def query_helper(self, index, low, high, start, end):
        if low > end or high < start:
            return 0
        if low >= start and high <= end:
            return self.tree[index]
        mid = (low + high) // 2
        left_sum = self.query_helper(2 * index + 1, low, mid, start, end)
        right_sum = self.query_helper(2 * index + 1, mid + 1, high, start, end)
        return left_sum + right_sum

    def update(self, index, value):
        self.arr[index] = value
        self.build(0,0,self.n-1)


if __name__ == "__main__":
    arr = [1, 2, 3]
    seg_tree = SegmentTree(arr)
    print(seg_tree.query(0, 2))
    seg_tree.update(3,4)