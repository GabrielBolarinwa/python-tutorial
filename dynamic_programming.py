class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one += two
            two = temp
        return one

    @staticmethod
    def minCostClimbingStairs(cost: list[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])

    @staticmethod
    def rob(nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob2(self, nums: list[int]):
        return max(nums[0], self.rob(nums[1:]), self.rob(nums[:-1]))


solution = Solution()
print(solution.climbStairs(5))
print(solution.minCostClimbingStairs([10, 15, 20]))
print(solution.rob([1, 2, 3, 1]))
print(solution.rob2([2, 3, 2]))
