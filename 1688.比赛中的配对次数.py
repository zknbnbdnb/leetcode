#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n != 1:
            res += n // 2
            n = n // 2 + 1 if n % 2 else n // 2
        return res
# @lc code=end


s = Solution()
print(s.numberOfMatches(7*2))
