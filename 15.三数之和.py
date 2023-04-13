# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, length = [], len(nums)
        if length < 3:
            return res
        nums.sort()
        mid = 1
        while mid < length - 1:
            first, last = 0, length - 1
            if mid > 1 and nums[mid] == nums[mid-1]:
                first = mid - 1
            while first < mid and last > mid:
                if first > 0 and nums[first] == nums[first - 1]:
                    first += 1
                    continue
                if last < length - 1 and nums[last] == nums[last + 1]:
                    last -= 1
                    continue
                sum = nums[first] + nums[mid] + nums[last]
                if sum == 0:
                    res.append([nums[first], nums[mid], nums[last]])
                    first += 1
                    last -= 1
                elif sum < 0:
                    first += 1
                else:
                    last -= 1
            mid += 1
        return res

        # @lc code=end
