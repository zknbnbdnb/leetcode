# @before-stub-for-debug-begin
from python3problem414 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return max(nums)
        return nums[2]
# @lc code=end
