#
# @lc app=leetcode.cn id=2396 lang=python3
#
# [2396] 严格回文的数字
#

# @lc code=start
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        res = ''
        t = n - 2
        # 转换成n-2进制
        while n:
            res = str(n % t) + res
            n //= t
        # 判断是否是回文
        return res == res[::-1]

# @lc code=end

