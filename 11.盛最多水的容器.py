# @before-stub-for-debug-begin
from python3problem11 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, temp_1, temp_2 = 0, 0, len(height) - 1
        while temp_1 < temp_2:
            w = temp_2 - temp_1
            if height[temp_1] < height[temp_2]:
                h = height[temp_1]
                temp_1 += 1
            else:
                h = height[temp_2]
                temp_2 -= 1
            res = max(res, w*h)
        return res
        # @lc code=end
