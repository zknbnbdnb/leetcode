#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                continue
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
# @lc code=end
