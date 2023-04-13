#
# @lc app=leetcode.cn id=2488 lang=python3
#
# [2488] 统计中位数为 K 的子数组
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        pre = 0
        p = nums.index(k)
        for i in range(p):
            if nums[i] > k:
                pre += 1
            else:
                pre -= 1
            d[pre] += 1
        ans = 0
        for i in range(p, n):
            if nums[i] > k:
                pre += 1
            if nums[i] < k:
                pre -= 1
            ans += d[pre] + d[pre - 1]
        return ans

s = Solution()
print(s.countSubarrays([3,2,1,4,5], 4))

# @lc code=end

