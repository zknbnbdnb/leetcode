#
# @lc app=leetcode.cn id=1551 lang=python3
#
# [1551] 使数组中所有元素相等的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n // 2) ** 2
        else:
            t = (n + 1) // 2
            return t * (t - 1)
# @lc code=end

