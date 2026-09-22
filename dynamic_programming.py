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

    @staticmethod
    def longestPalindrome(s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

    def num_of_palindromic_substrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPalindromes(i, i, s)
            res += self.countPalindromes(i, i + 1, s)
        return res

    @staticmethod
    def countPalindromes(l: int, r: int, s: str):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    @staticmethod
    def numDecodings(s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]

    @staticmethod
    def coinChange(coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else 0

    @staticmethod
    def maxProduct(nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax, curMin)
        return res


solution = Solution()
print(solution.climbStairs(5))
print(solution.minCostClimbingStairs([10, 15, 20]))
print(solution.rob([1, 2, 3, 1]))
print(solution.rob2([2, 3, 2]))
print(solution.longestPalindrome("babad"))
print(solution.num_of_palindromic_substrings("aaab"))
print(solution.numDecodings("121"))
print(solution.coinChange([1, 3, 4, 5], 7))
print(solution.maxProduct([1, 2, 3, 5]))
