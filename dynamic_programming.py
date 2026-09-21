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


solution = Solution()
print(solution.climbStairs(5))
print(solution.minCostClimbingStairs([3, 4]))
