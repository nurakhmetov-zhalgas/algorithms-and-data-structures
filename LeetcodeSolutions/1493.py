from math import inf
from typing import List


class Solution:
    def longestSubarray_simple1(self, nums: List[int]) -> int:
        current = 0
        prev = 0
        ans = -inf
        for number in nums:
            if number == 1:
                current += 1
            else:
                prev = current
                current = 0
            ans = max(ans, prev + current)
        return ans if ans != len(nums) else len(nums) - 1

    def longestSubarray_simple2(self, nums: List[int]) -> int:
        left = 0
        longest = 0
        last_zero = -1
        for right, value in enumerate(nums):
            if value == 0:
                left = last_zero + 1
                last_zero = right
            longest = max(longest, right - left)
        return longest

    def longestSubarray_dp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = nums[0]
        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0], dp[i][1] = dp[i - 1][0] + 1, dp[i - 1][1] + 1
            else:
                dp[i][0], dp[i][1] = 0, dp[i - 1][0]
        return max(dp[[i for j in dp for i in j]])

    def longestSubarray_sliding_window(self, nums: List[int]) -> int:
        left = 0
        available_deletions = 1
        correction = available_deletions - 1
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                available_deletions -= 1
            while available_deletions < 0:
                if nums[left] == 0:
                    available_deletions += 1
                left += 1
            res = max(res, right - left - correction)
        return res

    def longestSubarray_sliding_window_2(self, nums: List[int]) -> int:
        available_deletions = 1
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                available_deletions -= 1
            if available_deletions < 0:
                if nums[left] == 0:
                    available_deletions += 1
                left += 1
        return right - left
