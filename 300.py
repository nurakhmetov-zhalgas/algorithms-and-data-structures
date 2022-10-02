# https://leetcode.com/problems/longest-increasing-subsequence/
import math
import bisect


def lis(nums):
    dp = [math.inf for _ in range(len(nums) + 1)]
    dp[0] = -math.inf
    size = 0
    for i in range(len(nums)):
        j = bisect.bisect_right(dp, nums[i])
        if dp[j - 1] < nums[i] and nums[i] < dp[j]:
            dp[j] = nums[i]
            size = max(size, j)
    return size
