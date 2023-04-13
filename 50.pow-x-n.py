# @before-stub-for-debug-begin
from python3problem50 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return x
        # if n < 0:
        #     x = 1 / x
        #     n = -n
        # temp = self.myPow(x, int(n/2))
        # if n % 2 == 0:
        #     return temp * temp
        # return temp * temp * x

        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        mut, num = x, n
        while num != 0:
            if num & 1:
                res *= mut
            mut *= mut
            num = num >> 1
        return res
        # @lc code=end
