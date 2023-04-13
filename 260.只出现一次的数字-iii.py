#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        res = []
        dict = {}
        for key in nums:
            dict[key] = dict.get(key, 0) + 1
        for key, val in dict.items():
            if val == 1:
                res.append(key)
        return res
# @lc code=end


nums = [1, 2, 1, 3, 2, 5]
s = Solution()
print(s.singleNumber(nums))
