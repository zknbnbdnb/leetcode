#
# @lc app=leetcode.cn id=2348 lang=python3
#
# [2348] 全 0 子数组的数目
#
from typing import List
# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while l < len(nums):
            if nums[l] == 0:
                r = l
                while r < len(nums) and nums[r] == 0:
                    r += 1
                res += (r - l) * (r - l + 1) // 2 
                l = r
            else:
                l += 1
        return res

# @lc code=end

