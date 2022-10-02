# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        last_symbol = "I"
        for i in range(len(s) - 1, -1, -1):
            if symbol_value[s[i]] >= symbol_value[last_symbol]:
                result += symbol_value[s[i]]
            else:
                result -= symbol_value[s[i]]
            last_symbol = s[i]
        return result


s = Solution()
assert s.romanToInt("III") == 3
assert s.romanToInt("LVIII") == 58
assert s.romanToInt("MCMXCIV") == 1994
