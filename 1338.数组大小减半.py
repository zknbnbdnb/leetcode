#
# @lc app=leetcode.cn id=1338 lang=python3
#
# [1338] 数组大小减半
#

# @lc code=start
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = Counter(arr)
        l = sorted(d.values(), reverse=True)
        n = len(arr)
        ans = 0
        for i in range(len(l)):
            n -= l[i]
            ans += 1
            if n <= len(arr) // 2:
                break
        return ans
# @lc code=end

