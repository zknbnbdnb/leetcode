#
# @lc app=leetcode.cn id=2279 lang=python3
#
# [2279] 装满石头的背包的最大数量
#
from typing import List
# @lc code=start
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        abs_res = [0] * len(capacity)
        for i in range(len(capacity)):
            abs_res[i] = capacity[i] - rocks[i]
        abs_res.sort()
        res = 0
        for i in range(len(abs_res)):
            if additionalRocks >= abs_res[i]:
                additionalRocks -= abs_res[i]
                res += 1
            else:
                break
        return res
# @lc code=end

