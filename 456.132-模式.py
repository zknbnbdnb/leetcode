#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132 模式
#

# @lc code=start
from inspect import stack


class Solution:
    def find132pattern(self, nums) -> bool:
        if len(nums) < 3:
            return False
        stack, temp = [], -2**31
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < temp:
                return True
            while len(stack) != 0 and nums[i] > stack[-1]:
                temp = stack.pop()
            stack.append(nums[i])
        return False
# @lc code=end


nums = [3, 5, 0, 3, 4]
s = Solution()
print(s.find132pattern(nums))
