#
# @lc app=leetcode.cn id=2562 lang=python3
#
# [2562] 找出数组的串联值
#

# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        res = []
        while i < j:
            res.append(int(str(nums[i]) + str(nums[j])))
            i += 1
            j -= 1
        if i == j:
            res.append(nums[i])
        return sum(res)

# @lc code=end

