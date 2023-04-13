#
# @lc app=leetcode.cn id=1833 lang=python3
#
# [1833] 雪糕的最大数量
#
from typing import List
# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for i in range(len(costs)):
            if coins >= costs[i]:
                coins -= costs[i]
                res += 1
            else:
                break
        return res
# @lc code=end

