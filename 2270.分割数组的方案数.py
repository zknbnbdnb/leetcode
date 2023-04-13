#
# @lc app=leetcode.cn id=2270 lang=python3
#
# [2270] 分割数组的方案数
#

# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l, r = nums[0], sum(nums) - nums[0]
        ans = 0 if l < r else 1
        for i in range(1, len(nums) - 1):
            l, r = l + nums[i], r - nums[i]
            print(l, r)
            if l >= r:
                ans += 1
        return ans

# @lc code=end

