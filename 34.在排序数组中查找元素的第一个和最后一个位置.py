# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        res.append(self.searchFirstEqualElement(nums, target))
        res.append(self.searchLastEqualElement(nums, target))
        return res

    def searchFirstEqualElement(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                end = mid - 1
        return -1

    def searchLastEqualElement(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid+1] != target:
                    return mid
                start = mid + 1
        return -1
        # @lc code=end
