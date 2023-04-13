#
# @lc app=leetcode.cn id=1590 lang=python3
#
# [1590] 使数组和能被 P 整除
#
from typing import List
from itertools import accumulate
# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))
        x = pre[n] % p
        if x == 0:
            return 0
        hashmap = {0: 0}
        ans = n
        for i in range(n):
            y = pre[i + 1] % p
            hashmap[y] = i + 1
            z = (y - x) % p
            if z in hashmap:
                ans = min(ans, i + 1 - hashmap[z])
        return ans if ans < n else -1



    

# @lc code=end

