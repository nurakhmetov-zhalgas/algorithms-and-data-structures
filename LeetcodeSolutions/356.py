from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def is_reflected(self, points: List[List[int]]) -> bool:
        point_count = defaultdict(int)
        left_point = inf
        right_point = -inf
        for point in points:
            point_count[tuple(point)] += 1
            left_point = min(left_point, point[0])
            right_point = max(right_point, point[0])
        candidate = left_point + right_point
        for point in points:
            reflected_point = candidate - point[0], point[1]
            if point_count[tuple(point)] != point_count[reflected_point]:
                return False
        return True
