# @before-stub-for-debug-begin
from python3problem229 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        lenght = len(nums)
        for key in nums:
            dic[key] = dic.get(key, 0) + 1
        for key, val in dic.items():
            if val > int(lenght/3):
                res.append(key)
        return res
# @lc code=end
