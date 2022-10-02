from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        over = 1
        for index in range(len(digits) - 1, -1, -1):
            digits[index] += over
            digits[index], over = digits[index] % 10, digits[index] // 10
            if digits[index]:
                return digits
        return [1] + digits
