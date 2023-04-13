#
# @lc app=leetcode.cn id=2221 lang=python3
#
# [2221] 数组的三角和
#

# @lc code=start
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for j in range(len(nums) - 1, 0, -1):
            for i in range(j):
                nums[i] = (nums[i] + nums[i+1]) % 10
        return nums[0]
# @lc code=end

