# @before-stub-for-debug-begin
from python3problem509 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


class Solution:

    def fib(self, n: int) -> int:
        res = 0
        res = self.fib1(n, res)
        return res

    def fib1(self, n, res):
        if n <= 1:
            return n
        res += self.fib1(n - 1, res) + self.fib1(n - 2, res)
        return res

# @lc code=end
