#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(nums):
            n = len(nums)
            if n <= 2:
                return True
            diff = nums[1] - nums[0]
            for i in range(2, n):
                if nums[i] - nums[i-1] != diff:
                    return False
            return True
        m = len(l)
        res = [False] * m
        idx = 0
        for i, j in zip(l, r):
            tmp = sorted(nums[i:j+1])
            res[idx] = isArithmetic(tmp)
            idx += 1
        return res

# @lc code=end

