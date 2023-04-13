# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # for i, _ in enumerate(digits):
        #     digits[i] = str(digits[i])
        # res = ''.join(digits)
        # res = str(int(res) + 1)
        # res = list(res)
        # for i, _ in enumerate(res):
        #     res[i] = int(res[i])
        # return res
        res = 0
        i = len(digits)
        for val in digits:
            res += val*10**(i-1)
            i -= 1
        return [int(x) for x in str(res+1)]
# @lc code=end
