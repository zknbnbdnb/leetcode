#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l, r = 0, k
        t = sum(arr[:k])
        while r <= len(arr):
            if t >= k * threshold:
                res += 1
            t -= arr[l]
            l += 1
            if r < len(arr):
                t += arr[r]
            r += 1
            
        return res
# @lc code=end

