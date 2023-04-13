#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        length = len(nums) + 1
        nums = set(nums)
        for i in range(1, length):
            if i not in nums:
                res.append(i)
        return res
        # @lc code=end


nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
print(s.findDisappearedNumbers(nums))
