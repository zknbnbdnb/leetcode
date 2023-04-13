#
# @lc app=leetcode.cn id=2481 lang=python3
#
# [2481] 分割圆的最少切割次数
#

# @lc code=start
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        return n if n % 2 else n // 2
# @lc code=end

